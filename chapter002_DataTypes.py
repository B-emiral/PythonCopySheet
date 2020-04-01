#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:30:08 2020
@author: genelhesap
"""
# Bölüm 4: Veri Yapıları
#########################

#### LISTS
# Kapsayıcı
# Sıralı - Indexlenebilir
# Değiştirilebilir
list1 = [10,20,30]
type(list1)
list2 = [10,'a',3.1415]
type(list2)
list_sum = ["toplama", list1, list2]
list_sum[0]
list_sum[1]
len(list_sum)
dir(list)

#### LIST DETAILS
type(list_sum[0])
type(list_sum[1])
type(list_sum[1][0])
del list1
list_sum[1] # even if list1 is deleted, values still remains in object
list_sum[0:2]
list_sum[:2]
list_sum[2:]
list3 = ["a",10,[1,2,3,4,5]]
list3[2][4]
#add remove change
explist = ["ali","veli","berkcan","ayşe" ]
explist[1] = "intuivive language"
explist[2] = "python"
explist[1:3]= "a" , "b"
explist
#explist = explist + "kemal" causes error
explist = explist + ["kemal"]
del explist[1:3]
dir(explist)
#   .append()
explist.append("fatih") #explist.append("fatih","sultan") error
explist.remove("kemal") # only one argument is accepted
explist
explist.append("mustafa")
explist.append("fatih")
explist.remove("fatih") # iki tane varsa baştan siler
#   .insert()
#?explist.insert
explist.insert(0,"mehmet")
explist.insert(2,"mert")
explist.insert(len(explist),"songül")
explist.pop(0)
explist.pop(4)
explist.pop()   #last element is defaulted
explist
#   .count()
listA = ["ali","ahmet","ali","mehmet"]
listA.count("ali")
listA.count("ışık")
#   .copy()
listA_backup = listA.copy()
#   .extend() # multiple append or append with list
listB = ["ali","ahmet"]
listB.extend(["mehmet","ayşe"])
listB
#   .index() # find argument index
listB.index("mehmet")
#   .reverse()
listB
listB.reverse()
listB
#   .sort()
listName = ["cemal","ali","burak","3","Ada","Berk"]
listNum = [5,3,1]
listName.sort()
listNum.sort()
listName
listNum
listMix = ["cemal",3,"burak"] #listMix.sort() -> error
#   .clear() clear all elements
listName.clear()
listName


#### TUPLE
# Kapsayıcı
# Sıralı / Indexlenebilir
# DeğiştirileMEZ
tuple1 = ("ali",1995,180.5, ["erkek","Türk","Türkçe"])
tuple2 = "veli",1990,170.5, ["erkek","Türk","Türkçe"]
#tupple()
dir(tuple1)
#?tuple
type(tuple1)
singleTuple = "t"
type(singleTuple)
singleTuple = "t",  # !!!!!!!!!
type(singleTuple)
#operations
tupleA = "veli",1990,170.5, ["erkek","Türk","Türkçe"]
#tupleA[0] = "mehmet" ->error


#### DICTIONARY
# Kapsayıcı
# Sırasız / IndexleneMEZ # key-value
# Değiştirilebilir
dicA = {"Mehmet" : "ID:0101523" ,
        "REG" : "Regresyon Modeli" ,
        "LOJ" : "Lojistik Regresyon" ,
        "CART" : "Clasification and Regression"}
len(dicA)

dicB = {"Natural" : [0,1,2,3],
        "Integers" :[-3,-2,-1,"Natural"],
        -5: "Integer"
        }
dicB
#dicB[0] -> KeyError:0
dicB["Natural"]
dicB[-5]
#dicB["Integer"] causes error only key search is possible 
dicOfdic = {"furits":{ "apple" : 3,
                       "orange":4,
                       "banana":7
                    },
            "vegs" : { "cucumber":1,
                      "tomato" : 3
                    }
            }
dicOfdic["vegs"]
dicOfdic["vegs"]["tomato"]
#add new element to the dic
dicA
dicA["Ahmet"] = "ID:0101534"
dicA["Ahmet"] = "empty"
dicA[23] = "twentytree"
a = 31415
dicA[a] = "possible"
dicA[a]
dicA[31415]
a = 14
#dicA[a] if a change key is missing now
tupleA = "Hello",
dicA[tupleA] = "key tuple dictionary"
listA = [1,2,3]
#dicA[listA] = "impossible" error unhashable type


#### SET    performans için kullanılır
#   Kapsayıcıdır
#   Indexlenemez - Eşsiz Eleman Tutar
#   Değiştirilebilirdir
l = [1,1,2,3,4,5]
s = set(l)
s
stringA = "Hello World!"
s2 = set(stringA)
s2
t = ("Ali","Ali",2)
s3 = set(t)
s3
len(s3)
#s3[0]  error
listA = [1,2,3,4,5,"adam",4,4]
setA = set(listA)
setA
dir(setA)
setA.add("7")
setA.remove(1)
#setA.remove(1) error because there is no 1 anymore
setA.discard(1)
#other methods 
# difference
setA = set([1,2,3])
setB = set([3,4,5])
setDiff = setA - setB
setDiff
setB - setA
setDiff
setA.difference(setB)
#intersection and union
setA = set([1,2,3])
setB = set([3,4,5])
setA.intersection(setB)
setA&setB
setA.union(setB)
setA|setB
setA.intersection_update(setB)
setA
setA = set([1,2,3])
setA.symmetric_difference(setB)
# küme sorgulamaları
setA = set([1,2,3])
setB = set([3,4,5])
setA.isdisjoint(setB)
setA.issubset(setB)
setA.issuperset(setB)






















