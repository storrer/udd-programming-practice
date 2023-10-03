# Programming practice problems — Chris Storrer
Please save each solution in its own file, in a practice problems folder.

# Wordplay

A file containing all valid Scrabble words, one word per line:

https://www.dropbox.com/s/qkg62nkh483g635/sowpods.txt?dl=0


**For loops and if conditions**

[x] What are all of the words containing UU?
[x] What are all of the words containing an X and a Y and a Z?
[x] What are all of the words containing a Q but not a U?
[x] What are all of the words that contain the word CAT and are exactly 5 letters long?
[x] What are all of the words that have no E or A and are at least 15 letters long?
[x] What are all of the words that have a B and an X and are less than 5 letters long?
[x] What are all of the words that both start and end with a Y?
[x] What are all of the words with no vowel and not even a Y?
[x] What are all of the words that have all 5 vowels, in any order?
[x] What are all of the words that have all 5 vowels, in alphabetical order?

**Setting up storage to use during a for loop, including counters and arrays**

[x] How many words contain the substring "TYPE”?
[x] Create and print an array containing all of the words that end in "GHTLY"
[x] What is the shortest word that contains all 5 vowels?
[x] What is the longest word that contains no vowels?
[x] Which of the letters Q, X, and Z is the least common?
[x] What is the longest palindrome?
[x] What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?


# Countries

A file containing all of the countries in the United Nations, one country per line:

https://www.dropbox.com/s/k6xcq55tqanbdmz/countries.txt?dl=0


