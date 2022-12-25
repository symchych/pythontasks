my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
#
# Write a program that prints out all the elements of the list that are higher than or equal 10.
# Instead of printing the elements one by one, make a new list that has all the elements higher
# than or equal 10 from this list in it and print out this new list.
# Ask the user for a number as input and return a list that contains only those elements
# from my_list that are higher than the number given by the user.


def filter_list_of_numbers(list_value):
    user_number_typedin = input("number: \n")
    user_number = int(user_number_typedin)
    outcome = []
    for l in list_value:
        try:
            if user_number >= l:
                outcome.append(l)
            else:
                continue
        except ValueError:
            print("enter a correct value")
    print(outcome)
# filter_list_of_numbers(my_list)

# EXERCISE 2: Working with Dictionaries
# Using the following dictionary:

employee = { "name": "tim", "age": 30, "birthday": "1990-03-10", "tim" : "DevOps Engineer" }

# Write a Python Script that:

# Updates the job to Software Engineer
# Removes the age key from the dictionary
# Loops through the dictionary and prints the key:value pairs one by one


def edit_stuff(dict1):
    dict1.update({"tim": "Software Engineer"})
    dict1.pop("age")

    thisdict = dict.keys(dict1)
    for l in thisdict:
        print(l+": "+dict1[l])
#edit_stuff(employee)


# Using the following 2 dictionaries:

dict_one = {"a": 100, "b": 400}
dict_two = {"x": 300, "y": 200}

# Write a Python Script that:

# Merges these two Python dictionaries into 1 new dictionary.
# Sums up all the values in the new dictionary and print it out
# Prints the max and minimum values of the dictionary

def merge_and_sum(d1, d2):
    d1.update(d2)
    x=0
    for l in d1.values():
        try:
            int(l)
            x += l
        except ValueError:
            print("enter a correct value")
    print(d1)
    print(x)
    highest = 0  # (so far)
    for l in d1.values():
        try:
            int(l)
            if l > highest:
                highest = l
            else:
                continue
        except ValueError:
            print("enter a correct value")

    print("the highest number is", highest)

    lowest = highest
    for l in d1.values():
        try:
            int(l)
            if l < lowest:
                lowest = l
            else:
                continue
        except ValueError:
            print("enter a correct value")

    print("the lowest number is", lowest)
#merge_and_sum(dict_one, dict_two)

# EXERCISE 3: Working with List of Dictionaries
# Using a list of 2 dictionaries:
#
employees = [{ "name": "Tina", "age": 30, "birthday": "1990-03-10", "job": "DevOps Engineer", "address": { "city": "New York", "country": "USA" } }, { "name": "Tim", "age": 35, "birthday": "1985-02-21", "job": "Developer", "address": { "city": "Sydney", "country": "Australia" } }, { "name": "miro", "age": 22, "birthday": "1990-03-10", "job": "DevOps Engineer", "address": { "city": "New York", "country": "USA" } } ]
# { "name": "Myroslav", "age": 22, "birthday": "2228-03-10", "job": "DevOps", "address": { "city": "Kyiv", "country": "EU" } }
# Write a Python Program that:
#
# Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.
# Prints the country of the second employee in the list by accessing it directly without the loop.

def listofdictionary(list):
    for i in list:
        name = i.get("name")
        job = i.get("job")
        address = i.get("address")
        city = address.get("city")
        print(name+"'s job is", job, "and they live in", city)

    print(list[1]["address"].get("country"))
# listofdictionary(employees)

# EXERCISE 4: Working with Functions
# Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.
# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
# Write a function that prints the even numbers from a provided list.
# For cleaner code, declare these functions in its own helper Module and use them in the main.py fil

def getstufffromdictionary(list):
    the_youngest_employee_list_id = 0
    the_youngest_employee_age = list[0].get("age")
    for i in list:
        if int(i.get("age")) < the_youngest_employee_age:
            the_youngest_employee_age = int(i.get("age"))
            the_youngest_employee_list_id = list.index(i)
        else:
            continue
    print(the_youngest_employee_age)
    print(the_youngest_employee_list_id)
    theYoungestEmployeeName = list[the_youngest_employee_list_id]["name"]
    print("the name of the youngest employee is", theYoungestEmployeeName, "and he is", the_youngest_employee_age, "years old")
# getstufffromdictionary(employees)

# EXERCISE 5: Python Program 'Calculator"
# Write a simple calculator program that:
#
# takes user input of 2 numbers and operation to execute
# handles following operations: plus, minus, multiply, divide
# does proper user validation and give feedback: only numbers allowed
# Keeps the Calculator program running until the user types "exit"
# Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did
# Concept covered: working with different data types, conditionals, type conversion, user input, user input validation


import sys

def checking_numbers(number):
    num = ""
    while True:
        import sys
        num = input(f"enter number{number}: ")
        if num == "exit":
            sys.exit("Thank you for using calculator which was written by Myroslav S on 17.12.2022")
        try:
            int(num)
            if num.isdigit():
                return int(num)
        except ValueError:
            print("I said NUMBER!!!")

def calculate(num1, num2):
    while True:
        action = input(f"enter action: ")
        if action == "exit":
            sys.exit("Thank you for using calculator which was written by Myroslav S on 17.12.2022")
        elif action == "divide":
            return (num1 / num2)
        elif action == "plus":
            return (num1 + num2)
        elif action == "minus":
            return (num1 - num2)
        elif action == "multiply":
            return (num1 * num2)
        else:
            print("You entered a non-existent action. try again!")
            continue

