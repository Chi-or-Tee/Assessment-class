from user_storage import save_to,read_from

def services(bal):
    activity = input("What do you want to do? Enter 'd' for deposit, 'w' for withdrawal, and 'b' to check your account balance. Enter 'f' when done. \n")
    if activity == "d":
        deposit = int(input("How much do you want to deposit? \n"))
        bal += deposit 
        print(f"Your new balance is {bal}")

    elif activity.upper() == "W":
        withdrawal = int(input("How much do you want to withdraw? \n"))
        if withdrawal > bal:
            print("You do not have sufficient balance to complete this transaction.")
        if withdrawal <= bal:
            bal -= withdrawal
            print(f"Transaction successful. Your new balance is {bal}")
            
    elif activity.upper() == "B":
        print(f"Your account balance is {bal}")


def register():
    print('To Register\n')
    print('-' *40)
    name = input('enter your user name: ')
    password = input('enter your password: ')
    account_bal= input("how much would you like to open your acct with: ")
    if account_bal.isdigit():
        user_details = f"{name.strip()},{password.strip()},{account_bal.strip()}\n"
        save_to(user_details,'users.txt')
        print('registration succesful')


def Login():

    username = input("enter your user name: ")
    user_password = input("enter your password: ")

    file = read_from('users.txt')
    for users in file:
        user = users.split(',')
        name = user[0]
        password = user[1]
        bal= user[2]
        
        if name == username:
            if password == user_password:
                print("Login succesful")
                services(bal)
            else:
                print("incorrect password")
        


        

def main():
    while True:
        print('welcome to our bank\n')
        print('-' *40)
        activity = input("What do you want to do? Enter 'r' for register, 'L' for Login, and '' to check your account balance. Enter 'f' when done. \n")

        if activity == 'r':
            register()
        elif activity == "L":
            Login()
        elif activity == "f":
            break
        else:
            print('enter a valid option')   
main()