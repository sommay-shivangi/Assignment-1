#ques6 Write a program that reads the content of a text file and prints it to the console.
file_path='C:/Users/somma/OneDrive/Desktop/ML Internship/Assignment-1/trial.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")