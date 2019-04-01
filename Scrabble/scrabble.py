### This is Theodore Fongs Homework #6. It was a nightmare trying to complete this. ###

import sys, argparse
from score_word import score_word

# Exception for bad input
if len(sys.argv) < 2:
    print("Please supply a Scrabble rack between 2-7 letters. Use ? or * for wildcards.")
    exit()

## MAIN CONSTANTS
LETTERS = str(sys.argv[1]).lower() # Convert input into a variable
WILDCARDS = 0
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    DATA = [datum.strip('\n') for datum in raw_input]

## REQUIRED VARIABLES

# Wildcard counter
for i in range(len(LETTERS)):
    if LETTERS[i] == "?" or LETTERS[i] == "*":
        WILDCARDS += 1

#Lists of words without wildcards
letters_no_wildcard = LETTERS.replace("?", "")
letters_no_wildcard = letters_no_wildcard.replace("*", "")

## EXCEPTIONS
try:
    parser = argparse.ArgumentParser(description = "Homework 6 Scrabble Assignment")

    parser.add_argument( "Letters",
        help = "2-7 letters that you have to play if you were playing scrabble")

    args = parser.parse_args()
    args.Letters = args.Letters.lower()

    if len(LETTERS) < 2 or len(LETTERS) > 7:
        raise Exception("You need to input between 2-7 letters.")
        exit()
    elif WILDCARDS > 2:
        raise Exception("You can only have two wildcards.")
        exit()
except Exception as e:
    raise e


## FUNCTIONS
def word_filter(letters):
    """This function will create a list of potential words based upon the input
    length.  The maximum length of inputted words are 2-7 letters.  The list of
    possible sowpods has words that are greater than 7. Therefore, this minimizes the
    list of potential words that the possible permutations of the given letters
    can create by the character length of the word.
    """

    # Initial list
    potential_words = []

    # Filters each word in the dataset to just the length of the word.
    for word in DATA:
        if len(word) <= len(letters):
            potential_words.append(word.lower())
    return potential_words

def word_test(potential_word):
    """This function will check a given word compared to the letters inputted to
    validate if it is a possible word to be created.  If the letters in the word are
    not found in the list of potential letters, the function will check for wildcards.
    If there are inputted wildcards, then the word will pass the test if the number of
    wildcards required is greater than the potential wildcards.
    """

    # Initial variables
    needed_wildcards = 0
    potential_letters = list(letters_no_wildcard)

    # Checks how many wildcards are needed until the # of wildcards exceed the amount
    # of wildcards we have. Otherwise, returns back as True.
    for i in range(len(potential_word)):
        if potential_word[i] not in potential_letters:
            needed_wildcards += 1
            if needed_wildcards > WILDCARDS:
                return False
        else:
            potential_letters.remove(potential_word[i])
    return True

## FINAL PROCESS
def test_to_score():
    """This function compiles all of the defined modules to include the imported
    word_score.py module in order to create a list of words and their respective scores
    into a dictionary.  After it is in a dictionary, it will then sort it by highest score
    and then alphabetical order. Finally, it prints the results with a total score.
    """

    # Initial lists
    list_word = []
    list_score = []

    # Searches every word that is filtered by the word_filter function.
    for word in word_filter(LETTERS):

        # word is passed through the word_test function for validity of True or False.
        if word_test(word):

            # If word passes the test, then add the word and the score of the word to
            # the initial lists.
            list_word.append(word)
            list_score.append(score_word(word, letters_no_wildcard))

    # After the For loop, create a dictionary that zips the two lists together.
    my_dict = dict(zip(list_word, list_score))

    # Sorts the dictionary into a list by highest value and then by alphabetical order.
    final_list = sorted([(v,k) for k, v in my_dict.items()], key = lambda x: (-x[0], x[1]))

    # Prints out each item in the list to reveal possible words/scores.
    for item in final_list:
        print("({}, {})".format(item[0], item[1]))
    total = len(my_dict)
    print("Total number of words: {}".format(total))

# Runs the function.
test_to_score()
