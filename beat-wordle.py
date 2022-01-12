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
    return list(sys.argv[1].upper())

def getIncludedLettersAsList():
    if len(sys.argv) > 2 :
        return list(sys.argv[2].upper())
    return []

def getExcludedLettersAsList():
    if len(sys.argv) > 3 :
        return list(sys.argv[3].upper())
    return []

def getWordleCandidates(wordle_list, known_wordle, included_letters, excluded_letters):
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
    excluded_letters = getExcludedLettersAsList()
    wordle_candidates = getWordleCandidates(wordle_list, known_wordle, included_letters, excluded_letters)
    printResults(wordle_candidates)

if __name__ == "__main__":
    main()
