print("*******************CALCULATOR********************")

def add(n1,n2):#function for addition
    return n1+n2

def subtract(n1,n2):#function for subtraction
    return n1-n2
def multiply(n1,n2):#function for multiplication

    return n1*n2
def divide(n1,n2):#function for division

    return n1/n2


choice=0
while choice!=5:
    print("1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n 5.EXIT")
    choice=int(input("ENTER YOUR CHOICE"))
    if choice==1:#choice for addition
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number "))

        result=add(num1,num2)

        print("THE RESULT OF THE ADDITON IS:",result)
    elif choice==2:#choice for addition
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number "))

        result=subtract(num1,num2)

        print("THE RESULT OF THE SUBTRACTION IS:",result)

    elif choice==3:#choice for multiplication
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number "))

        result=multiply(num1,num2)

        print("THE RESULT OF THE MULTIPLICATION IS:",result)

    elif choice==4:#choice for division
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number "))

        result=divide(num1,num2)

        print("THE RESULT OF THE DIVISION IS:",result)

    elif choice==5:
        print("THANK YOU!!!!!!!!")

    else:

        print("INVALID CHOICE..............CHOOSE A NUMBER BETWEEN 1 AND 5")
    

