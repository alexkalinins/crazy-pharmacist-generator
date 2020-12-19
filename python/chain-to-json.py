#! /usr/bin/python3

# file for converting pickled models to json to be used later with javascript

import pickle

# unpicles


def unpickle(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)


# converts nested dictionary to json format string
def make_json(nest) -> str:
    if isinstance(nest, set):
        return '\'\''
    elif not isinstance(nest, dict):
        return f'{nest}'
    else:
        json = '{'
        for key in nest:
            json = f'{json}\'{key}\':{make_json(nest[key])},'
        return json[:-1] + '}'


# saves to file
def to_file(json: str, filename: str):
    with open(filename, 'w') as f:
        f.write(json)


# does the actual converting
def convert(filename: str):
    assert filename.endswith('.pkl')
    chain = unpickle(filename)
    json = make_json(chain)
    json_filename = filename.replace('.pkl', '.json')
    to_file(json, json_filename)


convert('name-chain.pkl')
convert('desc-chain.pkl')
