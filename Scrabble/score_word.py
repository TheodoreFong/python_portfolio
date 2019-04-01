# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 21:12:38 2019

@author: Theod
"""

def score_word(potential_word, letters_no_wildcard):
    """This function looks at every word in the input and then pulls its score
    from the value listed in the scores dictionary.
    """

    # Initial variables.
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    word_score = 0
    potential_letters = letters_no_wildcard
    potential_letters = list(potential_letters)

    # Assigns a score for each letter in scores variable and then returns the
    # total score for that word.
    for letter in potential_word.lower():
        if letter in potential_letters:
            word_score += scores[letter]
            potential_letters.remove(letter)
    return word_score
