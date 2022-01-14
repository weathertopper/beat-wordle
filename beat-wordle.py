import sys
import os
import copy

def readWordList():
    enable_word_list = list(map(str.rstrip, open(os.path.join(os.getcwd(),'enable1.txt'), "r").read().split("\n")))
    return enable_word_list

def buildWordleList():
    word_list = readWordList()
    wordle_list = filter(lambda x: len(x) == 5, word_list)
    return list(wordle_list)

def getKnownWordleAsList():
    known_wordle=[]
    while not known_wordle:
        input_known_wordle = input("Known WORDLE (with - for unknown letters):\n")
        if len(input_known_wordle) != 5:
            print("ERROR: WORDLE must be 5 characters long.")
            continue
        known_wordle=list(input_known_wordle.upper())
    return known_wordle

def getIncludedLettersAsList():
    included_letters=[]
    input_included_letters = input("Included letters (in no particular order):\n")
    if len(input_included_letters) > 0:
        included_letters=list(input_included_letters.upper())
    return included_letters

def getExcludedLettersAsList(known_wordle, included_letters, previous_guesses):
    excluded_letters=[]
    for guess in previous_guesses:
        for char in guess:
            if char not in known_wordle and char not in included_letters:
                excluded_letters.append(char)
    return excluded_letters

def getPreviousGuessesAsListOfLists():
    previous_guesses = []
    while True:
        input_guess = input("Previous guess (press enter to continue):\n")
        if not input_guess:
            break
        if len(input_guess) != 5:
            print("ERROR: WORDLE must be 5 characters long.")
            continue
        guess = list(input_guess.upper())
        previous_guesses.append(guess)
    return previous_guesses

def getWordleCandidates(wordle_list, known_wordle, included_letters, excluded_letters, previous_guesses):
    candidates = []
    for word in wordle_list:
        included_letters_checklist = copy.deepcopy(included_letters)
        legit_word = True
        for i in range(5):
            char = word[i].upper()
            if char in excluded_letters:
                legit_word = False
                break
            if known_wordle[i] != '-' and known_wordle[i] != char:
                legit_word = False
                break
            if char in included_letters_checklist:
                included_letters_checklist.remove(char)
                for previous_guess in previous_guesses:
                    if char == previous_guess[i]: # wrong position
                        legit_word = False
                        break
        if not legit_word or len(included_letters_checklist) > 0:
            continue
        candidates.append(word.upper())
    return candidates


def printResults(wordle_candidates):
    print(' -------------------')
    print('| WORDLE CANDIDATES |')
    print(' -------------------')
    print("\n".join(wordle_candidates))

# DRIVER
def main():

    wordle_list = buildWordleList()
    known_wordle = getKnownWordleAsList()
    included_letters = getIncludedLettersAsList()
    previous_guesses = getPreviousGuessesAsListOfLists()
    excluded_letters = getExcludedLettersAsList(known_wordle, included_letters, previous_guesses)
    wordle_candidates = getWordleCandidates(wordle_list, known_wordle, included_letters, excluded_letters, previous_guesses)
    printResults(wordle_candidates)

if __name__ == "__main__":
    main()
