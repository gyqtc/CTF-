from gmpy2 import *

# 根据题目要求盲猜是Rabin攻击
n = 523798549
c = 162853095
e = 2
p = 10663
q = 49123


def Rabin_decrypt(c, p, q, n):
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)
    t = invert(q, p)
    s = invert(p, q)
    m1 = mod(mp * t * q + mq * s * p, n)
    m2 = mod(mp * t * q - mq * s * p, n)
    m3 = mod(n - m1, n)
    m4 = mod(n - m2, n)
    m = [m1, m2, m3, m4]
    return m


probm = Rabin_decrypt(c, p, q, n)
for i in probm:
    print(bin(i))