[https://www.dropbox.com/s/k6xcq55tqanbdmz/countries.txt?dl=0](https://www.dropbox.com/s/k6xcq55tqanbdmz/countries.txt?dl=0)

**For loops and if conditions**

[ ] What are all of the countries that have “United” in the name?
[ ] What countries both begin and end with a vowel?
[ ] What country names are > 50% vowels?

**Setting up storage to use during a for loop, including counters and arrays**

[ ] What is the shortest country name? Make sure your solution can handle ties.
[ ] What countries use only one vowel in their name (the vowel can be used multiple times)
    - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.
[ ] There is at least one country name that contains another country name. Find all of these cases.
# Baby Names

A file containing the top 40 baby names for boys in 2020:

https://www.dropbox.com/s/drpcy1yrsq4uadk/baby_names_2020_short.txt?dl=0


A file containing the top 40 baby names for boys in 1880:

https://www.dropbox.com/s/fvdi7jl280lqp8c/baby_names_1880_short.txt?dl=0


**More for loops, if conditions, and storage**

[ ] What is the shortest baby name in the top 40 baby names for 2020?
[ ] What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie.

**Nested for loops**

[ ] There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names.
    [ ] Solve this two ways: first with an array to hold the Scrabble words, and then with a dictionary (or set) to hold the Scrabble words. Use timer functions to measure how long it takes to complete this work under each implementation. Why is the time different?
[ ] What are all of the names that were top 40 baby names in both 1880 and 2020?
# More Wordplay questions

The sections **after** this section (“NBA Finals”, “Top Movies”, “Billboard Top 100”) are focused on using bigger datasets to practice breaking down and solving larger problems, including making choices about what data structures to use, coming up with an algorithm to implement, and writing functions to help organize your implementation.

**Before** you move on to those sections, we recommend confirming that you are comfortable **independently** breaking down, implementing, and debugging the questions below. If you aren’t, work with your mentor on more Wordplay, Countries, and Baby Names-sized questions until you are consistently able to solve them independently.

**Revisiting for loops, if conditions, and using lists as storage**

[ ] What are all of the words that have only “U”s for vowels?
[ ] What are all of the words that have only “E”s for vowels and are at least 15 letters long?
[ ] What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?
[ ] What are all of the words that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.
[ ] What is the longest word that can be made from only the letters in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated. Make sure your solution can handle ties.
[ ] What is the longest word that can be made without the letters in “AEIOSHRTN” (in other words, without the most common letters)? Make sure your solution can handle ties.
[ ] Let’s assign letters the following points:
    - W = 12
    - Z = 15
    - E = -17
    - All other letters = 1

What are all of the words with at least 50 points?

**Functions**

[ ] Write a function that takes a string `substring` as an argument and returns an array of all of the words that contain that substring (the substring can appear anywhere in the word).
[ ] Write a function that takes a string `prefix` as an argument and returns an array of all of the words that start with that prefix (the prefix has to be at the beginning of the word).
[ ] Write a function that takes a string `prefix` as the first argument, a string `suffix` as the second argument, and an integer `length` as the third argument. It should return an array of all of the words that start with that prefix, end with that suffix, and are that length.
[ ] Write a function that takes a string `word` as an argument and returns a count of all of the “A”s in that string.
[ ] Write a function that takes a string `word` as the first argument, a string `letter` as the second argument, and returns a count of how many times `letter` occurs in `word`.
[ ] Write a function that takes a string `phrase` and returns a dictionary containing counts of how many times every character appears in `phrase`.
# NBA Finals

A CSV containing NBA finals data for every year:

https://www.dropbox.com/s/8dx99bjfwh9eh38/nba_finals.csv?dl=0


[https://www.dropbox.com/s/8dx99bjfwh9eh38/nba_finals.csv?dl=0](https://www.dropbox.com/s/8dx99bjfwh9eh38/nba_finals.csv?dl=0)

**Dictionaries**

Read the NBA finals CSV data into one more more data structures as needed to complete the following:


[ ] Write a function that takes as an argument a year and returns the winner of the NBA finals that year.
[ ] Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.
[ ] Which teams have made it to the NBA finals but have never won?
[ ] Print out a ranking of who has won the MVP more than once, by times won, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>
# Top Movies

Data on the top 1000 grossing movies:

https://www.dropbox.com/s/qfx0dx0ijzrey5t/top_movies.csv?dl=0


[https://www.dropbox.com/s/qfx0dx0ijzrey5t/top_movies.csv?dl=0](https://www.dropbox.com/s/qfx0dx0ijzrey5t/top_movies.csv?dl=0)

This is a CSV that we recommend parsing with a CSV parsing library (versus parsing it yourself).

**Questions**

[ ] What movies on this list were distributed by DreamWorks?
[ ] What is the highest grossing movie from Universal Pictures, domestically?
[ ] What distributor has the most films on this list?                                                                             
[ ] What is the earliest year on this list, and what were the films from that year?
[ ] What is the distribution of ratings? (How many are PG, PG-13, R, etc.?)  


# Billboard Hot 100 of 2000

A CSV containing the Billboard Hot 100 data for every week of 2000:

https://www.dropbox.com/s/v56vasmua65qjgy/billboard100_2000.csv?dl=0


[https://www.dropbox.com/s/v56vasmua65qjgy/billboard100_2000.csv?dl=0](https://www.dropbox.com/s/v56vasmua65qjgy/billboard100_2000.csv?dl=0)


[ ] Print out all of the #1 songs and the artists who made them. If a song was #1 for more than one week, only print it once. Example output:
    These were the number one songs of 2000:
    "Try Again" - Aaliyah
    "Say My Name" - Destiny's Child
    "What A Girl Wants" - Christina Aguilera
    "Maria Maria" - Santana Featuring The Product G&B
    "Smooth" - Santana Featuring Rob Thomas
    "Independent Women Part I" - Destiny's Child

…

[ ] What song was the #1 song for the most weeks of 2000, who was the artist, and how many weeks was it at #1?
[ ] What artist had the most songs chart in 2000, and what were those songs?
[ ] What song(s) were on the charts (anywhere on the charts) for the most weeks of 2000?
# Bigger Wordplay Questions

The questions **after** this section are all real 60-minute interview questions from tech companies. **Before** you move on to those questions, we recommend confirming that you are comfortable **independently** breaking down, implementing, and debugging the questions below.

If you aren’t, work with your mentor on more similarly-sized questions until you are consistently able to solve them independently, before moving on.


[ ] What is the longest word where no letter is used more than once?
[ ] What are all of the words that are at least 8 letters long and use 3 or fewer different letters? For example, “REFERRER” is an answer to this question, because it uses only 3 different letters: R, E, and F.
[ ] What are all of the words that have at least 3 different double letters? For example, “BOOKKEEPER” is an answer to this question because it has a double-O, a double-K, and a double-E.
[ ] Write a function that takes a string `availableLetters` as an argument and returns an array of all of the words that can be made from only those letters. Letters can be re-used as many times as needed and can appear in any order. Not all of the letters in `availableLetters` have to be used.
[ ] What are all of the compound words? These are words made up of 2 smaller words. For example, “SNOWMAN” is a compound word made from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from “BEACH” and “BALL”.
[ ] Finding alphabet chains:
    - First, what are all of the words that have a least one “A”, one “B”, one “C”, one “D”, one “E”, and one “F” in them, in any order?
        - For example, “FEEDBACK” is an answer to this question
    - Next, is “ABCDEF” the longest alphabet chain that can be found in a word, or is there a longer chain starting somewhere else in the alphabet? Find the longest chain and the words that can be made from that chain.
# Monster Maker

This is an exercise in class and API design. For this exercise, please use [this](https://www.dropbox.com/s/esl8kzhycwfwelp/animals.txt?dl=0) CSV file containing information on various animals.

## Setup
- An `Animal` has the following properties:
    - Name
    - Number of legs
    - Sound that it makes
- A `Monster` is created from two different `Animals` with the same number of legs: one for the head and one for the body.
- A `Monster` has the following properties:
    - Name (the combination of the names of the head and body)
    - Number of legs
    - `Animal` head
    - `Animal` body
    - Sound that it makes (the combination of the sounds of its `Animal` head and body)
## Tasks

We are going to design some classes and functions to create and interact with `Monster`s. The below descriptions are using generic pseudocode — the class and function signatures will look different in the specific programming language you are using.

The class and function definitions below are not fully specified — you will need to make some decisions about how they should work to be useful to someone who would use your code in their own projects.

Please implement the following:

- An `Animal` class
    - Example constructor call: `Animal(name: "Octopus", numLegs: 8, sound: "Burble")`
- A `Monster` class, that creates a `Monster` from an `Animal` head and an `Animal` body
    - Example constructor call: `Monster(head: Animal(Octopus), body: Animal(Scorpion))`
        - `Monster.name` → `OctopusScorpion`
        - `Monster.sound` → `BurbleHiss` 
    - Your code should ensure that we can only create a `Monster` with the head and body of two *different* `Animals`, who have the *same* number of legs.
- A function `createAllMonsters` that takes as input a number of legs and returns an array of all `Monsters` that can be made with that number of legs. A `Monster` with `Animal` A head and `Animal` B body is distinct from a `Monster` with `Animal` B head and `Animal` A body. Please use the *animals.txt* file linked at the beginning of this problem.
    - Example function call: `createAllMonsters(8)` → `[Monster(OctopusScorpion), Monster(ScorpionOctopus)]`
    - The crux of this function is: how do we produce all of the combinations of heads and bodies for animals with a given number of legs?
- A function `getRandomMonster` that takes as input a number of legs and returns a random Monster with that number of legs.
    - Example function call: `getRandomMonster(8)` → `Monster(OctopusScorpion)`
    - This function should call your `createAllMonsters` function
# Mini interview question: `k` largest elements

Goal: solve this problem in < 30 minutes.

Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns the `k` largest values from that array. The order of the elements in the returned array doesn’t matter.

**Example**

- Input array: `[5, 16, 7, 9, -1, 4, 3, 11, 2]`
- `k`: 3
- Result: `[16, 9, 11]`
# Mini interview question: pair sum

Goal: solve this problem in < 30 minutes.

Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns an array with all of the **pairs** of numbers from that array that sum to `k`. You can’t use the same number twice. You can assume that there are no duplicate numbers in the array.

**Example**

- Input array: `[1, 9, 6, 3, 5, 4]`
- `k`: 10
- Result: `[[1, 9], [6, 4]]` // Note that `[5, 5]` is not in the solution
# Interview question: prohibited strings

Goal: solve this problem in < 60 minutes.

Write a function that takes two arguments, a list of prohibited strings and a username, and returns a boolean of whether or not the username contains any of the prohibited strings.

Some important details:

- The list of prohibited words will provide words in some casing, and we want to be **case-insensitive** in our checks. For example, if “darn” is a prohibited word, “darn”, “DARN” and “DaRn” are all prohibited.
- Sometimes people like to make usernames that **substitute numbers for letters**, to try to get around a prohibited word list. We also want to make those substitutions prohibited. The specific letter substitutions we need to check are:
    - A becomes 4
    - E becomes 3
    - I becomes 1
    - O becomes 0
    - For example, if “darn” is a prohibited word, “d4rn” is also a prohibited word. If “darn” and “heck” are prohibited words, the username “D4RN_y0u_T0_h3ck” contains prohibited words.
# Interview question: postfix notation calculator

This is an example 60 minute interview question.

**Setup**

Most of us learn how to do math with operators in between numbers. For example:

`(((4 * 3) + 1) - 2) = 11`

You have an **operator** like `+ - * /`, and numbers (“**operands**”) on each side of the operator, and you apply the operator to those operands. If you have multiple expressions, you resolve them according to some order of operations (or forcing the order using parenthesis). This way of doing math uses **infix notation** — *the operators are in between the operands*.

There’s another way of doing math that uses **postfix notation** — *the operators come after the operands*. This is a cool way of doing math — you don’t need parenthesis or rules to describe the order of operations, so it’s easier to parse a math expression, and you can use a **stack** to manage the calculation (using the stack data structure in the real world!).

Let’s build a basic postfix notation calculator.

**What to implement**

Write a function that takes as an argument a string containing a mathematical expression in postfix notation, using as available operators `+ - * /`. The function should return the result of evaluating that expression.

**Example algorithm**

The postfix notation version of `(((4 * 3) + 1) - 2)` is:

`1 3 4 * + 2 -`

Here’s how the stack evolves while evaluating this expression:

| **Token**                    | **Stack**                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Before processing any tokens | [] // initially empty                                                                                         |
| 1                            | [1] // Push the operand onto the stack                                                                        |
| 3                            | [1, 3] // Push the operand onto the stack                                                                     |
| 4                            | [1, 3, 4]  // Push the operand onto the stack                                                                 |
| *                            | [1, 12] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack |
| +                            | [13] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack    |
| 2                            | [13, 2] // Push the operand onto the stack                                                                    |
| -                            | [11] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack    |

**Example inputs and outputs**

| **Input**       | **Output**                                       |
| --------------- | ------------------------------------------------ |
| “1 3 4 * + 2 -" | 11                                               |
| “3 2 1 + + 2 /” | 3                                                |
| “2 +”           | <raise an error, this is a malformed expression> |

Once you have a working implementation:

- What edge cases would you need to handle to have a robust calculator?
# Interview question: count ships

This is a 60 minute interview question.

Write a function that counts of the number of ships in a 2D grid.

- Input: an array of arrays of strings, representing a 2D grid. The strings are either a `"."` for open water, or an `"S"` for part of a ship. Connected `"S"`es are part of the same ship.
- Output: an integer that is the count of the number of ships in the grid.

Facts about ships:

- Ships are only horizontal or vertical, not diagonal.
- Ships have a width of one or more and a height of one or more.
- Ships never touch each other.

The input will always be a well-formed grid (all rows are the same length).

**Example function calls**


    let ships = [
        [".", "S", ".", "S"],
        [".", ".", ".", "S"],
        ["S", "S", ".", "S"],
        [".", ".", ".", "S"]
    ]
    
    countShips(ships) -> 3


    let ships = [
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", ".", ".", ".", "S", "S"]
    ]
    countShips(ships) -> 3
# Interview question: balanced brackets

This is a classic 60 minute interview question.

Given a string of different bracket types (**parentheses**, **square brackets**, and **curly braces**), write a function that returns whether or not the string is **balanced**.

The string is balanced if each opening bracket is followed by a corresponding close bracket, and all brackets between those open and close brackets are also balanced.

**Examples of balanced strings**

- `{[()]}`
- `{}[]()`
- `[(){()}]`

**Examples of unbalanced strings**

- `{[(])}` // Has a `]` before the `(` was closed with a `)`
- `{}][()` // Has a `]` without a preceding `[`
- `[(){()}` // Missing a closing `]`

**Example function calls**

- `checkBrackets("{[()]}") → True`
- `checkBrackets("{}][()") → False`
# Interview question: Scrabble solver

This was a real interview question at Dropbox. Candidates who passed the interview would typically successfully implement Part 1 and then articulate an algorithm for Part 2 within 60 minutes, but they might not have time to implement Part 2.

## Part 1

Write code that:

- Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
- Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

Example input and output:

`$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
`17 piques`
`17 equips`
`16 quips`
`16 pique`
`16 equip`
`15 quip`
`…`

Resources:

- [Word list](https://www.dropbox.com/s/qkg62nkh483g635/sowpods.txt?dl=0)
- [Letter scores](https://www.dropbox.com/s/talrnaxaftbb1rz/letter_scores.txt?dl=0)

Key points:

- Letters cannot be reused. For example, if your Scrabble rack is “ABCD”, you can make the word “CAB” but not the word “DAD”, because you only have one “D”.
- 
## Part 2

Extend the script to handle blank tiles. When reading the input, the character _ can be used as a wildcard — it can represent any letter.

Wildcards do not count towards a word's score.


# Interview question: rot solver

Part I an example 60 minute interview question. It’s easy to get tripped up on the math — be systematic in your debugging and power through it! Part II is a bonus exercise.

## Part I

(If you’ve heard of a rot13 letter substitution cipher, this question is a generalization of that cipher)

Write a function `rot` that:

- takes as arguments: an input string and an amount by which to shift the letters in the string
- returns: the input string, shifted by the shift amount

The function should preserve case — it should be able to handle both upper and lowercase letters — and it should not alter punctuation. The function should support negative numbers. The function should support large shift numbers.

Sample inputs and outputs:


    rot("HELLO", 1) -> "IFMMP" # shift right by 1
    rot("HELLO", 2) -> "JGNNQ" # shift right by 2
    rot("HELLO", -1) -> "GDKKN" # shift left by 1
    rot("HELLO", 27) -> "IFMMP" # shift right by 27, wrapping back to the beginning
    rot("Hello, Rick", 1) -> "Ifmmp, Sjdl" # Preserve case and punctuation
    rot(rot("Hello, Rick", 1), -1) -> "Hello, Rick"

Writing this function will require familiarity with converting between character and ordinals. For example, Python has the `ord` and `chr` functions, and JavaScript has the `charCodeAt` and `fromCharCode` String methods.

You may also find reviewing modular arithmetic (using `%`) to be helpful.

## Part II

Using your `rot` function, write a function `decrypt` that takes a text encrypted using a shift substitution cipher of an unknown shift amount, and returns a tuple containing `(the shift used to encrypt the original string, the original string)`.

You will need a dictionary or word list. An input string needs to be long enough to unambiguously determine the the shift used, or there could be multiple valid shifts.

Sample inputs and outputs:


    decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") -> ("It was the best of times, it was the worst of times", 1)


# Hard interview question: Boggle solver

This is a retired coding question from Dropbox. I don’t know how often candidates would actually solve this completely during a 60-minute interview, so instead I’m going to break this into a couple of pieces with expectations for each.


## Part 1

Implement a recursive depth-first search that you fully understand and could reproduce in front of someone from scratch if you needed to.

Then, run your DFS implementation on some example graphs. This means being comfortable with how to represent a graph with nodes and edges in your preferred interview language.

This will become the foundation for the Boggle solver.


## Part 2

Review how to play Boggle. [Here](https://www.puzzle-words.com/boggle-4x4/) is an example online version.

The goal of the game when played with humans is to find as many words as you can in a grid of 16 letters, in a limited amount of time. Words can only be made from connected letters — i.e. from a given letter you can only use the letters directly adjacent, including diagonally. You can’t reuse letters, and words must be at least 3 letters long.


## Part 3

Implement a Boggle solver. This is the part that you can treat like a time-boxed interview if you’d like. You will likely want to break this into the follow steps:


1. Stub out a function that takes as input a grid (e.g. a 2 x 2 or 4 x 4 matrix of letters) and returns all of the words that can be made from that grid.
2. Write a function to create a graph from the grid. *[Goal: complete this sub-part in 30 minutes]*
    1. Refer back to your graph representations from Part I.
    2. Test that you get the correct graph back from a grid.
3. Set up a data structure containing all words in the dictionary, with efficient lookup. *[Goal: complete this sub-part in < 10 minutes (you probably already have this implemented if you’ve completed the prior problems in this problem set)]*
4. Use depth-first search to find all of the words in the grid. *[Goal: complete this sub-part in 60 minutes]*
    1. You’ll need to run DFS starting from every letter.
    2. You don’t need any fancy data structures to solve a 4x4 grid quickly.
    3. You’ll need a way of confirming if a path through the grid makes a valid word.
    4. You might find it helpful (both as a light efficiency optimization and for easier debugging) to stop pursuing paths in the grid that cannot possibly lead to a valid word, i.e. that path is not a valid prefix for any word in the dictionary.


## Example inputs and outputs

**Example 1**
Grid:

    BE
    TQ

Valid words: {'BET'}

**Example 2**
Grid:

    ZQQZ
    ZAEZ
    ZUDZ
    ZQQZ

Valid words: {'ZUZ', 'ZED', 'ADZ', 'QUAD', 'EAU', 'DAE', 'DUE', 'ZEA', 'QUA', 'ADZE', 'AUE', 'ZZZ'}

**Example 3**
Grid:

    MSEF
    RATD
    LONE
    KAFB

Valid words: {'FONDEST', 'TOR', 'RANTED', 'OAF', 'FETES’ … 486 words in all}

# Hard interview question: Word Pattern

This is a retired 60-minute coding question from Dropbox. A good goal would be to be able to finish Part 1 within the 60 minutes, and then to come up with a plan for Part 2 even if you don’t have time to implement it fully.

## Part 1

Write a function that takes as arguments two strings: `pattern` and `input`. Return whether or not the words in `input` match the pattern of the characters in `pattern`.

Example 1:

| `pattern: 'abba'`            |
| ---------------------------- |
| `input: 'red blue blue red'` |
| `result: True`               |

Example 2:

| `pattern: 'abcabc'`                      |
| ---------------------------------------- |
| `Input: 'red blue green red blue green'` |
| `result: True`                           |

Example 3:

| `pattern: 'abba'`             |
| ----------------------------- |
| `Input: 'red blue green red'` |
| `result: False`               |



## Part 2

Write a function that takes as arguments two strings: `pattern` and `input`. Return whether or not `input` can be broken into words to match the pattern of the characters in `pattern`.

(In other words, this is the same problem as part 1, but `input` doesn’t contain spaces, so you’ll need to determine if it is possible to split up the input into words in a way that matches `pattern`. You will likely want to use recursion.)

Example 1:

| `pattern: 'abcba'`             |
| ------------------------------ |
| `input: 'redbluegreenbluered'` |
| `result: True`                 |

Example 2:

| `pattern: 'aba'`                                                               |
| ------------------------------------------------------------------------------ |
| `Input: 'xxyyyxx'`                                                             |
| `result: True`, with multiple solutions:<br><br>- x, xyyyx, x<br>- xx, yyy, xx |

Example 3:

| `pattern: 'abba'`          |
| -------------------------- |
| `Input: 'redbluegreenred'` |
| `result: False`            |

# Behavioral interview questions

