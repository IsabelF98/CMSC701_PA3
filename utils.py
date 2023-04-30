#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:30:54 2023

@author: Isabel
"""

import random
import numpy as np

# Function to create K and K' (list of strings)
# ---------------------------------------------
def word_lists(n,ratio):
    """
    Generates list K and K' where K is a list of words and K' is a list of
    the same words but a given ratio are relpaced with names.

    Parameters
    ----------
    n : int
        lenght of list (max is 1000)
    ratio : float
        ratio of replaced elements (must be from 0 to 1)

    Returns
    -------
    K : list
        list of words of length n
    Kp : list
        list of words with some names of length n

    """

    m = int(np.ceil(ratio*n)) # number of elements to replace in list

    # load list of workds and names
    word_file = open("words.txt", "r")
    name_file = open("names.txt", "r")
    words = word_file.read().split('\n')
    names = name_file.read().split('\n')
    
    # create K and K' with n elements
    K   = random.sample(words, n)
    Kp  = K.copy()
    
    aux = random.sample(names, m) # list of m names
    idx = random.sample(range(0, n), m) # list of m indecies
    
    # replace elements in K' with names
    for i in range(len(idx)):
        Kp[idx[i]] = aux[i]
    
    random.shuffle(Kp) # shuffle elements in K'
    
    return K, Kp

# Function to create list of unique integers
# ------------------------------------------
def unique_int_list(n, d):
    """
    This function creates a list of unique d-digit integers of length n.

    Parameters
    ----------
    n : int
        length of list
    d : int
        number of digits

    Returns
    -------
    list of unique integers

    """

    # Compute the minimum and maximum values for an m-digit integer
    min_val = 10 ** (d - 1)
    max_val = (10 ** d) - 1

    # Generate a list of unique integers
    nums = set()
    while len(nums) < n:
        nums.add(random.randint(min_val, max_val))

    return list(nums)

unique_list = unique_int_list(1000, 5)


# Function to create K and K' (list of ints)
# ------------------------------------------
def int_lists(n,ratio):
    """
    Generates list K and K' where K is a list of  unique 5-digit integers 
    and K' is  a list of the same integers but a given ratio are relpaced with 
    3 -digit integers.

    Parameters
    ----------
    n : int
        lenght of list (max is 1000)
    ratio : float
        ratio of replaced elements (must be from 0 to 1)

    Returns
    -------
    K : list
        list of 5-digit integers of length n
    Kp : list
        list of same integers  with some 3-digit integers of length n

    """
    m = int(np.ceil(ratio*n)) # number of elements to replace in list

    # create K and K' with n elements
    K   = unique_int_list(n, 5)
    Kp  = K.copy()
    
    aux = unique_int_list(m, 3) # list of m names
    idx = random.sample(range(0, n), m) # list of m indecies
    
    # replace elements in K' with names
    for i in range(len(idx)):
        Kp[idx[i]] = aux[i]
        
    random.shuffle(Kp) # shuffle elements in K'
    
    return K, Kp
    