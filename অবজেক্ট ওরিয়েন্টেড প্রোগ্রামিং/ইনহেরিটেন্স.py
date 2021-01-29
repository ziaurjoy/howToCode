#
# class Perents:
#     def __init__(self, father_name, father_age):
#         self.father_name = father_name
#         self.father_age = father_age
#     def perent_print(self):
#         return self.father_name, self.father_age
#
#
#
# class Persion(Perents):
#
#     def __init__(self, name, age, country):
#         super().__init__(father_name, father_age)
#         self.name = name
#         self.age = age
#         self.country = country
#
#     def persion_print(self):
#         return self.name, self.age, self.country
#
# persion1 = Persion()
# print(persion1.father_name())


# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("Hi, I am " + self.name)
# class PhysicianRobot(Robot):
#     def say_hi(self):
#         print("Everything will be okay! ")
#         print(self.name + " takes care of you!")
# y = PhysicianRobot("James")
# y.say_hi()

#
# class Parrent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_persion(self):
#         return self.name + ' ', self.age
#
# class Childen(Parrent):
#     def __init__(self, gender, id):
#         # super().__init__()
#         self.gender = gender
#         self.id = id
#         return self.name, ' ', self.age, self.gender, self.id

# chil1 = Childen('Male', 382170)
# print(chil1)


# a = Parrent('Joy', 20)
# print(a.print_persion())



# class Monster:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def attack(self):
#         print('I am attacking...')
#
# class Fogthing(Monster):
#     def make_sound(self):
#         print('Grrrrrrrrrr\n')
#
# class Mournsnake(Monster):
#     def make_sound(self):
#         print('Hiiissssshhhh\n')
#
# fogthing = Fogthing("Fogthing", "Yellow")
# fogthing.attack()
# fogthing.make_sound()
#
# mournsnake = Mournsnake("Mournsnake", "Red")
# mournsnake.name
# mournsnake.make_sound()





# class Parrent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def name(self):
#         print('My name is Joy')
#
# class Persion(Parrent):
#     def __init__(self, gender):
#         self.gender = gender
#
#     def gender(self):
#         print('I am a boy')

# p1 = Persion('Male')
# p1.name()



# method overiding

# class Monster:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def attack(self):
#         print('I am attacking')
#
# class Fogthing(Monster):
#     def attack(self):
#         print('I am killing')
#
#     def make_sound(self):
#         print('grrrrr')
# player1 = Fogthing('Joy', 'red')
# player1.attack()

#
# class A:
#     def where(self):
#         print('I am class of A')
#
# class B:
#     def where(self):
#         print('I am class of B')
#
# class C(A, B):
#     pass

# a = C()
# print(C.mro())
# a.where()




# class A:
#     def hello(self):
#         print('Hello Joy')
#
# class B(A):
#     def hello(self):
#         super().hello()
#         print('Hello Ziaur')
#
# b = B()
# b.hello()


# class A:
#     def spam(self):
#         print("Bangladesh")
#
# class B(A):
#     def spam(self):
#         print('Dhaka')
#         super().spam()
#
# B().spam()








