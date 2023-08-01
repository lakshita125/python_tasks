'''Write a program for rearrange the sequence of elements based on length of character in value '''
def sort_by_value_length(input_list):
    return sorted(input_list, key=lambda x: len(x))

# Example list
my_list = ['apple', 'banana', 'cherry', 'orange', 'grapes']


sorted_list = sort_by_value_length(my_list)
print("Rearranged list based on the length of characters in values:", sorted_list)

