from collections import Counter
import numpy as np

def mean(x: list) -> float:
    sizeOfList = len(x)

    total = float(0)
    for i in range(sizeOfList):
        total+=x[i]

    return total / sizeOfList

def median(x:list) -> float:

    l = 0
    r = len(x) - 1

    while (l < r):
        l+=1
        r-=1

    return (float(x[l]) + float(x[r]))/2

def mode(x:list) -> float:
    m = {}

    for i in range(len(x)):
        if x[i] in m:
            m[x[i]] += 1
        else:
            m[x[i]] = 1
            
    maxOcc = float(0)
    n = float(-1)
    
    for key,value in m.items():
        if value > maxOcc:
            maxOcc = value
            n = float(key)

    return n
    
def mean_median_mode(x: list) -> dict:
    x.sort()
    dict = {"mean":mean(x),"median":median(x),"mode": mode(x)}
    
    return dict