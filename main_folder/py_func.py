# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:32:22 2018

@author: Mefisto
"""
import py_database

data = py_database.Database()

def coffeeCountInc(ID):
    data.incr_coffee_count(int(ID[0]))
    return 'DONE'
    
def maintCountInc(ID):
    data.incr_maint_count(int(ID[0]))
    return 'DONE'
    
def coffeeCountReset(ID):
    data.reset_coffee_count(int(ID[0]))
    return 'DONE'
    
def maintCountReset(ID):
    data.reset_maint_count(int(ID[0]))
    return 'DONE'
    
def addPerson(user):
    surname = user[0]
    name = user[1]
    email = user[2]
    data.add_user(surname, name, email)
    return 'DONE'
    
def choosePerson(blank):
    users = data.get_users()
    coffee_counts = []
    IDs = []
    for i in users.keys():
        IDs.append(i)
        coffee_counts.append(users[i][2])

    max_coffee_count = coffee_counts.count(max(coffee_counts))
    if max_coffee_count == 1:
        mail = users[IDs[coffee_counts.index(max(coffee_counts))]][4]
    else:
        maint_ID = []
        maint_counts = []
        for i in range(len(coffee_counts)):
            if coffee_counts[i] == max(coffee_counts):
                maint_ID.append(IDs[i])
                maint_counts.append(users[IDs[i]][3])
        min_maint_count = maint_counts.count(min(maint_counts))
        if min_maint_count == 1:
            mail = users[maint_ID[maint_counts.index(min(maint_counts))]][4]
        else:
            date_ID = []
            date_counts = []
            for i in range(len(maint_counts)):
                if maint_counts[i] == min(maint_counts):
                    date_ID.append(maint_ID[i])
                    date_counts.append(users[maint_ID[i]][5])
            mail = users[date_ID[date_counts.index(min(date_counts))]][4]
            
    return '{}\n'.format(mail)

def maintDone(attr):
    ID = int(attr[0])
    maint_date = int(attr[1])
    data.maint_done(ID, maint_date)
    data.reset_coffee_count(ID)
    data.incr_maint_count(ID)
    
    return 'DONE'

functions = {'coffeeCountInc': coffeeCountInc,
             'maintCountInc': maintCountInc,
             'coffeeCountReset': coffeeCountReset,
             'maintCountReset': maintCountReset,
             'addPerson': addPerson,
             'choosePerson': choosePerson,
             'maintDone': maintDone}

def call_func(command):
    method = command[0]
    attribute  = command[1:-1]
    return functions[method](attribute)
