#ques22 Write a python program that returns the minimum and maximum values in a list of numbers.
list3=[1,2,3,4,5,6,7,8,9,0,11,34,-1,39]
max=list3[0]
min=list3[0]
for elt in list3:
    if(elt>max):
        max=elt
    if(elt<min):
        min=elt
print("minimum element is:",min,"and maximum element is:",max)