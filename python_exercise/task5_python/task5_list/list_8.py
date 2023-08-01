''' Write a function that takes a list of integers and returns a new list with each element 
 replaced by the product of all the other elements in the original list, excluding the current element. '''
from functools import reduce

def product_of_other_elements(input_list):
    total_product = reduce(lambda x, y: x * y, input_list)
    return [total_product // num for num in input_list]

# Example usage:
original_list = [1, 2, 3, 4]
new_list = product_of_other_elements(original_list)
print("New list with product of other elements:", new_list)
