# -*- coding: utf-8 -*-

class Human():
    def __init__(self, sex, age, name):
        self.living = True
        self.sex    = sex
        self.age    = age
        self.name   = name

    def _breathe(self):
        print('{0} is breathing.'.format(self.name))   

    def die(self):
        if self.living:
            self.living = False
            print('{0} has died at age {1}...'.format(self.getName(), self.getAge()))
        else:
            print('You can only die once...I think?')

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def isLiving(self):
        if self.living:
            self._breathe()
        else:
            print('{0} is not breathing...'.format(self.getName()))

    def speak(self, words):
        if self.living:
            print('{0} says:\n\t"{1}"'.format(self.getName(), words))
        else:
            print('{0} says:\n\t"{1}"\n from beyond the grave...'.format(self.getName(), words))
  
if __name__ == '__main__':
    from random import randint, choice
    
    def createAHuman():
        '''Look at you playing God'''
        people = {
                'Bob':'Male',
                'Mary':'Female',
                'Jim':'Male',
                'Marie':'Female'
                }    
        
        age = randint(0, 100)
        person = choice(list(people))
        return (people.get(person), age, person)

    # Warming up
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

    # Creating a Human
    sex, age, name = createAHuman()
    print((sex, age, name))
    human1 = Human(sex, age, name)

    # Running through life
    human1.isLiving()
    human1.speak('I am alive!')
    print('Some sort of unoriginal misfortune occurred to {0}'.format(human1.getName()))
    human1.die()
    human1.isLiving()
    human1.die()
    human1.speak('I almost made it to retirement...')
