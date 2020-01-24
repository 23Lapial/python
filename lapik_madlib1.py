#!/usr/bin/env python3

# prompts user with input then labeled to a variable.
name = input('enter a name: ')
place = input('enter a place: ')
adjective_one = input('enter an adjective: ')
adjective_two = input('enter an adjective: ')
food_one = input('enter a food: ')
food_two = input('enter a food: ')
noun = input('enter a noun: ')

# output using f string.
print(f"""{name} was planning a dream vacation to {place}.
{name} was especially looking forward to trying the local
cuisine, including {adjective_one} {food_one} and {food_two}.
 
{name} will have to practice the language {adverb} to
make it easier to {verb} with people.
 
{name} has a long list of sights to see, including the
{noun} museum and the {adjective_two} park.""")
