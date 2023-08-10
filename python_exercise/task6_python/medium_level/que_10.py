'''Write a Python program that executes an operation on a list and handles an
IndexError exception if the index is out of range.'''
def perform_operation_on_list(my_list, index):
    try:
        result = my_list[index]  
        print("Element at index", index, ":", result)
    except IndexError:
        print("Error: Index is out of range.")


my_list = [1, 2, 3, 4, 5]
index = 10


perform_operation_on_list(my_list, index)
