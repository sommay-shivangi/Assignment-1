#ques15 Write a program that reads data from a CSV file and prints it to the console.
import csv
file_path2="C:/Users/somma/OneDrive/Desktop/ML Internship/Assignment-1/demo.csv"
try:
    with open(file_path2, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"The file at '{file_path2}' was not found.")
