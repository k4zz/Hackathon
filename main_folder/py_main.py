# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 00:21:37 2018

@author: Mefisto
"""
import os
import time
import py_func
import py_comm

comm_dir = os.getcwd()
comm_read = 'C2P.txt'
comm_write = 'P2C.txt'

while True:
    if comm_read not in os.listdir(comm_dir):
        time.sleep(0.1)
        continue
    
    command = py_comm.read_data(comm_dir, comm_read)

    result = py_func.call_func(command)
    
    py_comm.write_data(comm_dir, comm_write, result)

    with open(os.path.join(comm_dir, '_' + comm_write), 'w') as out_file:
        out_file.write(result)

    os.rename('_' + comm_write, comm_write)
    
    time.sleep(0.1)