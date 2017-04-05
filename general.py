
# This import is to make operating system calls using python

import os

# Function to create new storage directory if it doesn't exist

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to write output to file in directory

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
