# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:32:22 2018

@author: Mefisto
"""
import py_database

data = py_database.Database()

def coffeeCountInc(ID):
    data.incr_coffee_count(ID)
    return 'DONE'
    
def maintCountInc(ID):
    data.incr_maint_count(ID)
    return 'DONE'
    
def coffeeCountReset(ID):
    data.reset_coffee_count(ID)
    return 'DONE'
    
def maintCountReset(ID):
    data.reset_maint_count(ID)
    return 'DONE'
    
def addPerson(surname, name, email):
    data.add_user(surname, name, email)
    return 'DONE'
    
def choosePerson():
    return None

functions = {'coffeeCountInc': coffeeCountInc,
             'maintCountInc': maintCountInc,
             'coffeeCountReset': coffeeCountReset,
             'maintCountReset': maintCountReset,
             'addPerson': addPerson,
             'choosePerson': choosePerson}

def call_func(command):
    method = command[0]
    attribute  = command[1:-1]
    return functions[method](attribute)
