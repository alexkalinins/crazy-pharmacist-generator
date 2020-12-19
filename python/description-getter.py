#!/usr/bin/python3

# fetches and processes wikipedia articles to get brief descriptions

import requests
import re

API_URL = 'https://en.wikipedia.org/w/api.php'

session = requests.Session()


attempts, good = 0, 0 
with open('descriptions.txt', 'a') as desc_file:
    with open('names.txt', 'r') as names_file:    
        for name in names_file:
            title = name.capitalize()
            title = title.strip()

            request_params = {
                'titles': title,
                'action': 'query',
                'origin': '*',
                'format': 'json',
                'prop': 'extracts'
            }
            attempts += 1

            try:
                request = session.get(url=API_URL, params=request_params)
                DATA = request.json()
                data = list(DATA['query']['pages'].values())[0]['extract']

                # first paragraph without bold tags
                par = data[data.index('<p>')+3:]
                par = par[:par.index('</p>')]

                par = par.replace('<b>', '')
                par = par.replace('</b>', '')

                # use sentence e.g. 'used to ...' or 'use in ...'
                desc = par[par.index('use'):]
                desc = desc[:desc.index('.')]

                # removing any parenthesis and their contents
                desc = re.sub(r'\([^)]*\)', '', desc)
                desc = desc.replace('<i>', '')
                desc = desc.replace('</i>', '')
                desc = 'used' + desc[5:] if desc.startswith('used,') else desc

                print(f'{title}: {desc}.')

                desc_file.write(desc + '.\n')
                good += 1
            except Exception as e:
                print(title+': couldn\'t get description.')

print(f'Done! Tried {attempts} names; got {good} descriptions')
