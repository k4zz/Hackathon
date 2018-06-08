# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:52:17 2018

@author: Mefisto
"""

class Database:
    def __init__(self):
        Users = {}
        with open('database.txt') as file:
            temp = file.readlines()
            data = []
            for row in temp:
                data.append(row.split(';'))
    
        for entry in data:
            Users[int(entry[0])] = entry[1:]
