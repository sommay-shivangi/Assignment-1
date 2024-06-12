#ques19 Write a python program that removes all punctuation from a given string.
str8="This, is a punctuated string!"
res=""
for char in str8:
    if char in '.,;:!?':
        continue
    else:
        res+=char
print(res)
