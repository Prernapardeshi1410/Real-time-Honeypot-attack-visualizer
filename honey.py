import socket
import json
from datetime import datetime
from collections import defaultdict

# ANSI colors (work in Windows CMD)
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

HOST = "127.0.0.1"
PORT = 8888

attempt_counter = defaultdict(int)
BLOCK_THRESHOLD = 3

print(f"{GREEN}Cyber Deception Honeypot running...{RESET}")
print(f"{GREEN}Listening on {HOST}:{PORT}{RESET}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    conn, addr = server.accept()
    ip = addr[0]
    data = conn.recv(1024).decode().strip()
    conn.close()

    attempt_counter[ip] += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Attack classification
    severity = "INFO"
    attack_type = "Unknown Attempt"

    if "admin" in data or "root" in data:
        attack_type = "Default Credential Attack"
        severity = "CRITICAL"
    elif attempt_counter[ip] >= BLOCK_THRESHOLD:
        attack_type = "Brute Force Simulation"
        severity = "CRITICAL"
    else:
        attack_type = "Weak Credential Attempt"
        severity = "WARNING"

    # Fake auto-block
    if attempt_counter[ip] >= BLOCK_THRESHOLD:
        print(f"{RED}[BLOCKED]{RESET} {ip} temporarily blocked (simulation)")

    # Colored output
    color = GREEN if severity == "INFO" else YELLOW if severity == "WARNING" else RED

    print(
        f"{color}[{severity}]{RESET} {timestamp} | {attack_type} | "
        f"IP={ip} | DATA={data}"
    )

    log_entry = {
        "timestamp": timestamp,
        "ip": ip,
        "severity": severity,
        "attack_type": attack_type,
        "data": data
    }

    with open("logs.json", "a") as f:
        json.dump(log_entry, f)
        f.write("\n")
