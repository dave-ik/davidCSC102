# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Coffee:
    
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk  = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        print(f"you now have your coffee with {self.milk} milk, {self.sugar} sugar and {self.coffeemate} coffeemate")
        
        
mySugarFreeCoffee = Coffee(2,0,1)

myMuchFreeCoffee = Coffee(2,10,1)
