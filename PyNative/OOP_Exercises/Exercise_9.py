'''
OOP Exercise 9: Check object is a subclass of a particular class
'''
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

if __name__ == '__main__':
    print(issubclass(Dog, Animal))
    print(issubclass(Animal, Dog))
    print(issubclass(Cat, Animal))
    print(issubclass(Puppy, Animal))