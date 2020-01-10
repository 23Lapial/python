#!/usr/bin/env python3

#PART A
print("Welcome to information Technology\n\nProgramming and\nWeb Devolopment")
print("")
print(" _       ___________\n| |     / /_  __/   |\n| | /| / / / / / /| |\n| |/ |/ / / / / ___ |\n|__/|__/ /_/ /_/  |_|\n\n\n")


#PART B
print('A lightning flash:\nbetween the forest trees\nhave seen water.\n\t- Shiki')

print('**********\n*        *\n* MR. G  *\n* RM 119 *\n*        *\n**********')

print("\"Computer Science is no more about computers\nthan astronomy is about telescopes\"\n- Edsger W. Dijkstra")

#CHALLENGE
print('\n/|\n[]')


#PART C
user_name = input('what is your name? ')
favorite_animal = input('what is your favorite animal? ')
print('hello, ' + user_name + '. your favorite animal is the ' + favorite_animal + '.')

number = input('\nwhat is your favorite number? ')
print(number*3)

test_score = {'score_one':input('\nEnter 3 test scores! '),'score_two':input('Just 2 more to go! '),'score_three':input('last one! ')}
test_sum = int(test_score['score_one'])+int(test_score['score_two'])+int(test_score['score_three'])
print('\nyour test score average: ' + str(test_sum / 3))

print('\nenter 3 animals')
a = {'a1':input('\n'),'a2':input(),'a3':input()}
print('\n',a['a3'],a['a2'],a['a1'])
