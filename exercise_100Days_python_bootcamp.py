#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:48:08 2024

@author: sarahmoniri
"""

#Exercise dict


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  grades = student_scores[key]
  if grades < 70:
    student_grades[key] = "Fail"
  elif grades >= 71 and grades < 80:
    student_grades[key] = "Acceptable"
  elif grades >= 81 and grades < 90:
    student_grades[key] = "Exceeds Expectations"
  else:
    student_grades[key] = "Outstanding"
print(student_grades)




#Travel Log #
#TODO

travel_log = {
    "france":{
        "cities_visited" :["lion","nice"]
}}
print(travel_log)



#DICTIONARY

#TODO write the function that will allow new countries to be added to the travel_log
 
travel_log = [
    {"country":"france",
     "visits":12, 
     "cities":["hamburg","frankfurt" ]
    }]
name = input("the name of counry. ")
time_visited= int(input("how many times? "))
cities_visited = input("which cities? ").split(",")

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country ["country"] = name
    new_country ["visits"] = times_visited
    new_country ["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country(name, time_visited, cities_visited)
#print(add_new_country) 
print(travel_log) 



# 
#from replit import clear
#from art import logo


 
bids = {} 
bidding_finished = False

while bidding_finished != False: #or while not bidding_finished 
    name = input("what is your name?")
    bid = int (input(" what is your bid price? $"))
    bids [name]= bid
    should_contiue = input ("are there any other bidders? Type 'yes or no'")
    if should_continue =="no":
        bidding_finished = True
    elif should_continue == "yes":
        print("n")








