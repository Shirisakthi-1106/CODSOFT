print("**********************WELCOME TO ROCK PAPERS AND SCISSORS GAME******************************")
 



options=['ROCK','PAPER','SCISSOR']

score_user=0

score_system=0

import random


def system_generate():

    global options
    
    system=random.choice(options)
    return system

def user_generate():
   
   print("PLEASE ENTER ANY ONE AMONG: \n #ROCK \n #SCISSOR \n #PAPER")
   user=input("ENTER YOUR CHOICE")
   if user.upper() in options:
       return user
   else:
       print("INVALID CHOICE..........TRY AGAIN")
       user_generate()
   
def play():

    global score_user,score_system
    user_choice=user_generate()

    system_choice=system_generate()

    if user_choice.upper()=='ROCK':
        if system_choice.upper()=='PAPER':
            score_system+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU LOST!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)
            
        elif system_choice.upper()=='SCISSOR':
            score_user+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU WON!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

        elif system_choice.upper()=='ROCK':
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("IT'S A TIE!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

    elif user_choice.upper()=='PAPER':
        if system_choice.upper()=='PAPER':
            
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("IT'S A TIE!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)
            
        elif system_choice.upper()=='SCISSOR':
            score_system+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU LOST!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

        elif system_choice.upper()=='ROCK':
            score_user+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU WON!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

    elif user_choice.upper()=='SCISSOR':
        if system_choice.upper()=='PAPER':
            score_user+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU WON!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)
            
        elif system_choice.upper()=='SCISSOR':
            
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("IT'S A TIE!!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

        elif system_choice.upper()=='ROCK':
            score_system+=1
            print("THE USER'S CHOICE IS:",user_choice)
            print("THE SYSEM'S CHOICE IS:",system_choice)
            print("YOU LOST!!")
            print("THE USER'SCORE IS:",score_user)
            print("THE SYSTEM'S SCORE IS:",score_system)

    play_again_choice=input("Do you want to play another round(Y/N)")

    if play_again_choice.upper()=='Y':
        play()

    else:

        print("*******************THANK YOU FOR PARTIPATING******************")
        feedback=input("PLEASE ENTER THE FEEDBACK FOR THE GAME:(AVERAGE/GOOD/WORST)")
        exit()
play()


    








   