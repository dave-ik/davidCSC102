# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:16:49 2021

@author: SST-Lab
"""

class XBank:
    loggedinCounter = 0
    def _init_(self, atmpin, theaccountbalance, thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        XBank.loggedinCounter = XBank.loggedinCounter + 1
        
    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print(f"Sorry we are not able to process at this time")
        else:
            print(f"Collect your cash...Thanks for banking with XBank")
            
    def ChangePin(self, newPin):
        self.atmpin = newPin
        print(f"Your pin has been changed...Thanks for banking with XBank")
    @classmethod
    def No0fCustomersLoggedin (cls):
        print(f"we have total of" + str(XBank.loggedinCounter) + "that have logged in")
        
        
f = open("C: \\Users\\SST-LAB\\Desktop\\database.txt",'r')

#print(f.readline())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(' ')
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
    break

print("enter your pin.....")

pasw = input()

if(pasw == password[0]):
    customer = XBank(password[0],accountB[0],name[0])