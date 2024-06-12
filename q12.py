#ques12 Write a python program that calculates the sum of the digits of a given number.
num4=123432
sum=0
while(num4>0):
    sum+=num4%10
    num4//=10
print("sum of digits is:",sum)
