#!/usr/bin/env python3

import os
import shlex
import shutil

"""
Creates "test" directories of specific size on which the pman and pfioh tests will be performed
"""

# Erases contents of directory in temp
def clean():
        if os.path.isdir("/tmp/files/"):
                shutil.rmtree('/tmp/files/')

# Creates a file with specific size in MB
def create(size, name):
        print("size: ",size)
        print("name: ", name)
        print("file location: /tmp/files/{size}{name}",)
        with open('/tmp/files/{size}{name}' , 'wb') as bigfile:
                bigfile.seek(1000000 * size - 1)
                bigfile.write(b'0')

# Creates a new directory to store files
def create_dir():
        os.makedirs("/tmp/files")

# Automates the entire processs : deletes directory, builds a new directory, and creates 10 files with specific size 
def automate(size):
        clean()
        create_dir()
        for y in range(10):
                print("Creating file with size : {size} & name : {size}{y}")
                create(size, y)

