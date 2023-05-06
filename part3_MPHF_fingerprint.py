#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 3: Augment the MPHF with a “fingerprint array”

Created on Sat May  6 11:34:34 2023

@author: Isabel
"""

import time
import numpy as np
import pandas as pd
import bbhash
import xxhash
import matplotlib.pyplot as plt
from utils import str_int_dict


#%% MPHF + Fingerprinting Test Function
#   -----------------------------------

def part3(n,ratio,b):
    # Generate K and K'
    # ----------------   
    K, Kp = str_int_dict(n,ratio)
    
    # Create MPHF
    # -----------
    num_threads = 1
    gamma = 1.0
    mph = bbhash.PyMPHF(list(K.keys()), n, num_threads, gamma)
    mph_size = mph.__sizeof__()
    
    # Create Fingerprint Array
    # ------------------------
    h = xxhash.xxh32()
    fp_arr = [0 for i in range(n)]
    for k in K.keys():
        idx = mph.lookup(k)
        h.update(K[k])
        bit = bin(xxhash.xxh32(K[k]).intdigest())[-int(b+1):-1]
        fp_arr[idx] = bit
        
    # Compute size of fingerprint array (in bits)
    # -------------------------------------------
    fp_size = 0
    for i in range(len(fp_arr)):
        fp_size += len(fp_arr[i])

    size = mph_size+fp_size
    
    # Check K' elemnts in MPHF + Fingerprint
    # --------------------------------------
    true_ct = 0
    false_pos_ct = 0
    false_neg_ct = 0
    
    start = time.time()
    for kp in Kp.keys():
        mphf_val = mph.lookup(kp)
        
        if mphf_val == None:
            mphf_check = False
        else:
            fp_val = fp_arr[mphf_val]
            h_val  = bin(xxhash.xxh32(Kp[kp]).intdigest())[-int(b+1):-1]
            if fp_val == h_val:
                mphf_check = True
            else:
                mphf_check = False

        true_check = kp in list(K.keys())
        
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

n_list = np.linspace(1000,10000,10)
ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# save last 7 bits
b = 7
false_pos_df1 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df1  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df1  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        print('n',n,'ratio',ratio)
        print(" ")
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part3(n,ratio,b)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df1["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df1["ratio "+str(round(ratio,2))]  = time_arr
    mem_size_df1["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df1['mean'] = CPU_time_df1.loc[:,[c for c in CPU_time_df1.columns if c!= "data size"]].mean(axis=1)
false_pos_df1.to_csv("false_pos_rate_MPHF_fp_err1.csv")

# save last 8 bits
b = 8
false_pos_df2 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df2  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df2  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        print('n',n,'ratio',ratio)
        print(" ")
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part3(n,ratio,b)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df2["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df2["ratio "+str(round(ratio,2))]  = time_arr  
    mem_size_df2["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df2['mean'] = CPU_time_df2.loc[:,[c for c in CPU_time_df2.columns if c!= "data size"]].mean(axis=1)
false_pos_df2.to_csv("false_pos_rate_MPHF_fp_err2.csv")

# save last 10 bits
b = 10
false_pos_df3 = pd.DataFrame(n_list, columns=["data size"])
CPU_time_df3  = pd.DataFrame(n_list, columns=["data size"])
mem_size_df3  = pd.DataFrame(n_list, columns=["data size"])

for ratio in ratio_list:
    rate_arr = np.zeros(len(n_list))
    time_arr = np.zeros(len(n_list))
    size_arr = np.zeros(len(n_list))
    
    for i in range(len(n_list)):
        n = int(n_list[i])
        print('n',n,'ratio',ratio)
        print(" ")
        true_rt, flase_pos_rt, flase_neg_rt, CPU_time, size = part3(n,ratio,b)
        rate_arr[i] = flase_pos_rt
        time_arr[i] = CPU_time
        size_arr[i] = size
        
    false_pos_df3["ratio "+str(round(ratio,2))] = rate_arr
    CPU_time_df3["ratio "+str(round(ratio,2))]  = time_arr  
    mem_size_df3["ratio "+str(round(ratio,2))]  = size_arr
    
CPU_time_df3['mean'] = CPU_time_df3.loc[:,[c for c in CPU_time_df3.columns if c!= "data size"]].mean(axis=1)
false_pos_df3.to_csv("false_pos_rate_MPHF_fp_err3.csv")



#%% Plots
#   -----

# CPU time b=7
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df1['data size'], CPU_time_df1["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for MPHF w/ Fingerprint Array $b=7$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# CPU time b=8
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df2['data size'], CPU_time_df2["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for MPHF w/ Fingerprint Array $b=8$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# CPU time b=10
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
for ratio in ratio_list:
    plt.plot(CPU_time_df3['data size'], CPU_time_df3["ratio "+str(round(ratio,2))],
             label="ratio "+str(round(ratio,2)))
plt.title("Query Time for MPHF w/ Fingerprint Array $b=10$")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# avg CPU time
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
plt.plot(CPU_time_df1['data size'], CPU_time_df1["mean"], label="$b=7$")
plt.plot(CPU_time_df2['data size'], CPU_time_df2["mean"], label="$b=8$")
plt.plot(CPU_time_df3['data size'], CPU_time_df3["mean"], label="$b=10$")
plt.title(" Average Query Time for MPHF w/ Fingerprint")
plt.xlabel("n")
plt.ylabel("time (sec)")
plt.legend()

# memory in bits
fig = plt.figure(figsize=(12,10))
plt.rcParams.update({'font.size': 22})
plt.plot(mem_size_df1['data size'], mem_size_df1["ratio 0.1"], label="$b=7$")
plt.plot(mem_size_df2['data size'], mem_size_df2["ratio 0.1"], label="$b=8$")
plt.plot(mem_size_df3['data size'], mem_size_df3["ratio 0.1"], label="$b=10$")
plt.title("MPHF w/ Fingerprint Array Memory")
plt.xlabel("n")
plt.ylabel("size (bits)")
plt.legend()



