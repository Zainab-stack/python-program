#create a calculator

num1=int(input("enter your first number:"))
num2=int(input("Enter your second number:"))
opr=str(input("""Choose option,
            A.Addition
            B.Subtraction
            C.Multiplication
            D.Division
            E.Modules"""))
if opr=="A" or opr=="a":
    print("Your answer is =",num1 + num2)
elif opr=="B" or opr=="b":
    print("Your answer is =",num1 - num2)
elif opr=="C" or opr=="c":
    print("Your answer is =",num1 * num2)
elif opr=="D" or opr=="d":
    print("Your answer is =",num1 / num2)
elif opr=="E" or opr=="e":
    print("Your answer is =",num1 % num2)
