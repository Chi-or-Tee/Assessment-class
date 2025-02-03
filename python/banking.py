def deposit(bal):
    deposit = int(input("How much do you want to deposit? \n"))
    bal += deposit 
    return bal
def withdrawal(bal):
    withdrawal = int(input("How much do you want to withdraw? \n"))
    if withdrawal > bal:
         print("You do not have sufficient balance to complete this transaction.")
    if withdrawal <= bal:
        bal -= withdrawal
        print(f"Transaction successful. Your new balance is {bal}")

    

def main():
    print("Hello! Welcome to Notes.")
    while True:
        bal = 2000
        activity = input("What do you want to do? Enter 'd' for deposit, 'w' for withdrawal, and 'b' to check your account balance. Enter 'f' when done. \n")
        if activity.upper() == "D":
            new_balance =deposit(bal)
            print(f"Your new balance is {bal}")
        elif activity.upper() == "W":
            withdrawal(bal)
            
        elif activity.upper() == "B":
            print(f"Your account balance is {bal}")
        elif activity.upper() == "F":
            print("Thanks for using Notes.")
            break
        else:
            print("Invalid input. Please try again")

def vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = input("Enter a sentence: ")
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    print(f"The number of vowels in the sentence is {count}")

vowels()