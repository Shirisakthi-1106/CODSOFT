print("*********************WELCOME TO PASSWORD GENERATOR*******************")

import string

import random

def generate_password(length,complexity):

    password=''

    if complexity.lower()=='simple':
        all_characters=list(string.ascii_uppercase+string.ascii_lowercase)
        for i in range(length):
            password+=random.choice(all_characters)
        return password
    
    elif complexity.lower()=='moderate':
        all_characters=list(string.ascii_uppercase+string.ascii_lowercase)
        for i in range(length//2+1):
            password+=random.choice(all_characters)
        for i in range(length//2,length):
            password+=random.choice(list(string.digits))
        return password
    
    elif complexity.lower()=='complex':
        all_characters=list(string.ascii_uppercase+string.ascii_lowercase)
        for i in range(length//2+1):
            password+=random.choice(all_characters)

        for i in range(length//2+1,length):
            password+=random.choice(list(string.digits))
            
        password_final = random.choice(list(string.punctuation)).join(list(password))
        return password_final
    
def main():
    length=int(input("ENTER THE LENTGH OF THE PASSWORD:"))

    if not isinstance(length, int):
        raise TypeError("The variable 'length' must be an integer.")
    choice=0
    while choice!=3:
        print("1.SIMPLE \n 2.MODERATE \n 3.COMPLEX")
        choice=int(input("ENTER THE CHOICE FOR COMPLEXITY OF PASSWORD:"))

        if choice==1:

            print("THE GENERATED PASSWORD IS:",generate_password(length,'simple'))
            exit()

        elif choice==2:

            print("THE GENERATED PASSWORD IS:",generate_password(length,'moderate'))
            exit()

        elif choice==3:

            print("THE GENERATED PASSWORD IS:",generate_password(length,'complex'))
            exit()

        else:

            print("ENTER RIGHT CHOICE BETWEEN 1 AND 3")

main()




