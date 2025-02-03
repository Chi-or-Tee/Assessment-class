names = ['steve','ema','carlos']

people = ['jenni','chi','ayo']

names.extend(people)
print(names)


names = ('ann','john','chris')

print(names)


anita={'name':'ann'}
anita['name']='anita'
print(anita)

anita['age']=23
print(anita)

james={'names':'james','aged':27}

anita.update(james)
print(anita)


anita.pop('names')
print(anita)

anita.popitem()
print(anita)
anita.keys()
anita.values()
anita.items()


set={1,1,2,2,3,3}

set.add(6)
set.remove(2)

print(set)

students={}
"""name=input("Enter your student's name \n")
score=float(input("Enter your student's score \n"))
students[name]=score
print(students.items())
update=input("Would you like to change a student's score, delete a student, or see the average score of students? Enter 'c' for change, 'd' for delete, or 'a' for average score \n")
if update.upper() == "C":
    student_name=input("What's the name of the student? \n")
    if student_name == name:
        new_score=float(input("Enter the new score"))
        score.update(new_score)
        print("Updated " + students.items())
    elif student_name != name:
        print("Student does not exist")
if update.upper()== "D":
    deleted=input("Enter the name of the student you'd like to delete. \n")
    if deleted == name:
        students.pop(name)
        print("Student deleted")
if update.upper()== "A":
    number_of_students =sum(students.values())/ len(students.values())
    
else:
    print("You're all done.")"""



"""students={}
while True:
    update=input("would you like to register a student, change a student's score, delete a student, or see the average score of students?\nEnter:\n'r' to register a student \n'c' for change, \n'd' for delete, or \n'a' for average score. \nEnter 'q' to quit: ")

    if  update == 'r':
        name = input('enter your name: ')
        score = input('enter your score: ')
        if score.isdigit():
            students[name]=float(score)
            print(f"registration succesful: {students}")
        else:
            print('enter a valid score')
    elif update == 'c':
        name = input('enter name: ')
        if name in students.keys():
            score = input('enter the new score: ')
            if score.isdigit():
                students[name]=float(score)
                print(f"Update score succesful: {students}")
        else:
            print("student does not exist ")

    elif update == 'd':
        name = input('enter name: ')
        if name in students.keys():
            students.pop(name)
            print(f"Removed succesfully: {students}")
        else:
            print("student does not exist ")

    elif update == "a":
        number_of_students =float(sum(students.values())/ len(students.values()))
        print(f"Average scores: {number_of_students}")

    elif update == "a":
        print('thank you for using the system')
        break

    else:
        print("enter a valid response")"""
    
"""tom = ('tomatoes', 500)
pep = ('pepper', 500)
veg = ('veg oil', 1000)
oni = ('onions', 1500)
gin = ('ginger', 500)

market_list = [tom, pep, veg, oni, gin]
print(market_list)
market_list.pop(1)
total = 0
print(market_list)
for items in market_list:
    total += items[1]
print(total)"""



def sum(a=12,b=10):
    sum = a + b
    print(sum)

sum()
"""def subtract(a):
   b = sum(7,8)
   value = a-b
   print(value) 
subtract(12)

def div(a):
    b=sum(50)
    prod = b/a"""

add = lambda a,b: a + b

print(add(2,3))


