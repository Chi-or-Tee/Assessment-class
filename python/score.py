def register():
    name = input('enter your name: ')
    score = input('enter your score: ')
    if score.isdigit():
        students[name]=float(score)
        print(f"registration succesful: {students}")
    else:
        print('enter a valid score')

def change():
    name = input('enter name: ')
    if name in students.keys():
        score = input('enter the new score: ')
        if score.isdigit():
            students[name]=float(score)
            print(f"Update score succesful: {students}")
        else:
            print("student does not exist ")

def delete():
    name = input('enter name: ')
    if name in students.keys():
        students.pop(name)
        print(f"Removed succesfully: {students}")
    else:
        print("student does not exist ")

def average():
    number_of_students =float(sum(students.values())/ len(students.values()))
    print(f"Average scores: {number_of_students}")

students={}
while True:
    update=input("would you like to register a student, change a student's score, delete a student, or see the average score of students?\nEnter:\n'r' to register a student \n'c' for change, \n'd' for delete, or \n'a' for average score. \nEnter 'q' to quit: ")

    if  update == 'r':
        register()
    elif update == 'c':
        change()
    elif update == 'd':
        delete()
    elif update == "a":
        average()
    elif update == "a":
        print('thank you for using the system')
        break

    else:
        print("enter a valid response")