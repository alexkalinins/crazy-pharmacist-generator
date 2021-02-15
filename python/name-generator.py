import random
import pickle
import re

CHAIN = 'name-chain.pkl'

def unpickle():
    with open(CHAIN, 'rb') as f:
        return pickle.load(f)


def isVowel(char: str):
    return char == 'a' or \
            char == 'e' or \
            char == 'o' or \
            char == 'u' or \
            char == 'i' or \
            char == 'y' or \
            char == '' or \
            char == '.'


def isConson(char: str):
    return not isVowel(char)


def next_char(prev: str, current: str, chain: dict):
    if current == '.':
        return ''
    else:
        picked_char = pick_char(chain[current])
        prevTwoVowel = isVowel(prev) and isVowel(current)
        prevTwoConson = not prevTwoVowel

        # making sure there are no more than two conscutive consonants/vowels
        while (prevTwoVowel and isVowel(picked_char)) or (prevTwoConson and isConson(picked_char)):
            picked_char = pick_char(chain[current])

        return current + next_char(current, picked_char, chain)


def pick_char(probs: dict):
    total_next_chars = sum(probs.values())
    rand = random.random() * total_next_chars

    # hopefully shuffeling makes it more random
    for char in random.sample(probs.keys(), k=len(probs)):
        # picks a random word based on probability of that word appearning next
        rand -= probs[char]
        if rand < 0:
            return char

    return 'a'  # would never actually happen


def make_word(chain: dict):
    first_char = pick_char(chain['_start'])
    return next_char('', first_char, chain)


def is_spunky(word: str):
    has_funky_letter = re.match(r'.*[qxzjr]', word)
    return has_funky_letter is not None


def generate(count: int, min_length: int, max_length: int):
    chain = unpickle()

    for i in range(count):
        word = make_word(chain)

        while (len(word) < min_length or len(word) > max_length) or not is_spunky(word):
            word = make_word(chain)

        print(word)




generate(10, 6, 9)
