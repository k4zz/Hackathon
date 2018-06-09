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
            temp = [int(entry[0]),
                    entry[1],
                    entry[2],
                    int(entry[3]),
                    int(entry[4]),
                    entry[5],
                    int(entry[6])]
            self._users[temp[0]] = temp[1:]

    def get_users(self):
        return self._users

    def push_base(self):
        with open('database.txt', 'w') as file:
            for ID in self._users.keys():
                temp = '{0};{1};{2};{3};{4};{5};{6};\n'.format(ID,
                                                            self._users[ID][0],
                                                            self._users[ID][1],
                                                            self._users[ID][2],
                                                            self._users[ID][3],
                                                            self._users[ID][4],
                                                            self._users[ID][5])
                file.write(temp)

    def incr_coffee_count(self, ID):
        self._users[ID][2] += 1
        self.push_base()

    def incr_maint_count(self, ID):
        self._users[ID][3] += 1
        self.push_base()

    def reset_coffee_count(self, ID):
        self._users[ID][2] = 0
        self.push_base()

    def reset_maint_count(self, ID):
        self._users[ID][3] = 0
        self.push_base()

    def add_user(self, surname, name, email):
        ID = max(self._users.keys())
        self._users[ID] = [surname, name, 0, 0, email, ID]
        self.push_base()
        
#new = Database()
#new_data = new.get_users()
#
#print(new_data[4])
#print(new.incr_coffee_count(4))
#print(new_data[4])