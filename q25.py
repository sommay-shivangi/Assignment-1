#ques25 Write a program that copies the contents of one text file to another.
source_file_path="C:/Users/somma/OneDrive/Desktop/ML Internship/Assignment-1/demo.csv"
destination_file_path="C:/Users/somma/OneDrive/Desktop/ML Internship/Assignment-1/cop.csv"
try:
    with open(source_file_path, 'r') as source_file:
        content = source_file.read()        
    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(content)        
    print(f"Contents copied from '{source_file_path}' to '{destination_file_path}' successfully.")
except FileNotFoundError:
    print(f"The file at '{source_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")