#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_username(user_name):
    print("hello_" + user_name + "!")

hello_username("USERNAME")

#Question 2: Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    first_odds = 0
    while first_odds < 100:
        first_odds += 1
        if first_odds % 2 == 0:
            continue
        print(first_odds)
        
first_odds()

#Question 3: Please write a Python fuction, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    print(max(a_list))

max_num_in_list([])

#Question 4: Write a function to return if the given year is a leap year.

def is_leap_year(a_year):
    if ((a_year % 4 == 0) and
    (a_year % 100 != 0 or
    a_year % 400)) == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")

is_leap_year()

#Question 5: Write a function to check to see if all numbers in a list are consecutive numbers.

def is_consecutive(a_list):
    for x in range(1, len(a_list)):
        if a_list[x] - a_list[x-1] != 1:
            print("The list is not consecutive.")
            return
    print("The list is consecutive.")
    
is_consecutive([])