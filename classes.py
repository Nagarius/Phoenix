class Dog:
    def __init__(self, color, age, name):
        self.color = color
        self.age = age
        self.name = name
    def getColor(self):
        return ("The colour is " + str(self.color))
    def getAge(self):
        return ("The age is " + str(self.age))
    def getName(self):
        return ("It's name is " + str(self.name))

nameString = input ("So what is this new dog called?: ")
colorString = input ("So what is this new dog's colour?: ")
ageString = input ("So what is this new dog's age?: ")
newDog = Dog(colorString, ageString, nameString)
print (newDog.getName())
print (newDog.getColor())
print (newDog.getAge())
