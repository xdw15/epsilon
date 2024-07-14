# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:54:12 2024

@author: P048168
"""

import numpy as np

#%% a)




n=10;i=3;j=5;c=4/5;s=3/5

def givensmat(n,i,j,c,s):
    
    
    if abs(c**2+s**2-1)>1e-15:
        raise Exception('the squares of c and s do not add to 1')
    
    if i<0:
        raise Exception('the given i is negative')
    elif j<0:
        raise Exception('the given j is negative')
        
    if i>=j:
        raise Exception('j must be greater than i')
        
    if j>n:
        raise Exception('j can not be greater than n')
    
    J=np.eye(n)
    
    J[i-1,i-1]=c
    J[j-1,i-1]=-s
    J[i-1,j-1]=s
    J[j-1,j-1]=c

    return J


J=givensmat(n,i,j,c,s)

#%% b)

a=np.arange(1,n+1)
A=np.vander(a,len(a)).astype(dtype=np.float64)


i=3;j=5;c=4/5;s=3/5

def givensxder(A,i,j,c,s):
        
    n=len(A)
    if abs(c**2+s**2-1)>1e-15:
        raise Exception('the squares of c and s do not add to 1')
    
    if i<0:
        raise Exception('the given i is negative')
    elif j<0:
        raise Exception('the given j is negative')
        
    if i>=j:
        raise Exception('j must be greater than i')
        
    if j>n:
        raise Exception('j can not be greater than n')
    
    A_out=A.copy()
    A_out[:,i-1]=A[:,i-1]*c-s*A[:,j-1]
    A_out[:,j-1]=A[:,i-1]*s+c*A[:,j-1]
    
    return A_out

AJ=givensxder(A,i,j,c,s)

A.dot(J)-AJ

A.dot(J)[:,i-1]
AJ[:,i-1]

A_out-A.dot(J)
    










