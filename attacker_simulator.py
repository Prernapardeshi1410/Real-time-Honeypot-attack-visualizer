import socket
import random
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8888   # same port as honeypot


usernames = ["admin", "root", "guest", "test", "user", "support","yash","nick ","Mukesh","amiee","michael","sysadmin","operator"]
passwords = ["123456", "password", "admin@123", "qwerty", "letmein", "welcome","hdg@jk","ami3288","SID4#@","lala@","653#g","mshv@$5","vhs*@54"]

for attempt in range(12):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))

        username = random.choice(usernames)
        password = random.choice(passwords)

        payload = f"username={username}, password={password}\n"
        s.send(payload.encode())

        print(f"[+] Sent -> {payload.strip()}")

        s.close()
        time.sleep(0.5)

    except Exception as e:
        print("Connection failed:", e)
        break
