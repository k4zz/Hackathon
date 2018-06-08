# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:22:15 2018

@author: Mefisto
"""
import os

def read_data(filedir, filename):
    with open(os.path.join(filedir, filename), 'r') as read_file:
        read_data = read_file.readlines()[0]

    old_file = os.path.join(filedir, filename)
    new_file = os.path.join(filedir, '_' + filename)
    os.rename(old_file, new_file)

    command = read_data.split(' ')

    return command

def write_data(filedir, filename, result):
    with open(os.path.join(filedir, '_' + filename), 'w') as write_file:
        write_file.write(result)

    old_file = os.path.join(filedir, '_' + filename)
    new_file = os.path.join(filedir, filename)
    os.rename(old_file, new_file)
