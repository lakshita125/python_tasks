# Find the sum of all numeric elements in a list.
def sum_numeric_elements(my_list):
    total_sum = 0
    for element in my_list:
        if isinstance(element, (int, float)):
            total_sum += element
    return total_sum

# Example usage:
my_list = [5,5,'laksh',1.5 ,'nav',3]
sum = sum_numeric_elements(my_list)
print("Sum of numeric elements in the given list:", sum)