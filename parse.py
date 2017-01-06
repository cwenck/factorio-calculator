#!/usr/bin/env python3

import os
import sys
import re
import json

def main():
    recipe_path = os.path.expanduser('~/Library/Application Support/factorio/script-output/recipes')
    filelist = os.listdir(recipe_path)

    recipes = {}

    for filename in filelist:
        filepath = os.path.join(recipe_path, filename)
        recipe = parsefile(filepath)
        name = recipe['name']
        del recipe['name']
        recipes[name] = recipe


    json_str = json.dumps(recipes, sort_keys=True, indent=4)
    with open('recipes.json', 'w') as f:
        f.write(json_str)
    print('DONE!')
    print('Generated recipes.json')


def parsefile(path):
    print('Processing File: ' + path)
    with open(path, 'r') as f:
        text = f.read()
        text = re.sub('(\w+) = ', '"\g<1>": ', text)
        text = re.sub('}(,\n\s+"name)', '', text)
        text = re.sub(' --[[table: 0x[0-9a-f]+]]', '', text)

        text = text.replace('\n', '')
        text = text.replace(' ', '')

        text = re.sub('"ingredients":{(.*)},"name"', '"ingredients":[\g<1>],"name"', text)
        text = re.sub('"products":{(.*)}}', '"products":[\g<1>]}', text)

        # category_match = re.match('\s+category\s?=\s?"(\w+)",?')
        # energy_match = re.match('\s+energy\s?=\s?"(\d+)",?')
        # energy_match = re.match('\s+name\s?=\s?"(\d+)",?')

        # text should now be in json format, and thus easier to parse
        # print(text)
        recipe = json.loads(text)
        time = recipe['energy']
        del recipe['energy']
        recipe['time'] = time
        return recipe

if __name__ == '__main__':
    main()