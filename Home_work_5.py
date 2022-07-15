import random

def Task1():
    computer_number = random.randint(1,10)
    user_number = int(input('Try to guess number from 1 to 10"\n'))
    if computer_number == user_number:
        print('You are right!')
    else:
        print(f'You are wrong!\nIt was {computer_number}{". It was close!"*(2>abs(user_number-computer_number))}!')
        # if diference less then 1 print 'It was close'
#Task1()

def Task2():
    user_name = input('Print you name:\n')
    user_age = int(input('Print your age:\n'))
    print(f'Hello {user_name}, on your next birthday you’ll be {user_age+1} years!')
#Task2()

def Task3():
    user_string = input('Print your string:\n')
    string_to_list = []
    i = 0
    while i < len(user_string):
        string_to_list += [user_string[i]]
        i += 1
    i = 0
    while i < 5:
        random.shuffle(string_to_list)
        print(''.join(string_to_list))
        i += 1
#Task3()
