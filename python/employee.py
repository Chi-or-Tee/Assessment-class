import json

data = [{"name": "Alice", "age": "25", "city": "Abuja"},
        {"name": "Joe", "age": "32", "city": "Lagos"},
        {"name": "Taiwo", "age": "27", "city": "Osun"},
        {"name": "Olu", "age": "31", "city": "Ogun"},
        {"name": "Debby", "age": "28", "city": "Lagos"}
        ]

def save_to(file, filepath):
    with open(filepath,'w') as fileobj:
        json_string = json.dumps(file)
        fileobj.write(json_string)

def register():
    with open('employee_record.json', 'r') as file:
        employee_data = json.load(file)

    reg = input("Hello! Do you want to register a new employee? Enter 'Y' for yes and 'N' for no.")
    if reg == 'Y':
        fname = input('enter your name: ')
        dob = input('enter your age: ')
        residence = input('enter your city: ')
        employee_details = { "name": fname, "age": dob, "city": residence }
        employee_data.append(employee_details)
        save_to(employee_data, 'employee_record.json')
        print("Registration succesful")
    elif reg == 'N':
        print("Great")

def main ():
    register()

    '''with open('employee_record.json', 'w') as file:
        json_string = json.dumps(data)
        file.write(json_string)'''

    with open('employee_record.json', 'r') as file:
        employee_data = json.load(file)
        print(employee_data)

    for employees in employee_data:
        dob = int(employees["age"])
        if dob > 30:
            print (employees['name'])
    
main()