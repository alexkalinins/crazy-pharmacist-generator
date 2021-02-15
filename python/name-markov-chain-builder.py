#!/usr/bin/python3

import pickle

CHAIN = 'name-chain.pkl'


def build_chain(file_path: str):
    chain = {
        '_start': {}
    }

    with open(file_path, 'r') as names:
        for name in names:
            word = name.strip() # stripping white space

            word = word+'.' # period is end character

            # adding first character to first characters count
            if word[0] in chain['_start']:
                chain['_start'][word[0]] +=1
            else:
                chain['_start'][word[0]] = 1


            for ix in range(len(word) - 1):
                if word[ix] in chain:
                    # current word IS in chain
                    if word[ix+1] in chain[word[ix]]:
                        # next has been seen before by this word
                        chain[word[ix]][word[ix+1]] += 1
                    else:
                        # next word has NOT been seen by this word
                        chain[word[ix]][word[ix+1]] = 1
                else:
                    # current word IS NOT in chain
                    chain[word[ix]] = {word[ix+1]: 1}

    with open(CHAIN, 'wb') as f:
        pickle.dump(chain, f, pickle.HIGHEST_PROTOCOL)

    return chain


build_chain('../data/names.txt')
