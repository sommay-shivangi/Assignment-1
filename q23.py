#ques23 Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
conv=int(input("please enter 1 for C to F, and 2 for F to C: "))
temp=int(input("please enter the temp to converted: "))
if(conv==1):
    faren=(temp*(9/5))+32
    print(temp,"C in fahrenheit is:", faren,"F")
elif(conv==2):
    cels=(temp-32)*(5/9)
    print(temp,"F in celsius is:", cels,"C")
else:
    print("chose between 1 and 2")