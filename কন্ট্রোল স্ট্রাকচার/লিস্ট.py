

# create list

# words = ["Hello", "world", "!"]
# print(list_create)



# value access of list

# words = ["Hello", "world", "!"]
# print(words[0])
# print(words[1])
# print(words[2])


# Emty list

# words = []
# print(words)


# all type data access of list

# my_list = ['Bangladesh', 1971, ['Bangladesh', 'India', 'Pakistan']]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])


# string behavior list
# language = 'Python is a beautiful language'
# print(language[3])


# Element access of list

# numbers = [1, 2, 3, 5]
# print(numbers)
# numbers[3] = 4
# print(numbers)

# List + list and multiplacation

# number_one = [1, 2, 3, 4, 5]
# number_two = [6, 7, 8, 9, 10]
# print(number_one + number_two + [11, 12, 13, 14, 15])
# print(number_one * 3)


# Element check in list
# city = ['Dhaka', "Bogra", 'Feni', 'Cumilla']
# print('Dhaka' in city)
# print('Mirpur' in city)
# print('Mirpur' not in city)


# append, insert, index, count, extends, remove, pop, reverse, sort

# city = ['Dhaka', "Bogra", 'Feni', 'Cumilla', 'Feni']
# city.append('Mirpur')
# city.insert(2, 'Sherpur')
# print(city.index('Sherpur'))
# print(city.count('Feni'))
# city2 = ['Sherpur', 'Sonka']
# city.extend(city2)
# city.pop() # last element remove
# city.pop(0) #index element remove
# city.remove('Dhaka') # remove element name
# city.reverse()
# city.sort()

# print(city)





# some_marks = [2, 4, 6, 32, 60, 65, 69, 76, 80, 85, 90]
# print(some_marks[2:7])
# print(some_marks[2:])
# print(some_marks[:7])


# some_marks = [2, 4, 6, 32, 60, 65, 69, 76, 80, 85, 90]
# print(some_marks[::3])
# print(some_marks[2:9:2])

# some_marks = [2, 4, 6, 32, 60, 65, 69, 76, 80, 85, 90]
# print(some_marks[3: -4])
# print(some_marks[-7:-2])

# print(some_marks[::-1])
# print(max(some_marks))
# print(min(some_marks))
# print(sum(some_marks))




# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num_list = [even_num for even_num in num_list if even_num % 2 == 0]
# print(even_num_list)
# even_num_list = [if x % 2 == 0 for x in num_list]
# even_num_list = [x for x in num_list if x % 2 == 0]
# print(even_num_list)


# num_list = [1, 2, 3, 4, 5]

# result = [x**2 for x in num_list]
# print(result)

# name_lower = ['Joy', 'Ziaur', 'Kobir', 'Imam']
# upper_name = [name.upper() for name in name_lower]
# print(upper_name)

# names = "Joy, Ziaur, Kobir, Imam"
# a = [names for name in names.join(' ')]
# print(a)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for i in num_list:
#     if i % 2 == 0:
#         # print(i)
#         new_list.append(i)
# print(new_list)
#
# new_list2 = [new_list for new_list in num_list if new_list % 2 == 0]
# print(new_list2)

# matrix_1d = []
matrix_2d = [[1, 2, 3],
            [4, 5, 6]]

# for i in matrix_2d:
#     matrix_1d.append(i)
# print(matrix_1d)

# matrix_1d = [x for x in matrix_2d]
# print(matrix_1d)

# matrix_1d = [i for x in matrix_2d for i in x]
# print(matrix_1d)

# matrix_1d = [i**2 for x in matrix_2d for i in x]
# print(matrix_1d)

# sentence = 'I am awesome!'
# vowels = 'aeiou'
# new = []
# for i in sentence:
#     if i not in vowels:
#         new.append(i)
# print(new)
# print(''.join(new))

# new_sentance = ''.join([letter for letter in sentence if letter not in vowels])
# print(new_sentance)
