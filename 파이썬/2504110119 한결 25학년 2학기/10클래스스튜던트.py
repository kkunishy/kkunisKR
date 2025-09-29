class Student:
    def __init__(self, name, math, computer):
        self.__name = name
        self.__math = math
        self.__computer = computer

    def get_name(self):
        return self.__name
    def get_average(self):
        return (self.__math + self.__computer) / 2
    def get_math(self):
        return self.__math
    def get_computer(self):
        return self.__computer

s1=Student('hanbit',95,89)


hfh