#!/usr/bin/python3
"""My add_item module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv

my_list = []
filename = 'add_item.json'
my_list = load_from_json_file(filename)
for i in range(1, len(argv)):
    my_list += [argv[i]]
save_to_json_file(my_list, filename)