#ques20 Write a python program that takes a list of numbers and returns their sum.
sum2=0
while(True):
    num5=int(input("enter any number(to pause, enter -1): "))
    if(num5==-1):
        break
    sum2+=num5
print("sum of numbers entered:",sum2)