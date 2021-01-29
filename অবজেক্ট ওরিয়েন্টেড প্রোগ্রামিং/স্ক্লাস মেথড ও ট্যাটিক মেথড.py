

# classmethod

# class Persion:
#     sentance = 'Bangladesh is a beautiful country'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_name(self):
#         return f'My name is {self.name}'
#     @classmethod
#     def class_ethod(cls, country):
#         return f'My country name is {country}'
#     @classmethod
#     def sentance_cls(cls):
#         # return Persion.sentance
#         return cls.sentance
#
# persion1 = Persion('Ziaur Rahman Joy', 20)
# print(persion1.class_ethod('Bangladesh'))
# print(persion1.sentance_cls())



# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def call_area(self):
#         return self.height * self.width
#
#     @classmethod
#     def square(cls, no):
#         return cls(no, no)

# a = Rectangle(4,5)
# print(a.call_area())
# print(a.square('Hello'))
# b = Rectangle.square(5)
# print(b.call_area())


# staticmethod

# class Persion:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def sen(sentance):
#         return sentance
#
# p1 = Persion('Joy', 20)
# print(p1.sen('I love Bangladesh'))


# class Persion:
#     @staticmethod
#     def sen(sentance):
#         return sentance
# p1 = Persion()
# print(p1.sen('I love Bangladesh'))


# from datetime import datetime
#
# class Persion:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_persion(self):
#         return self.name, self.age
#
#     @classmethod
#     def brithday(cls, name, year):
#         return cls(name, datetime.today().year - year)
#
#     @staticmethod
#     def check_method(age):
#         if age > 18:
#             return 'yes you are yong'
#         else:
#             return 'you are child'
#
# p1 = Persion('Ziaur', 20)
# print(p1.print_persion())
# p2 = Persion.brithday('Joy', 2000)
# print(p2.print_persion(), p2.check_method(p2.age))


# property

# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @property
#     def pineapple_allowed(self):
#         return False

# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)




# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#
#     @staticmethod
#     def validate_topping(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             return True
#
# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)

