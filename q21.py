#ques21 Write a python program that counts the occurrences of a specific element in a list.
list2=[1,2,3,4,5,3,4,6,4,7]
cnt=0
num6=4
for elt in list2:
    if(elt==num6):
        cnt+=1
print("number of occurences of",num6,"is:",cnt)