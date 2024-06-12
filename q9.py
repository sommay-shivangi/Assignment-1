#ques9 Write a python program that checks if a substring is present in a given string.
str4="geeksforgeeks"
str5="forg"
idx=str4.index(str5)
if(idx==-1):
    print("not present")
else:
    print("present")
