#!/usr/bin/python3

import subprocess

user = input("What is your username: " )
host = input("What is the ip address or FDQN: ")

subprocess.Popen("ssh {user}@{host} -p {port} {cmd}".format(user=user, host=host, port=port, cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
