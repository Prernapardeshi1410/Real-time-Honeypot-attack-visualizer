@echo off
echo 
echo Cyber Deception Honeypot Demo
echo 

echo Clearing old logs...
type nul > logs.json

echo Starting Honeypot...
start cmd /k python honey.py

timeout /t 2 >nul

echo Running Attacker Simulator...
python attacker_simulator.py

timeout /t 2 >nul

echo Starting Web Dashboard...
start cmd /k python web.py

timeout /t 3 >nul

echo Opening Browser Dashboard...
start http://127.0.0.1:5000

echo Project Started Successfully!
