# Find the maximum difference between any two elements in a  list
def max_difference(my_list):
    if len(my_list) < 2:
        return None

    min_num = max_num = my_list[0]

    for num in my_list[1:]:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    return max_num - min_num

# Example usage:
my_list = [1,4,5,7,9]
result = max_difference(my_list)
print("Maximum difference in the list:", result)




