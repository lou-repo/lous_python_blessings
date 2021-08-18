#!/usr/bin/python3
import sys
import paramiko
from paramiko import SSHClient
import subprocess
import time

host = input("IP or FQDN: ")
username = input("What is your username: " )
port = input("SSH Port Number: ")
command = "ls -l"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

def line_reader(lines):
	for line in lines:
		print(line.strip())

print(line_reader(lines))
time.sleep(3)


