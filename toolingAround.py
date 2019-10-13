# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint, choice

for i in range(100):
    if i % 5 == 0:
        print(i)
        
words = (
        '\nI have a large set of text stored in this wonderfully large'
        ' tuple which is apparently one of the best practiced ways of'
        ' storing lots of text when it should not be stored in a docstring.'
        ' though it does seem to have an issue with the .format().'
        ' I guess we will see in the end how it plays out.'
        ' It is interesting how this is my first foray into Python outside'
        ' of work, and I feel like a beginner outside of work since'
        ' I do not have a particular project or problem to solve.'
        ' I will have to resolve that!'
        )
print(words)


class Human():
    def __init__(self, sex, age, name):
        self.living = True
        self.sex    = sex
        self.age    = age
        self.name   = name
            
    def isLiving(self):
        if self.living:
            self.breathe()
        else:
            print('{0} is not breathing...'.format(self.name))
    
    def breathe(self):
        print('{0} is breathing.'.format(self.name))
        
    def speak(self, words):
        print('{0} says:\n\t{1}'.format(self.name, words))
        
    def die(self):
        self.living = False
        print('{0} has died...'.format(self.name))
        
        
        
def createAHuman():
    people = {
            'Bob':'Male',
            'Mary':'Female',
            'Jim':'Male',
            'Marie':'Female'
            }    
    
    age = random.randint(0, 100)
    person = random.choice(list(people))
    return (people.get(person), age, person)

sex, age, name = createAHuman()