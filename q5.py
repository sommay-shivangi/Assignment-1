#ques5 Write a program that takes a string input from the user and writes it to a text file.
content=input("enter anything: ")
opfile=open('C:/Users/somma/OneDrive/Desktop/ML Internship/Assignment-1/trial.txt','w')
print(content, file=opfile)