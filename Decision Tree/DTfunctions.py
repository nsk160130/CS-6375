
from math import log
from __future__ import division
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from collections import Counter,defaultdict
import operator

def PosNeg(X,Y):
    """
    This function separates the postiive and negative instances.
    """
    Xp = [s for (p,s) in zip(X,Y)   if p == 1 ]
    Xn = [s for (p,s) in zip(X,Y)   if p == 0 ]
    
    return (Xp,Xn)

def count(X):
    """
    This function returns sum of positive and negative examples.
    """
    return (sum(X),len(X)- sum(X))

def entropy(n,p):
    """
    This function calculates the entropy, the amount of information content the attribute carries.
    We make the use of entropy formula : sum(-p logp), where p is the probability of attribute p.
    """
    t = n+p
    if n == 0 and p == 0:
        return 0
    elif p == 0:
        return -(n/t)*log(n/t,2)
    elif n==0:
        return -(p/t)*log(p/t, 2)
    else:
        return ( (p/t)*log(p/t,2) + (n/t)*log(n/t,2) )

def InformationGain((P,N),(p1,n1),(p2,n2)):
    """
    This function takes the current attribute and calculates the Information Gain for splitting on next attribute,
    if we split on next attribute with p1 positive and n1 negative examples for P positive examples based on current attribute
    and p2 positive and n2 negative examples for N negative exmaples based on current attribute.
    """
    m1 = n1+p1
    m2 = n2+p2
    M = N+P

    return -(entropy(N,P) - ((m1/M)*entropy(n1,p1)+(m2/M)*entropy(n2,p2)))

def highIG(lst,Y):
    """
    Now we got to find for which attribute we get highest information gain.
    """
    temp = []
    for i in lst:
        x = InformationGain(count(Y),count(PosNeg(i,Y)[0]),count(PosNeg(i,Y)[1]))
        temp.append(x)
    index, value = max(enumerate(temp), key=operator.itemgetter(1))
    return index
