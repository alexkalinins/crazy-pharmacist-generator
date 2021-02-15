#!/usr/bin/python3

import pickle


def build_chain(description_file_path: str):
    chain = {} 

    with open(description_file_path, 'r') as descriptions:
        for line in descriptions:
            words = line.strip().split() # spliting line into words

            for ix in range(0, len(words)-1):
                if words[ix] in chain:
                    # current word IS in chain
                    if words[ix+1] in chain[words[ix]]:
                        # next has been seen before by this word
                        chain[words[ix]][words[ix+1]]+=1
                    else:
                        # next word has NOT been seen by this word
                        chain[words[ix]][words[ix+1]]=1
                else:
                    # current word IS NOT in chain
                    chain[words[ix]] = {words[ix+1]:1}

    with open('chain.pkl', 'wb') as f:
        pickle.dump(chain, f, pickle.HIGHEST_PROTOCOL)

    return chain

build_chain('../data/descriptions.txt')
