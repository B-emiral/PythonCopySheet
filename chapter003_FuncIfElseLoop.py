#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:41:48 2020
@author: genelhesap
"""
#   FUNCTIONS   CONDITIONALS    LOOPS
#   FUNCTIONS
print()
type(print)
dir(print)
# ?print when help wouldn't work

#   MATH OPERATIONS
2**3 #exponentiation
2//3 #integer division

#   USER DEFINED FUNCTIONS
#   tekrar eden görevleri yerine getirmek için yazılır
def kare_al(x):
    print("sayı:",x," karesi: "+ str(x**2) )      
kare_al(2)

def root_find(a,b,c,doPrint=1):
    delta = b**2 - 4*(a*c) #local variable: loop / if / function
    x1 = (-b -delta**0.5) / 2*a
    x2 = (-b +delta**0.5) / 2*a
    t = (x1,x2)
    if(doPrint == 1):
        print(str(a)+"a +" + str(b)+"b +" + str(c) + str(" =0"))
        print("Roots are: " , t) 
    return t
root_find(1,2,1,True) 
root_find(1,-5,7)  #for complex root
root_find(b=5,c=3,a=2)

# Global and Local Variable
listA = []
def append_list(toAdd):
    listA.append(toAdd) # first search in local area then global
append_list(3)

# Conditional and Control
limit = 100
limit == 2
2 <= limit

simple = 122
if simple < limit :
    print("Lower than limit")
elif simple == limit:
    print("Equal")
else:
    print("Higher")


#   LOOPS
for i in listA:
    if i < 3:
        print("isn't 3")
    else:
        print("it is tree")

a = 1.1
a_first = 1.03
while a < 100:
    a = a * a_first
print(a)




















