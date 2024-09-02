#!/usr/bin/env python3


class Person:
    """Class for defining the Person attributes"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print("Your name is", self.name, "and you are ", self.age, "Years old and of " , self.gender, "gender")
        

newPerson = Person("Brian", 24, "Male")

newPerson.print_details()
