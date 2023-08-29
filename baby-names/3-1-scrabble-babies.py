"""
There is at least one baby name from the top 40 baby names for 2020 that, 
when spelled backwards, is a valid Scrabble word. Find and print all such 
names. Solve this two ways: first with an array to hold the Scrabble words, 
and then with a dictionary (or set) to hold the Scrabble words. Use timer 
functions to measure how long it takes to complete this work under each 
implementation. Why is the time different?
"""

# Open scrabble words
with open('C:/Projects/udd-programming-practice/wordplay/sowpods.txt', 'r') as file:
    words = [word.rstrip() for word in file.readlines()]


# Open baby names 2020
#with open('baby_names_2020_short.txt', 'r') as file: