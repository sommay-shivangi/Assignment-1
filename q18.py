#ques18 Write a python program that checks if two strings are anagrams of each other.
str11="silent"
str12="listen"
if(len(str11)!=len(str12)):
    print("not anagrams")
elif(sorted(str11)!=sorted(str12)):
    print("not anagrams")
else:
    print("strings are Anagrams of each other")
