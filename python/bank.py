import random



'''random_n= random.randint(1,50)
tries = 5
while tries != 0:
    
        print('Welcome to our random number guessing game')
        number= int(input("Guess a number between one and 50: "))
        tries -=1
        
       
        if number < random_n:
            print("the number you guessed is less than the actual number try again")
            print(f"you have {tries} tries left")
        elif number > random_n:
            print('the number you guessed is greater than the actual number try again')
            print(f"you have {tries} tries left")
        else:
            print("Correct!!.You Win")
            break
'''


names = ['steve','ema','carlos']

print(random.choice(names))
print(random.choices(names,k=2))

codes=['axa','abb','cca']
for i in range(len(codes)):
    random.seed(12)
    finalnumber = random.randint(1,100)
    print(codes[i]+str(finalnumber))
(random.seed(10))
print(random.randint(1,100))





#R
#W
#A

with open('fff.txt',"r") as file:
    f = file.readlines()[2]
    print(f)


with open('another_file.txt','w')as file:
    file.write(f)


with open('another_file1.txt','a')as file:
    file.write(f)