while True:

    import random

    print("Welcome to the PyPassword Generator!\n")
    letter_count = int(input("How many letters would you like in your password?\n"))
    symbol_count = int(input("How many symbols would you like\n"))
    number_count = int(input("How many numbers?\n"))

    #Password length
    total_count= letter_count + symbol_count + number_count

    #Password components
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
     'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
     'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ["~","!","@","#","$","%","^","&","*","(",")"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]

    password_list = []

    #Randomly select correct number of each component to add to password_list
    for char in range(1,letter_count+1):
        password_list += random.choice(letters)
    for char in range(1,symbol_count+1):
        password_list += random.choice(symbols)
    for char in range(1,number_count+1):
        password_list += random.choice(numbers)

    #Shuffle components
    random.shuffle(password_list)

    #Make the password
    password=""
    for char in password_list:
            password+= char

    #Quality determined by length
    length = len(password)
    if length<8:
        quality="useless."
    elif length==8:
        quality="weak."
    elif length>8 and length<10:
        quality="average."
    else:
        quality="strong."


    print(f"\nYour password is : {password}\n")
    print(f"\nThis password is {length} characters long which makes it {quality}\n")


    #Prompt to repeat
    repeat = input("Another one? Y/N > ")
    while repeat not in ("Y","N"):
        repeat = input("Another one? Y/N > ")
    if repeat == "N":
        break
