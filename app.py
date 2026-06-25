import subprocess
import os

def run_command(user_input):
    subprocess.call(user_input, shell=True)

def get_password():
    password = "admin123"
    return password

def read_file(filename):
    with open("/var/www/" + filename) as f:
        return f.read()

run_command("ls")
print("Password retrieved [REDACTED]")
