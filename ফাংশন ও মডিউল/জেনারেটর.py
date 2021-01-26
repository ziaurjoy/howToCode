
#
# def gen(x):
#     for i in range(1, x+1):
#         if i % 2 == 0:
#             yield i
#
#
# print(list(gen(10)))
#
#
# def gen2():
#     a = 10
#     for i in range(a):
#         yield i
# for j in gen2():
#     print(j)



# ডেকোরেটর

# def my_function(fun):
#     def function():
#         print('--------------')
#         fun()
#         print('--------------')
#     return function
#
# def print_function():
#     print('Bangladesh')
#
# variable = my_function(print_function())
# print(variable)

# def my_calculation(fun):
#     def result():
#         return fun()
#     return result
#
# def addition():
#     x = 10
#     y = 20
#     # return x+y
#     print(x+y)
# my_calculation(addition())

# def substraction():
#     x = 10
#     y = 20
#     # return x+y
#     print(x-y)
# my_calculation(substraction())



# def my_function(fun):
#     def function():
#         print('--------------')
#         fun()
#         print('--------------')
#     return function
#
#
# @my_function
# def print_decorator():
#     print('Hello Bangladesh')
#
# print_decorator()
#
# @my_function
# def my_name():
#     print('Joy')
#
# my_name()

# def my_calculator(fun):
#     def result():
#         fun()
#     return result
#
# @my_calculator
# def add():
#     x = 20;
#     y = 30
#     print('addition is ', x+y)
# add()
#
# @my_calculator
# def substraction():
#     x = 20
#     y = 15
#     print('Substraction : ', x-y)
# substraction()



# def recursion(x):
#     if x == 1:
#         return 1
#     else:
#         return x * recursion(x-1)
# print(recursion(5))


# num_set = {1, 2, 3, 4, 5}
# word_set = set(["spam", "eggs", "sausage"])
# print(num_set)
# print(word_set)
#
# print(2 in num_set)
# print('spam' in word_set)
#
# blank_set = set()
# print(blank_set)




# num_set = {1, 2, 3, 4, 5, 3, 5}
# print(num_set)
# num_set.add(8)
# num_set.remove(2)
# print(num_set)


# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}
#
# print('Union : ', first | second)
# print('intersection : ', first & second)
# print('difference : ', first - second)
# print('symmetric different : ', first ^ second)


# from itertools import takewhile
#
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums_less_equal_six = takewhile(lambda x: x <= 6, my_numbers)
# filtered_numbers = list(nums_less_equal_six)
# print(filtered_numbers)


from itertools import accumulate, takewhile

# my_list = [1, 2, 3, 4, 5, 6]
# accumulate_befor = accumulate(my_list)
# print(list(accumulate_befor))
#
# my_list = [1, 2, 3, 4, 5, 6]
# takewhile_befor = takewhile(lambda x: x <= 5, my_list)
# print_takewhile = list(takewhile_befor)
# print(print_takewhile)














