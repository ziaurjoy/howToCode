

# exception
# user_number_a = int(input('Enter Number of A : '))
# user_number_b = int(input('Enter Number of B : '))
# result = user_number_a/user_number_b
# print(result)


# try:
#     user_number_a = int(input('Enter Number of A : '))
#     user_number_b = int(input('Enter Number of B : '))
#     result = user_number_a/user_number_b
#     print(result)
# except (ZeroDivisionError, ValueError): # exception handling
#     print('Sorry Input Type Error')


# try:
#     user_number_a = int(input('Enter Number of A : '))
#     user_number_b = int(input('Enter Number of B : '))
#     result = user_number_a/user_number_b
#     print(result)
# except ZeroDivisionError: # exception handling
#     print('Sorry Input Zero has not supported')
# except ValueError:
#     print('Sorry Value Error')


# try:
#     a = 'abc'
#     b = 20
#     result = a/b
#     print(result)
# except:
#     print("sorry you are rong")



# finally
# try:
#     user_number_a = int(input('Enter Number of A : '))
#     user_number_b = int(input('Enter Number of B : '))
#     result = user_number_a/user_number_b
#     print(result)
# except ZeroDivisionError: # exception handling
#     print('Sorry Input Zero has not supported')
# except ValueError:
#     print('Sorry Value Error')
# finally:
#     print("Finally Code execute") # finally is all error execution after run


# try:
#     print('Joy')
#     result = 10/0
#     print(result)
# except:
#     print('Yes')
# finally:
#     print('Finally code done')


# manually custom exception create

# print('Hello Joy')
# raise NameError('Hello Bangladesh')
# raise ValueError('Joy')


# try:
#     user_number_a = int(input('Enter Number of A : '))
#     user_number_b = int(input('Enter Number of B : '))
#     result = user_number_a/user_number_b
#     print(result)
# except ZeroDivisionError: # exception handling
#     print('Sorry Input Zero has not supported')
# except ValueError:
#     print('Sorry Value Error')
#     raise

# print('a')
# assert 11 == 11
# print('b')
# assert 'b' == 'b'
# print('c')
# assert 'c' == 'u', 'c not equal u'
# print('d')

# def KelvinToFahrenheit(Temperature):
#     assert (Temperature >= 0), "Colder than absolute zero!"
#     return (((Temperature-273)*1.8)+32)
#
# print(KelvinToFahrenheit(144))
# print(KelvinToFahrenheit(244))
# print(KelvinToFahrenheit(-5))



