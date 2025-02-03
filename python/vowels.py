
def vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    with open('another_file.txt','r')as file:
        
        for letter in file.read():
            if letter in vowels:
                count += 1
    print(f"The number of vowels in the sentence is {count}")

def length_of_lines():
    with open('another_file.txt','r')as file:
        length = len(file.readlines())
        print(length)

def characters():
    count = 0
    with open('another_file.txt','r')as file:
        for letter in file.read():
                count += 1
    print(f"The number of characters in the sentence is {count}")

def words():
    with open('another_file.txt','r')as file: 
        words = file.read()
        words = words.split()
        word = len(words)
    print(f"The number of words in the sentence is {word}")

def main():
    vowels()
    length_of_lines()
    characters()
    words()

main()

