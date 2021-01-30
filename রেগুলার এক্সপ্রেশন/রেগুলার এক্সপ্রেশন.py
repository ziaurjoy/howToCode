

import re


# pattern = 'Bangla'
# pattern = r'India'
# result = re.match(pattern, 'Bangladesh')
# if result:
#     print('hello Banlgadesh')
# else:
#     print('Sorry dos not match')



# pattern = 'Bangla'
# # pattern = r'India'
# result = re.match(pattern, 'India Bangladesh')
# if result:
#     print('hello Banlgadesh')
# else:
#     print('Sorry dos not match')



# word = r'Bangla'
# sentance = 'I love Bangla language. and I love Bangladesh'
# result = re.search(word, sentance)
# if result:
#     print('yes searching result is done')
# else:
#     print('Sorry dos not found')

# word = r'Bangla'
# sentance = 'I love Bangla language. and I love Bangladesh'
# result = re.findall(word, sentance)
# print(result)



# word = r'Bangla'
# sentance = 'I love Bangla language. and I love Bangladesh'
# result = re.search(word, sentance)
# print(result.group())
# print(result.start())
# print(result.end())
# print(result.span())


# word = r'gr.y'
# if re.match(word, 'grey'):
#     print('match 1')
# if re.match(word, 'gray'):
#     print('match 2')
# if re.match(word, 'blue'):
#     print('match 3')

# word = r"^Ba.sh$"
#
# if re.match(word, 'Bangladesh'):
#     print('match 1')
# if re.match(word, 'Bansh'):
#     print('match 2')
# if re.match(word, 'Bade'):
#     print('match 3')



vowels = f'[aeiou]'

# if re.search(vowels, 'grey'):
#     print("The word 'grey' got at least one vowel!")
# else:
#     print('No vowels found')

# sentance = input('Enter your sentance : ')
# if re.search(vowels, sentance):
#     print('The word is found')
# else:
#     print('No vowel found')




# pattern = r"[A-Z][A-Z][0-9]"
#
# if re.search(pattern, "NS1 is prefix of first name server address."):
#     print('yeas search result is true')
# else:
#     print('sorry word search not found')


# pattern = r"[A-Z][a-z][0-9]"
#
# if re.search(pattern, "Nf1 is prefix of first name server address."):
#    # Found NS1 as match
#    print("OK")

# pattern = r"[^A-Z]"
# if re.search(pattern, "The name of my country is bangladesh"):
#     print('yes')


# pattern = r'egg(spam)*'
# if re.search(pattern, 'egg'):
#     print('Match 1')
# if re.search(pattern, 'eggspam teeedd'):
#     print('Match 2')



# pattern = r"a(bc)(de)(f(g)h)i"
#
# match = re.match(pattern, "abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.groups())



# pattern = r'(?P<first>abc)(?:def)(ghi)'
# match = re.match(pattern, 'abcdefghi')
# print(match.group('first'))
# print(match.groups())

# pattern = r'gr(a|e)y'
# if re.match(pattern, 'gray'):
#     print('Yes mathc 1')
#
# if re.match(pattern, 'grey'):
#     print('Yes mathc 2')
#
# if re.match(pattern, 'grvy'):
#     print('Yes mathc 3')



