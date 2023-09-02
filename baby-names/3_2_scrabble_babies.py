"""
There is at least one baby name from the top 40 baby names for 2020 that, 
when spelled backwards, is a valid Scrabble word. Find and print all such 
names. Solve this two ways: first with an array to hold the Scrabble words, 
and then with a dictionary (or set) to hold the Scrabble words. Use timer 
functions to measure how long it takes to complete this work under each 
implementation. Why is the time different?
"""
# Dictionary/set implementation
import time
start_time = time.time()

# Open scrabble words
words = set()
with open('C:/Projects/udd-programming-practice/wordplay/sowpods.txt', 'r') as file:
    for word in file.readlines():
        words.add(word.rstrip)


    words = set([word.rstrip() for word in file.readlines()])

scrabble_babies = []

# Open baby names 2020
with open('baby_names_2020_short.txt', 'r') as file:
    for name in file:
        # string[start:stop:step] equivalent [::-1] == [-1::-1]
        name = name.rstrip().upper()[::-1]
        if name in words:
            scrabble_babies.append(name)
        # print(name)

print(*scrabble_babies)

end_time = time.time()

print("The running time is:", end_time - start_time)


"""
Python time module:
The running time is: 0.09116554260253906

Powershell timer:
Seconds           : 1
Milliseconds      : 43
Ticks             : 10435801
TotalDays         : 1.20784733796296E-05
TotalHours        : 0.000289883361111111
TotalMinutes      : 0.0173930016666667
TotalSeconds      : 1.0435801
TotalMilliseconds : 1043.5801
"""