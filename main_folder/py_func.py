# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:32:22 2018

@author: Mefisto
"""
import py_database

data = py_database.Database()

def coffeeCountInc(id):
    
    return 'DONE'

def choosePerson:
    

functions = {'coffeeCountInc': coffeeCountInc,
             'choosePerson': choosePerson}

def call_func(command):
    method = command[0]
    attribute  = command[1]
    return functions[method](attribute)
#def functions(name):
#    return funcs[name]