#ques11 Write a python program that generates the first n numbers in the Fibonacci sequence.
n1=0
n2=1
n=10
print(n1)
print(n2)
for i in range (n-2):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3