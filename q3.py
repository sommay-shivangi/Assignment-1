#ques3 WAP a python program that calculates the factorial of a given number.
num3=int(input("enter a number: "))
fact=1
for i in range (1,num3+1):
    fact*=i
print("factorial is:",fact)