# Check if a specific element exists in a list
def check_element_in_list(element, my_list):
    if element in my_list:
        return True
    else:
        return False

# Example usage:
my_list = [6,9,4,7,2]
element_to_check = 7
result = check_element_in_list(element_to_check, my_list)
print("Element exists in the list:", result)
