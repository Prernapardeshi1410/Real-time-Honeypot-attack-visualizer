import subprocess
import webbrowser
import time
import sys

print("Starting Cyber Deception Honeypot Project...")

# Start honeypot
subprocess.Popen([sys.executable, "honeypot.py"])

# Give it time to start
time.sleep(1)

# Start web dashboard
subprocess.Popen([sys.executable, "web.py"])

# Give Flask time to start
time.sleep(1)

# Open browser automatically
webbrowser.open("http://127.0.0.1:5000/login")

print("Project is running. Browser opened automatically.")
