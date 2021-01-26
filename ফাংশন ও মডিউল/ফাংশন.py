

# function declaration
# def function_name():
#     print('Hello Function')
#
# function_name()
#
# function_name()
# function_name()


# function parameter

# def hello(x):
#     return x
# print(hello('I love bangladesh'))
# print(hello('I love Dhaka'))

# def hello(x, y):
#     return x+y
# print(hello(10,10))
# print(hello(10,15))


# multiple parameters * tuple values

# def function_name(*multiple_parameter):
#     a = list(multiple_parameter)
#     return a
# print(function_name(1,2,3,4,5))

# def function_name(*multiple_parameter):
#     sum = 0
#     for i in multiple_parameter:
#         sum += i
#     return sum
# print(function_name(1,2,3,4,5))
#
# def function_name2(*multiple_parameter):
#     return sum(multiple_parameter)
#
# print(function_name2(1,2,3,4,5))


# multiple parameters ** dictionary values

# def city_name(**citys):
#     for city in citys:
#         print('{} : {}'.format(city, citys[city]))
#     # return city
# print(city_name(Bangladesh = 'Dhaka', India = 'Delhi', Pakistan = 'Islamabad'))

# def city_name(**citys):
#     all_city = {city: citys[city] for city in citys}
#     return all_city
# print(city_name(Bangladesh = 'Dhaka', India = 'Delhi', Pakistan = 'Islamabad'))

# def print_dict(**kwargs):
#     for args in kwargs:
#         print("{0} : {1}".format(args, kwargs[args]))
# print_dict(a=1, b=2, c=3)



# def function_name(single, *multiple, **dictionary):
#     single = single
#     multiple = multiple
#     dictionary = dictionary
#     print(single, multiple, dictionary)
# function_name('Joy', 'kobir', 'Imam', 'Rahi',Bangladesh = 'Dhaka', India = 'Delhi', Pakistan = 'Islamabad')



# def get_larger(a, b):
#     if a > b:
#         return 'a is large', a
#     else:
#         return 'b is large', b
#
# get_number = get_larger(30, 20)
# print(get_number)


# doc string

# def greet(word):
#     """
#     Print a word with an
#     exclamation mark following it.
#     """
#     print(word + "!")
# print(greet.__doc__)


# def function_name(sentance):
#     return sentance
# print(function_name('I love Bangladesh'))
#
# sentance2 = function_name  // function refarance or assignment
# print(sentance2('I love Dhaka'))


# def name_print(word):
#     return word
#
# def make_function(fun, word):
#     return fun(word)
#
# print(make_function(name_print,'Bangladesh'))



# def add_five(x):
#     return x + 5
#
# def make_twice(func, arg):
#     return func(func(arg))
#
# print(make_twice(add_five, 10))
#
#
# def make_twice(func, arg):
#     return func(func(arg))
# print(make_twice(add_five, 10))




# def squred(x):
#     return x * x
#
# def higher_order_function(func, number):
#     return func(number)
#
# print(higher_order_function(squred, 5))

# def add(x):
#     return x + 5
#
# def higher_order_function(fun, number):
#     return fun(fun(number))
#
#


# f = lambda x, y: x + y
# a = lambda x: x
# print(f(10, 20))
# print(f(20, 40))
# print(a(10))
# print(a(20))

# lam = lambda x: x + 5
# def heigher_order_function(fun, num):
#     return fun(fun(num))
# print(heigher_order_function(lam, 10))

# def heigher_order_function(fun, num):
#     return fun(fun(num))
# print(heigher_order_function(lambda x: x + 5, 10))
# print(heigher_order_function(lambda x: x * 5, 10))


# def squre_function(x):
#     return x * 2
# my_number = [10, 20, 30, 40,]
# result = map(squre_function, my_number)
# print(list(result))
# print(list(result))


# def even(x):
#     return x % 2 == 0
# my_number = [1,2,3,4,5,6,7]
# result = filter(even, my_number)
# print(list(result))

# result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
# print(list(result))
#
# result1 = map(lambda x: x*2, [1, 2, 3, 4, 5, 6, 7])
# print(list(result1))


