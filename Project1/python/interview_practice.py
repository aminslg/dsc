#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:00:55 2019

@author: amin
"""
import numpy as np
import math
#================================================================
def isPrime(x):
    if (x<=1):
        print('number should be greatet than one')
    elif x==2 or x==3:
        return True
    elif x==4:
        return False
    else:        
        for j in range(2,np.int(np.ceil(np.sqrt(x)))):
            if (x%j==0):
                return False
            else:
                return True
            
isPrime(14)         
num = list(range(2,51))
num
list(map(isPrime,num))
#====================================================================
def fib(n):
    if n==0 or n==1 :
        return (n)
    else:
        return (fib(n-1) + fib (n-2))
    
fib(20)   
#==================================================================
def fib2(n):
    if n==0 or n==1 :
        return (n)
    else:
        first = 0
        second = 1
        for i in range(2,n+1) :
            
            third = first + second
            first = second
            second = third
    return (third)        
            
fib2(20)            
#================================================================
def isFib(n):
    i = 0
    while fib2(i) <=n:
        if fib2(i)==n:
            return (True)
            break
        else:
            i +=1
    return(False)         
    
isFib(6765)  
#================================================================
def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return n == s*s
    
isPerfectSquare(25)

def isFib2(n):
    return (isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4))
        
for i in range(1,11):
    if isFib2(i)==True:
        print (i, "is a Fib number")
    else:
        print(i, "is NOT a Fib number")

#===============================================================
'''
Max subarray Sum

'''
mylist = [2,4,-1,3,0,5,-8,6]
l1 = mylist

def maxSubarray(mylist):
    l = len(mylist)
    current_sum = mylist[0]
    max_sofar = mylist[0]
    for i in range(1,l):
        current_sum = max(mylist[i],current_sum + mylist[i])
        max_sofar = max(max_sofar,current_sum)
    return (max_sofar)   
        
        
maxSubarray(mylist)        
#=================================================================
def maxSubarray2(mylist):
    l=len(mylist)
    max_ending_here = 0
    max_so_far = 0
    start = 0
    end = 0
    s = 0
    
    for i in range(0,l):
        max_ending_here += mylist[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    print ("Maximum sum is %d" %(max_so_far))
    print ("Start Index is %d" %(start))
    print ("End Index is %d" %(end))    
        
maxSubarray2(mylist)        
#===================================================================        
test = 'abcabdefghac'
ord(test[0])
#==================================================================
def my_sqrt(x):
    r = 32000
    l = 0
    while(r-l>1e-9):
        mid = (r+l)/2
        if mid*mid > x :
            r = mid
        else:
            l = mid
    return (r)        
        
my_list = list(range(1,20))  
my_list_sqrt1 = np.sqrt(my_list)   
    
my_list_sqrt2 = list(map(my_sqrt,my_list))    
#===================================================================
'''
Find the smallest positive number missing from an unsorted array
'''
def small(A):
    m = max(A)
    if m<0:
        return(1)
    if len(A)==1:
        if A[0]==1:
            return(2)
        else:
            return(1)
    my_list = [0]*m
    for i in range(len(A)):
        if A[i]>0:
            if my_list[A[i]-1] != 1:
               my_list[A[i]-1] = 1
    for i in range(len(my_list)):
        if my_list[i]==0:
           return(i+1)
        
    return(i+2)
A = [1,3,6,4,2,1]        
small(A)           
#================================================================          
abuse_word = ['Amin','Marjan','black tea']    
tweet = 'Negin Salighehdar Haha'
if any(word in tweet for word in abuse_word):
    print(True)
else:
    print(False)    


import os
housing_path = os.path.join('dataset','housing')
if not os.path.isdir(housing_path):
    os.makedirs(housing_path)




        
        
        
        
        
        
        
        
        
        
        
        
        


            
        
        
        
        
    
    



