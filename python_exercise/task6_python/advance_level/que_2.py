# Write a program to count the the lines in a file “demo.txt” 
def count_lines(file_path):
    with open(file_path, 'r') as file:
        num_lines = sum(1 for line in file)
    return num_lines

file_path = 'D:\\python exercise\\task6_python\\medium_level\\advance_level\doc.txt'
num_lines = count_lines(file_path)
print(f"Number of lines in the file: {num_lines}")

