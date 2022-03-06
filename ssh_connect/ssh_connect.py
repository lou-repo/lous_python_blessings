#!/usr/bin/python3
import sys
from tkinter import COMMAND
import paramiko
from paramiko import SSHClient
import subprocess
import time

HOST = input("IP or FQDN: ")
USERNAME = input("What is your username: " )
PORT = input("SSH Port Number: ")
COMMAND = "ls -l"

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