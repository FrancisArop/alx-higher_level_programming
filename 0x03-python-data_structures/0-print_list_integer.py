#!/usr/bin/python3
#0-print_list_integer.py

def print_list_interger(my_list=[]):
    """Print all interger of a list"""
    for i in range (len(my_list)):
        print("{:d}".format(my_list[i]))
