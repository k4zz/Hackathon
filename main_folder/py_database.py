# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:52:17 2018

@author: Mefisto
"""

class Database:
    def __init__(self):
        self._users = {}
        with open('database.txt', 'r') as file:
            temp = file.readlines()
            data = []
            for row in temp:
                data.append(row.split(';'))
    
        for entry in data:
            self._users[int(entry[0])] = entry[1:]

    def get_users(self):
        return self._users

new = Database()
new_data = new.get_users()

print(Database().get_users()[4])