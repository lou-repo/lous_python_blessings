#!/usr/bin/env python3

#import modules
import requests
import os
import sys 
import tarfile
import gzip
import shutil
import subprocess 

#archive extensions
targz_extension = ".tar.gz"

print('beginning wordpress download')

url = 'https://wordpress.org/latest.tar.gz'
r = requests.get(url, allow_redirects=True)
open('latest.tar.gz', 'wb').write(r.content)

print('download completed')

#print('extracting')
#wordpress_tar = tarfile.open('latest.tar.gz')
#wordpress_tar.extractall('./')
#wordpress_tar.close()
#print('extracting completed')

print('extracting')
process = subprocess.Popen(['tar','-xzf','latest.tar.gz','--strip-components=1'])
output, error = process.communicate()
print('extracting completed')


