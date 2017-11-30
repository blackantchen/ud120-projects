#!/usr/bin/python

"""
    Get POI names list from txt file
"""
from numpy import *
import operator

def get_poi_names_list():
    fr = open("../final_project/poi_names.txt")
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    return_mat = zeros((number_of_lines, 3))
    index = 0

    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index,:] = list_from_line[0:3]
        index += 1

    return return_mat

print "return mat:", get_poi_names_list()
