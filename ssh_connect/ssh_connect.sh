#!/bin/bash

read -p 'Hostname or FQDN: ' HOST
read -p 'Username: ' USER

ssh $USER@$HOST

