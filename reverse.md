# CTF reverse刷题记录

## NSSCTF

### SWPUCTF2021 新生赛 fakerandom
- 知识点：python随机数初始化过程
- wp
```
import random

result = [201, 8, 198, 68, 131, 152, 186, 136, 13, 130, 190, 112, 251, 93, 212, 1, 31, 214, 116, 244]
random.seed(1)
l = []
for i in range(4):
    l.append(random.getrandbits(8))
flag = []
for i in range(len(l)):
    random.seed(l[i])
    for n in range(5):
        flag.append(result[i * 5 + n] ^ random.getrandbits(8))
string = ''
for i in flag:
    string += chr(i)
print(string)
```

## buuctf

### GUETCTF 2019 re
- 知识点：
- wp
```
x = [1629056, 6771600, 3682944, 10431000, 3977328, 5138336, 7532250, 5551632, 3409728, 13013670, 6088797, 7884663,
     8944053, 5198490, 4544518, 3645600, 10115280, 9667504, 5364450, 13464540, 5488432, 14479500, 6451830, 6252576,
     7763364, 7327320, 8741520, 8871876, 4086720, 9374400, 5759124]
y = [166163712, 731332800, 357245568, 1074393000, 489211344, 518971936, 406741500, 294236496, 177305856, 650683500,
     298351053, 386348487, 438258597, 249527520, 445362764, 174988800, 981182160, 493042704, 257493600, 767478780,
     312840624, 1404511500, 316139670, 619005024, 372641472, 373693320, 498266640, 452465676, 208422720, 515592000,
     719890500]
# 注意题目中少了一个值，需要通过该位来爆破
print(len(x))
print(len(y))
a = []
for i in range(len(x)):
    a.append(y[i] // x[i])
    print(i)
print(a)

for i in range(len(x)):
    if a[i] * x[i] != y[i]:
        print(i)
flag = ''
for i in a:
    flag += chr(i)
print(flag)
flag1 = flag[:6]
print(flag1)

```