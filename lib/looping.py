#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter-= 1
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    return[x**2 for x in int_list]
    

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    
