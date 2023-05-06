#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:30:54 2023

@author: Isabel
"""

import random
import numpy as np


# Function for list of unique k-mers
# ----------------------------------
def unique_str_list(n, letters, d):
    """
    This function creates a list of unique strings of length n where each string
    is of lenth d and comprised of characters in the list letters.

    Parameters
    ----------
    n : int
        length of list
    letters : list of characters (strings)
        list of characters to comprise the strings
    d : int
        length of strings

    Returns
    -------
    list of unique strings

    """
    strs = set()
    while len(strs) < n:
        s = ''.join(random.choices(letters, k=d))
        strs.add(s)

    return list(strs)

# Function to create K and K' (list of strings)
# ---------------------------------------------
def string_lists(n,ratio):
    """
    Generates list K and K' where K is a list of k-mers and K' is a list of
    the same k-mers but a given ratio are relpaced with different k-mers.
    k = 32

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
    
    # create K and K' with n elements
    K = unique_str_list(n, ['A','C','G','T'], 32)
    Kp  = K.copy()
    
    aux = unique_str_list(m, ['B','D','F','U'], 32) # list of m names
    idx = random.sample(range(0, n), m) # list of m indecies
    
    # replace elements in K' with names
    for i in range(len(idx)):
        Kp[idx[i]] = aux[i]
    
    #random.shuffle(Kp) # shuffle elements in K'
    
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


# Function to create K and K' (list of ints)
# ------------------------------------------
def int_lists(n,ratio):
    """
    Generates list K and K' where K is a list of  unique 10-digit integers 
    and K' is  a list of the same integers but a given ratio are relpaced with 
    8 -digit integers.

    Parameters
    ----------
    n : int
        lenght of list (max is 1000)
    ratio : float
        ratio of replaced elements (must be from 0 to 1)

    Returns
    -------
    K : list
        list of 10-digit integers of length n
    Kp : list
        list of same integers  with some 8-digit integers of length n

    """
    m = int(np.ceil(ratio*n)) # number of elements to replace in list

    # create K and K' with n elements
    K   = unique_int_list(n, 10)
    Kp  = K.copy()
    
    aux = unique_int_list(m, 8) # list of m names
    idx = random.sample(range(0, n), m) # list of m indecies
    
    # replace elements in K' with names
    for i in range(len(idx)):
        Kp[idx[i]] = aux[i]
        
    #random.shuffle(Kp) # shuffle elements in K'
    
    return K, Kp

# Function to create K and K' (dict of strs and ints)
# ---------------------------------------------------
def str_int_dict(n,ratio):
    """
    Generates dictionaries K and K' where K is a dictionary with values of unique 
    k-mers (k=32) and keys of unique 10-digit integers and K' is  a dictionary
    of the same keys and values but a given ratio are relpaced with different 
    k-mers as values and 8 -digit integers as keys.

    Parameters
    ----------
    n : int
        number of elements in dictionaries
    ratio : float
        ratio of replaced elements (must be from 0 to 1)

    Returns
    -------
    K_dict : dict
        dictionary of int keys and k-mer values
    Kp_dict : dict
        same dictionary of int keys and k-mer values with some swapped

    """
    m = int(np.ceil(ratio*n))
    
    K_key = unique_int_list(n, 10)
    K_val = unique_str_list(n, ['A','C','G','T'], 32)
    Kp_key = K_key.copy()
    Kp_val = K_val.copy()
    
    aux_key = unique_int_list(m, 8)
    aux_val = unique_str_list(m, ['B','D','F','U'], 32)
    
    idx = random.sample(range(0, n), m)

    # replace elements in K' with names
    for i in range(len(idx)):
        Kp_key[idx[i]] = aux_key[i]
        Kp_val[idx[i]] = aux_val[i]

    K_dict = dict(zip(K_key, K_val))
    Kp_dict = dict(zip(Kp_key, Kp_val))
    
    return K_dict, Kp_dict
