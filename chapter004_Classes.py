#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:11:42 2020
@author: genelhesap
"""
# CLASSES

class VeriBilimci():
    bolum = ''
    python = 'Yes'
    sql = 'Yes'
    programming_languages = []
    deneyim = 0

VeriBilimci.python

#instantiation Sınıfın varsayılan özelliklerini değiştirmek
ali = VeriBilimci()
ali.python = 'No'
ali.programming_languages.append("c++")
veli = VeriBilimci()
veli.python     # answer is yes it is okey
veli.programming_languages[0] # c++ is here there is a problem

#class with initializer
class Personnel():
    personnelName = []
    totalEmployee = 0
    valid_languages = ["R","Python","Java","c++"]
    avg_salary = 4000
    def __init__(self):
        self.name = ''
        self.education = ''
        self.experience = 0
        self.programming_languages = []
        self.salary = 0

    def calcSalary(self):
        accurateLang = 0
        for i in self.programming_languages:
            if Personnel.valid_languages.count(i) :
                accurateLang += 1
        if accurateLang ==0:
            return 0
        self.salary = Personnel.avg_salary
        self.salary += accurateLang*0.1*Personnel.avg_salary
        self.salary *= (1 + self.experience*0.1) 
        return self.salary
    
    def addPersonnel(self,edu,exp,prg_list,name):
        self.name = name
        self.education = edu
        self.experience = exp
        self.programming_languages.extend(prg_list)
        self.salary = self.calcSalary()
        if self.salary == 0:
            print("we will call you later")
            return
        print("Offered Salary: ",self.salary," Will You Accept It? (y/n)" )
        accept = input()
        if accept=='y':
            Personnel.personnelName.append(name)
            Personnel.totalEmployee += 1
            self.printNewPersonnel()
        else:
            print("Good Luck!!!")
            
    def printNewPersonnel(self):
        print("Name: ",self.name)
        print("Edu: ",self.education)
        print("Exp: ",self.experience)
        print("Skills: ",self.programming_languages)
        print("Salary: ", self.salary)
        print("Welcome to your new Job!")


mehmet = Personnel()
mehmet.addPersonnel("CompEng",3,["Java","Python"],"Mehmet")

ali = Personnel()
ali.addPersonnel("PhyEng",5,["Python"],"Ali")


big = Personnel()
big.addPersonnel("CompEng+",0,["Python","Java","c++"],"Big")

ezi = Personnel()
ezi.addPersonnel("IndEng+",0,["Excel"],"Ezi")

Personnel.personnelName



#INHERITENCE


class Employees():
    def __init__(self,firstName,lastName):
        self.firstName = ""
        self.lastName = ""
        self.salary = 0

class DataScience(Employees):
    def __init__(self,firstName,lastName):
        self.Programming = []

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""
        
datascience001 = Employees("Mehmet","Kamu")

datascience002 = DataScience("Alper","Kamu")

























