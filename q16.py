#ques16 Write a program in python that counts the frequency of each character in a string.
str7="useless"
dict1={}
for char in str7:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
print("the frequency of chars are:")
for char,freq in dict1.items():
    print(char,":",freq)
