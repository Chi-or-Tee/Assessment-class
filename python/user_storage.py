def save_to(file,filepath):
    with open(filepath,'a') as fileobj:
        fileobj.write(file)


def read_from(filepath):
    with open(filepath,"r") as fileobj:
        file = fileobj.readlines()
        return file



def full_name ():
    a = input("What's your first name?")
    b = input("What's your last name?")
    #c =a + " " + b+"\n"
    c = f"{a} {b}\n"
    print(c)
    save_to(c,'usernames.txt')

def greet_systemusers():
    users = read_from('usernames.txt')
    for user in users:
        print(f"hello {user}")

#full_name()
greet_systemusers()