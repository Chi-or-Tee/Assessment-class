
print("Hello world!")
#strings are "strings" of characters, like Hello World!. Now we want to learn strings manipulation
#using \n helps you create a new line instead of manually going to a new line to write. Makes your code shorter
print("Hello world!\nI hope you're doing great.")
#Unless you want a space to appear before the next word in the next line, don't add space after the \n
#You can add two strings, such that one comes after the other by using a plus sign. It's called string concatenation
print("Hello" + "Angela")
#The outcome of the code above has no space in between words because there wasn't space before the Angela or after the Hello.
print("Hello" + " Angela")
#Note that in Python program, spaces are important. You might get indentation errors when you add space to your print statement.
#Now we want to try out the input function that prompts users to provide data. We use the "input" function
# input("What is your name?")
#But when the user inputs a response, where does the text go and how can we capture it?
#We can take the output and print it using string concatenation.
# print("Hello " + input("What is your name?"))
# print("Hello " + input("What is your name?\n") + "!")
#You can use ctrl + / to turn a line of code to a comment
#Moving on, we're going to talk about variables. You can assign strings or outputs to variables in order to use it again.
# name = input("What is your name?\n")
#When you assign data to a value, you give the variable a name and use the equal sign to assign it
# print("Hello " + name)
# name = "Jack"
# print(name)
#Next, how to find the length of a string. We use the len() function
# print(len(name))
# name = input("What is your name?\n")
# print(len(name))
#the code can be shorter and written in one line as follows
print(len(input("What is your name?")))
#An easier way for readers to understand is by using variables to separate the steps
# username = input("What is your surname?\n")
# length = len(username)
# print(length)
#It's time for variable naming. You call your variables anything you want but an important rule is to make your code readable
#To separate words in variables, you use underscore. You can't use space. You can have numbers in your variable but not at the beginning.
#Lastly, it's bad practice to use function names like "print" or "input" as variable name.
#If you want to print a variable, you spell it wrong, it won't print.Be consistent






