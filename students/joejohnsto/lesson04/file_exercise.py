# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Paths and File Processing

import os

# write print full path for all files in current directory
for _ in os.listdir():
    print(os.path.abspath(_))


# Copy file from source to destination
sourcedir = os.getcwd()
#destination = sourcedir + r'\new_students.txt'
#source = sourcedir + r'\students.txt'
destination = sourcedir + r'\MontyPython_new.jpg'
source = sourcedir + r'\MontyPython.jpg'

with open(source, 'rb') as infile, open(destination, 'wb') as outfile:
    while True:
        line = infile.readline()
        if not line:
            break
        outfile.write(line)


# File reading and parsing
pyclass = dict()
with open(sourcedir + r'\students.txt', 'r') as infile:
    header = infile.readline()
    while True:
        line = infile.readline()
        if not line:
            break
        student = line.split(':')
        name = student[0]
        langs = student[1].split(',')
        for i in range(len(langs)):
            langs[i] = langs[i].strip()
        nickname = ''
        if langs[0]:
            if langs[0][0].isupper():
                nickname = langs[0]
                langs = langs[1:]
        pyclass.update({name : dict({'nickname' : nickname, 'languages' : langs})})
