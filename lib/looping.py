#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    for i in range(num, 0, -1):
        if i == 1:
            print(i)
            print("Happy New Year!")
        else:
            print(i)
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [int ** 2 for int in int_list]
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)            
    pass

fizzbuzz()