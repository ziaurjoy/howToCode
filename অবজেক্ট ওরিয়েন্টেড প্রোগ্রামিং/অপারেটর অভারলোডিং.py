
# class Mynam:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return (self.value * 2) + (other.value * 2)
# a = Mynam(2)
# b = Mynam(3)
#
# c = a + b
# print(c)



# class MyInt():
#     def __init__(self, value):
#         self.__value = value
#
#     def __int__(self):
#         return self.__value
#
#     def __add__(self, other):
#         return self.__value + int(other) * int(other)
#
#
# a = MyInt(2)
# b = MyInt(3)

# c = a + b
#
# print(c)



# class MyInt:
#     def __init__(self, value):
#         self.__value = value
#
#     def __int__(self):
#         return self.__value
#
#     def __add__(self, other):
#         return self.__value + int(other) * int(other)
#
# a = MyInt(2)
# b = MyInt(3)
# c = a + b
# print(c)
#
#
# class MyInt:
#     def __init__(self, value):
#         self.__value = value
#
#     def __int__(self):
#         return self.__value
#
#     def __sub__(self, other):
#         return self.__value - int(other) * int(other)
#
# a = MyInt(2)
# b = MyInt(3)
# c = a - b
# print(c)


# b = 20
# print(type(b))
# c = 10
# print(type(c))
# d = b.__sub__(c)
# print(d)

class MyInt:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
a = MyInt(2)
b = MyInt(3)
c = a + b
print(c)
