#!/usr/bin/env python3

# using a dictionary to label the user's input in a variable named madlib.
madlib = {'name':input('enter a name: '),'noun':input('enter a noun: '),'adj':input('enter an adjective: '),'verb':input('enter a verb: '),'adverb':input('enter an adverb: ')}

# output with the madlib values placed in appropriate order.
print('{name} likes to {verb} with a {adj} {noun} at the park, but people say {name} likes to {verb} REALLY {adverb} so this is important to know.'.format(**madlib))
