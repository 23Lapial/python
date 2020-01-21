#!/usr/bin/env python3

# declaring variables and prompting user with input
name = input('enter a name: ')
noun = input('enter a noun: ')
adj = input('enter an adjective: ')
verb = input('enter a verb: ')
adverb = input('enter an adverb: ')

# using formating strings to help produce an output
print(f'{name} likes to {verb} with a {adj} {noun} at the park, but people say {name} likes to {verb} REALLY {adverb} so this is very important to know.')
