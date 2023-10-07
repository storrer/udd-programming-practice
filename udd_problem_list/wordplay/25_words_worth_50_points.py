"""
Let us assign letters the following points:
    - W = 12
    - Z = 15
    - E = -17
    - All other letters = 1

What are all of the words with at least 50 points?
"""


# Could be more testable for 
# Inner function, scores the word, input = word, returns -> bool
from typing import Any



def matches_criteria(word: str):
    # assert len(word)
    assert type(word) == str

    points = {"W": 12, "Z": 15, "E": -17}
    score = 0
    # Loop over each letter
    for letter in word:
        # Accumulate a score based each letters value
        score += points.get(letter, 1)
    #TODO change this from hardcode
    return score >= 50
    #TODO if I could refactor and return the score, I might do that for testing


# Outer function, input = list of words, return -> all words matching criteria
def find_matching_words(words: list[str]):
    # words_worth_at_least_50_points = []
    return True
    # Loop over all the input words
        # stripping whitespace
        # call inner function with this word
            # if it matches, append the word to result
            # else continue
    # Return the words matching this criteria

# open file for reading
    # Pass words to outer function

#if not matches_criteria("WEST"):
#    print("PASS")
assert not matches_criteria("WEST"), "Expected True"

if matches_criteria("WOWZAWOW"):
    print("PASS")

if not matches_criteria("ZZWOW"):
    print("FAIL")
else:
    print("PASS")

matches_criteria(word="WEST")