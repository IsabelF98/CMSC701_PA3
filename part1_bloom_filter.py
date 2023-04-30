#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 1: Empirical evaluation of the bloom filter

Created on Sat Apr 29 11:39:15 2023

@author: Isabel

"""

import time
import numpy as np
import pandas as pd
from bloom_filter2 import BloomFilter
import matplotlib.pyplot as plt
from utils import word_lists
    
#%% Bloom Filter Test Function
#   --------------------------

def part1(n,ratio,error_rate):   
    # Generate K and K'
    # ----------------   
    K, Kp = word_lists(n,ratio)
    
    # Create Bloom Filter
    # -------------------
    bloom = BloomFilter(max_elements=n, error_rate=error_rate)
    for elm in K:
        bloom.add(elm)
        
    size = bloom.num_bits_m
    
    # Check K' elemnts in Bloom Filter
    # --------------------------------
    true_ct = 0
    false_pos_ct = 0
    false_neg_ct = 0
    
    start = time.time()
    for elm in Kp:
        bloom_check = elm in bloom
        true_check  = elm in K
        if bloom_check and true_check:
            true_ct += 1
        elif not bloom_check and not true_check:
            true_ct +=1
        elif bloom_check and not true_check:
            false_pos_ct += 1
        else:
            false_neg_ct += 1
    end = time.time()
    CPU_time = end-start
    
    true_rt = true_ct/n
    flase_pos_rt = false_pos_ct/n
    flase_neg_rt = false_neg_ct/n
    
    return true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size


#%% Results
#   -------

n_list = np.linspace(50,1000,20)
ratio_list = np.linspace(0.1,0.6,6)

# error rate = 1/2^7
error_rate = 1/(2**7)
false_pos_df1 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df1  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df1  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part1(n,ratio,error_rate)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df1["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df1["ratio "+str(round(ratio,2))]  = time_arr  
    mem_size_df1["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df1['mean'] = CPU_time_df1.loc[:,[c for c in CPU_time_df1.columns if c!= "data size"]].mean(axis=1)
false_pos_df1.to_csv("false_pos_rate_bloom_err1.csv")

# error rate = 1/2^8
error_rate = 1/(2**8)
false_pos_df2 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df2  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df2  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part1(n,ratio,error_rate)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df2["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df2["ratio "+str(round(ratio,2))]  = time_arr  
    mem_size_df2["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df2['mean'] = CPU_time_df2.loc[:,[c for c in CPU_time_df2.columns if c!= "data size"]].mean(axis=1)
false_pos_df2.to_csv("false_pos_rate_bloom_err2.csv")

# error rate = 1/2^10
error_rate = 1/(2**10)
false_pos_df3 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df3  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df3  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part1(n,ratio,error_rate)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df3["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df3["ratio "+str(round(ratio,2))]  = time_arr  
    mem_size_df3["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df3['mean'] = CPU_time_df3.loc[:,[c for c in CPU_time_df3.columns if c!= "data size"]].mean(axis=1)
false_pos_df3.to_csv("false_pos_rate_bloom_err3.csv")

#%% Plots
#   -----

# CPU time error rate = 1/2^7
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df1['data size'], CPU_time_df1["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for Bloom Filter $error=1/2^7$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# CPU time error rate = 1/2^8
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df2['data size'], CPU_time_df2["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for Bloom Filterfor $error=1/2^8$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# CPU time error rate = 1/2^10
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df3['data size'], CPU_time_df3["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for Bloom Filter for $error=1/2^{10}$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# avg CPU time
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
plt.plot(CPU_time_df1['data size'], CPU_time_df1["mean"], label="$error=1/2^{7}$")
plt.plot(CPU_time_df2['data size'], CPU_time_df2["mean"], label="$error=1/2^{8}$")
plt.plot(CPU_time_df3['data size'], CPU_time_df3["mean"], label="$error=1/2^{10}$")
plt.title(" Average Query Time for Bloom Filter")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# memory in bits
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
plt.plot(mem_size_df1['data size'], mem_size_df1["ratio 0.1"], label="$error=1/2^{7}$")
plt.plot(mem_size_df2['data size'], mem_size_df2["ratio 0.1"], label="$error=1/2^{8}$")
plt.plot(mem_size_df3['data size'], mem_size_df3["ratio 0.1"], label="$error=1/2^{10}$")
plt.title("Bloom Filter Memory")
plt.xlabel("n")
plt.ylabel("size (bits)")
plt.legend()












