import subprocess
import os

def run_command(user_input):
    # Vulnerable to command injection
    subprocess.call(user_input, shell=True)

def get_password():
    # Hardcoded credentials - bad practice
    password = "admin123"
    return password

def read_file(filename):
    # Path traversal vulnerability
    with open("/var/www/" + filename) as f:
        return f.read()

run_command("ls")
print(get_password())