def calculator():
    i = 0
    print("hi")
    while True:
        import os
        print(f"you've made {i} calculations")
        num1 = checking_numbers(" one")
        num2 = checking_numbers(" two")
        print("result: ", calculate(num1, num2))
        i = i + 1
        continue
#calculator()

# EXERCISE 6: Python Program 'Guessing Game"
# Write a program that:
#
# runs until the user guesses a number (hint: while loop)
# generates a random number between 1 and 9 (including 1 and 9)
# asks the user to guess the number
# then prints a message to the user, whether they guessed too low, too high
# if the user guesses the number right, print out YOU WON! and exit the program
# Hint: Use the built-in random module to generate random numbers https://docs.python.org/3.3/library/random.html 1
#
# Concepts covered: Built-In Module, User Input, Comparison Operator, While loop

import random
def guessingame():

    a = (random.randint(1, 9))
    while True:
        b = (checking_numbers(""))
        if int(a) == int(b):
            print("YOU WON")
            break
        elif int(a) < int(b):
            print("too high")
            continue
        elif int(a) > int(b):
            print("too low")
            continue
#guessingame()

# EXERCISE 7: Working with Classes and Objects
# Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:
#
# a) Create a Student class
#
# with properties:
#
# first name
# last name
# age
# lectures he/she attends
# with methods:
#
# can print the full name
# can list the lectures, which the student attends
# can add new lectures to the lectures list (attend a new lecture)
# can remove lectures from the lectures list (leave a lecture)
# b) Create a Professor class
#
# with properties:
#
# first name
# last name
# age
# subjects he/she teaches
# with methods:
#
# can print the full name
# can list the subjects they teach
# can add new subjects to the list
# can remove subjects from the list
# c) Create a Lecture class
#
# with properties:
#
# name
# max number of students
# duration
# list of professors giving this lecture
# with methods:
#
# printing the name and duration of the lecture
# adding professors to the list of professors giving this lecture
# d) Bonus task
#
# As both students and professors have a first name, last name and age, you think of a cleaner solution:
#
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Create a Person class, which is the parent class of Student and Professor classes
# This Person class has the following properties: "first_name", "last_name" and "age"
# and following method: "print_name", which can print the full name
# So you don"t need these properties and method in the other two classes. You can easily inherit these.
# Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class


# EXERCISE 8: Working with Dates
# Write a program that:
#
# accepts user"s birthday as input
# and calculates how many days, hours and minutes are remaining till the birthday
# prints out the result as a message to the user


def birthday_calc():
    from datetime import datetime

    import time
    print("what's your birthday? input: d/m")
    dt1 = "10/20" #input()

    dt2 = datetime.fromtimestamp(time.time()).strftime('%m/%d')
    d1 = datetime.strptime(dt1, "%m/%d")
    d2 = datetime.strptime(dt2, "%m/%d")

    # difference between dates in timedelta
    delta = d2 - d1
    print(time.time().strftime('%m/%d'))
    # print(delta)
    # print(f'Difference is {delta.days} days')
#birthday_calc()
from datetime import datetime

import time
now = datetime.now
print(now)



# EXERCISE 9: Working with Spreadsheets
# Write a program that:

# reads the provided spreadsheet file "employees.xlsx" (see Download section at the bottom) with the following information/columns: "name", "years of experience", "job title", "date of birth"
# creates a new spreadsheet file "employees_sorted.xlsx" with following info/columns: "name", "years of experience", where the years of experience is sorted in descending order: so the employee name with the most experience in years is on top.
# EXERCISE 10: Working with REST APIs
# Write a program that:
#
# connects to GitHub API
# gets the projects for a specific GitHub user
# prints the project names
# employees.xlsx (8.6 КБ)
#
# 14 - Automation with Python
# Exercises for Module "Automation with Python"
# EXERCISE 1: Working with Subnets in AWS
# Get all the subnets in your default region
# Print the subnet Ids
# EXERCISE 2: Working with IAM in AWS
# Get all the IAM users in your AWS account
# For each user, print out the name of the user and when they were last active (hint: Password Last Used attribute)
# Print out the user ID and name of the user who was active the most recently
# EXERCISE 3: Automate Running and Monitoring Application on EC2 instance
# Write Python program which automatically creates EC2 instance, install Docker inside and starts Nginx application as Docker container and starts monitoring the application as a scheduled task. Write the program with the following steps:
#
# Start EC2 instance in default VPC
# Wait until the EC2 server is fully initialized
# Install Docker on the EC2 server
# Start nginx container
# Open port for nginx to be accessible from browser
# Create a scheduled function that sends request to the nginx application and checks the status is OK
# If status is not OK 5 times in a row, it restarts the nginx application
# EXERCISE 4: Working with ECR in AWS
# Get all the repositories in ECR
# Print the name of each repository
# Choose one specific repository and for that repository, list all the image tags inside, sorted by date. Where the most recent image tag is on top
# EXERCISE 5: Python in Jenkins Pipeline
# Create a Jenkins job that fetches all the available images from your application"s ECR repository using Python. It allows the user to select the image from the list through user input and deploys the selected image to the EC2 server using Python.
#
# Instructions:
#
# Start EC2 instance and install Docker on it
# Install Python in Jenkins
# Create 3 Docker images with tags 1.0, 2.0, 3.0 from one of the previous projects
# Create a Jenkins Pipeline with the following steps:
# Fetch all 3 images from the ECR repository (using Python)
# Let the user select the image from the list (hint: https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/ 1)
# SSH into the EC2 server (using Python)
# Run docker login to authenticate with ECR repository (using Python)
# Start the container from the selected image from step 2 on EC2 instance (using Python)
# Validate that the application was successfully started and is accessible by sending a request to the application (using Python)