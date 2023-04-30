#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 2: Empirical evaluation of a minimal perfect hash

Created on Sun Apr 30 11:37:14 2023

@author: Isabel
"""

import time
import numpy as np
import pandas as pd
import bbhash
import matplotlib.pyplot as plt
from utils import int_lists


#%% Bloom Filter Test Function
#   --------------------------

def part2(n,ratio):   
    # Generate K and K'
    # ----------------   
    K, Kp = int_lists(n,ratio)
    
    # Create MPHF
    # -----------
    num_threads = 1
    gamma = 1.0
    mph = bbhash.PyMPHF(K, n, num_threads, gamma)
    size = mph.__sizeof__()
    
    # Check K' elemnts in MPHF
    # ------------------------
    true_ct = 0
    false_pos_ct = 0
    false_neg_ct = 0
    
    start = time.time()
    for elm in Kp:
        mphf_val = mph.lookup(elm)
        
        if mphf_val == None:
            mphf_check = False
        else:
            mphf_check = True
        true_check  = elm in K
        
        if mphf_check and true_check:
            true_ct += 1
        elif not mphf_check and not true_check:
            true_ct +=1
        elif mphf_check and not true_check:
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

false_pos_df = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df  = pd.DataFrame(n_list, columns=["data size"])
for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    for i in range(len(n_list)):
        n = int(n_list[i])
        #print("ratio:",ratio,"n:",n)
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part2(n,ratio)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        #print(" ")
    false_pos_df["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df["ratio "+str(round(ratio,2))]  = time_arr
    mem_size_df["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df['mean'] = CPU_time_df.loc[:,[c for c in CPU_time_df.columns if c!= "data size"]].mean(axis=1)
false_pos_df.to_csv("false_pos_rate_df_mphf.csv")

#%% Plots
#   -----

fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df['data size'], CPU_time_df["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for MPHF")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
plt.plot(mem_size_df['data size'], mem_size_df["ratio 0.1"])
plt.title("MPHF memory")
plt.xlabel("n")
plt.ylabel("size (bits)")
plt.legend()






