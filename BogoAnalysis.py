# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:31:56 2023

@author: bendc
"""

import matplotlib.pyplot as plt
import numpy as np
import random

n = 2 

def random_list(n):
    '''
    Generates the list that will be used to run the BogoSort algorithm.
    If BogoSort is shown a list that is already sorted, the number of steps will
    of course be 1. Also, if a list given has duplicate elements, the algorithm
    should run faster because there are more possible solutions that create a 
    sorted list. For consistency's sake, this function ensures that the 
    list generated is not pre-sorted and does not contain any duplicate elements.
    
    '''
    if n == 1:
        return [random.randint(0,99)]
    randlist = []
    while len(randlist) < n:
        number = random.randint(0,99)
        if number not in randlist: #Ensures no duplicates in list
            randlist.append(number)
    while sorted(randlist) == randlist: #Ensures list is not already sorted
        random.shuffle(randlist)
    
    return randlist


trials = 10000

def bogo(n, trials):
    steps = 0
    for i in range(trials):
        mylist = random_list(n)
        while sorted(mylist) != mylist:
            random.shuffle(mylist)
            steps += 1
    return steps / int(trials)


x = [1, 2, 3, 4, 5, 6, 7, 8,]
y = [bogo(n, trials) for n in x] 


plt.figure(figsize=(5, 2.7))
plt.plot(x, y, label='Average')
plt.xlabel('Length of list')
plt.ylabel('Average steps to sort')
plt.title("Average steps to BogoSort a list of given length")
plt.legend()
