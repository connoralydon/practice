# decorators.py

"""
decorators are something that I've seen in python packages, but never understood.

they are a wrapper for functions. in the same way that functions can be passed into functions, decorators can be used to wrap functions.

I followed this guide in geeksforgeeks. 
https://www.geeksforgeeks.org/decorators-in-python/

"""

def my_decorator(func):
    def inner1(): # need this interior portion to make it work
        print("beginning of wrapped function")
        
        func()
        
        print("end of wrapped function")
    
    return inner1

@my_decorator 
def main_func():
    print("interior text")
    
# my_decorator(main_func)
main_func()


# for functions they need to have an inner portion where the inner function is returned


import time
import math

def calculate_time(func):
    
    def inner1(*args, **kwargs):
        
        begin = time.time()
        
        func(*args, **kwargs)
            
        end = time.time()
        
        print("Total time taken in : ",func.__name__, end - begin)
        
    return inner1 # this runs it

@calculate_time
def factorial(num):
    time.sleep(2)
    
    print(math.factorial(num))
    
# calculate_time(factorial(10)) # doesn't print the decorator properly
factorial(10)


# Python program to illustrate functions
# Functions can return another function
# only have one variable when creating the adder, but wrapping it into a variable allows to add y
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))