'''Create a function that takes a list and returns a new list with unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]'''
def create_unique_list(list):
    unique_list=[]
    unique_list = set(list)
    return unique_list


list = [1,2,2,3,4,4,5,5]
new_list = create_unique_list(list)
print("New list with unique elements:", new_list)
