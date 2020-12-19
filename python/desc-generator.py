#!/usr/bin/python3

import random
import pickle

def unpickle():
    with open('desc-chain.pkl', 'rb') as f:
        return pickle.load(f)

def next_word(current:str, chain:dict):
    if current.endswith('.'):
        return current
    else:
        total_next_words = sum(chain[current].values())
        rand = random.random() * total_next_words

        for word in chain[current]:
            #picks a random word based on probability of that word appearning next
            rand -= chain[current][word]
            if rand < 0:
                return f'{current} {next_word(word, chain)}'
        
        return current # would never actually run

def generate(count: int):
    chain = unpickle()
    for i in range(count):
        print(next_word('used', chain))

generate(100)
