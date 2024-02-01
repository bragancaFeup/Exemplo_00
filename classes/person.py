# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2022)
#objective: class Person
"""""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Person(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # Attribute names list, identifier attribute must be the first one
    att = ['_code','_name','_dob','_salary']
    # auto_number = 1      # Uncomment in case of auto number on
    # Constructor: Called when an object is instantiated
    def __init__(self, code, name, dob, salary):
        super().__init__()
        # Object attributes
        self._code = str(code)
        self._name = name
        self._dob = datetime.date.fromisoformat(dob)
        self._salary = float(salary)
        # Add the new object to the dictionary of objects
        Person.obj[code] = self
        # Add the code to the list of object codes
        Person.lst.append(code)

    # code property getter method
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def dob(self):
        return self._dob
    # dob property setter method
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    # salary property getter method
    @property
    def salary(self):
        return self._salary
    # salary property setter method
    @salary.setter
    def salary(self, salary):
        perc = (salary - self.salary) / self.salary
        if perc < 0 or perc > 0.2:
            print("Salary cannot be reduced or increased by more than 20%")
        else:
            self._salary = salary
    # age property getter method
    @property
    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age

