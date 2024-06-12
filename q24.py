#ques24 Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
op=int(input("enter 1 for +, 2 for -, 3 for *, 4 for /"))
num7=int(input("enter first number: "))
num8=int(input("enter second number: "))
if(op==1):
    print("sum is:",num7+num8)
elif(op==2):
    print("difference is:",num7-num8)
elif(op==3):
    print("multiplication is:",num7*num8)
elif(op==4):
    if(num8==0):
        print("denominator can not be zero")
    else:
        print("division is:",num7/num8)
else:
    print("enter valid number")
