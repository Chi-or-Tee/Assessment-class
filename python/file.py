#you can read from a file or w
#the argument that the open function takes is the name of the file
#file.readlines gives you an array
#file.readline gives you the first line of the text in the text file
#Another way to read and write files is to use json. It helps us work with dictionary better. the regular python read and write functions only work with strings.

import json

"""artist = ['Marshmellow', 'Khalid', 'coldplay']
with open('music list', 'a') as file:
    file.write(str(artist))

#let's do an example with json
#if you want to save multiple dictionaries, you nest it in a list. 


data = [{"name": "Alice", "age": "25", "city": "Abuja"},
        {"name": "Joe", "age": "26", "city": "Lagos"},
        {"name": "Taiwo", "age": "27", "city": "Osun"}
        ]
with open('data.json','w') as file:
    json_string = json.dumps(data)
    file.write(json_string)

with open('data.json', 'r') as file:
    load_data = json.load(file)
print(load_data)
#if you want to see a value, like the city in the dictionary, you can call the key in the print statement.
print(load_data)

for items in load_data:
    print(items['name'])"""


#error handling using try block
try:
    with open('aaa.py', 'r') as file:
        print(file.read())
except Exception:
    print("Cannot find the file") 

#Here's how we get both the error and the exception
try:
    with open('aaa.py', 'r') as file:
        print(file.read())
except Exception as e:
    print(f"Cannot find the file: {e}")

#use case
try:
    number1 = int(input ("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print(number1 + number2)
except Exception as e:
    print(f"Cannot add numbers: {e}")
else:
    print("Addition Successful.")
finally:
    print("Something else")