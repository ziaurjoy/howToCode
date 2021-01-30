import json

persion = {
    'name': 'Ziaur Rahman Joy',
    'age': 20,
    'country': 'Bangladesh',
    'is_active': True
}
# print('Python dictionary : ', persion)
# persion_jsion = json.dumps(persion)
# print('convert to json : ', persion_jsion)
#
# json_python = json.loads(persion_jsion)
# print('convert python : ', json_python)


with open('file.csv', 'w') as dic:
    json.dump(persion, dic)

with open('file.csv', 'r') as red:
    convert_python = json.load(red)
    print(convert_python)


