#coding: utf-8

import sys
import json

def load_list(filename):
    """
    argv:
        filename: file name
    return: word list of each line
    """
    word_lst = []
    with open(filename) as fr:
        word_lst = fr.readlines()
        word_lst[:] = [ line.strip() for line in word_lst]
    return word_lst


def load_set(filename):
    """
    argv:
        filename: file name
    return word set ofr each line
    """
    word_set = set(load_list(filename))
    return word_set

def load_dict(filename, delimiter='\t'):
    """
    """
    word_dict = {}
    with open(filename) as fr:
        for line in fr:
            try:
                key, value = line.strip().split(delimiter)
            except:
                continue
            word_dict[key] = value
    return word_dict


if __name__ == "__main__":
    filename = 'test'
    load_list(filename)
    load_set(filename)
    load_dict(filename)


    
    
    
