#ques26 Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str10="PreStringSuff"
pre="pre"
suf="Suff"
if str10.startswith(pre):
    print(f"The string starts with the prefix '{pre}'.")
else:
    print(f"The string does not start with the prefix '{pre}'.")
if str10.endswith(suf):
    print(f"The string ends with the suffix '{suf}'.")
else:
    print(f"The string does not end with the suffix '{suf}'.")
