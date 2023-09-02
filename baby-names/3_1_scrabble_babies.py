"""
There is at least one baby name from the top 40 baby names for 2020 that, 
when spelled backwards, is a valid Scrabble word. Find and print all such 
names. Solve this two ways: first with an array to hold the Scrabble words, 
and then with a dictionary (or set) to hold the Scrabble words. Use timer 
functions to measure how long it takes to complete this work under each 
implementation. Why is the time different?
"""
# Array implementation
import time
start_time = time.time()

# Open scrabble words
with open('C:/Projects/udd-programming-practice/wordplay/sowpods.txt', 'r') as file:
    words = [word.rstrip() for word in file.readlines()]

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
The running time is: 0.19123005867004395

Powershell timer:
Seconds           : 1
Milliseconds      : 88
Ticks             : 10882476
TotalDays         : 1.25954583333333E-05
TotalHours        : 0.000302291
TotalMinutes      : 0.01813746
TotalSeconds      : 1.0882476
TotalMilliseconds : 1088.2476
"""