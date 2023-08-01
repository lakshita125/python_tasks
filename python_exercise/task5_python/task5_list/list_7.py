# Calculate the pairwise product of two lists
def pairwise_product(list1, list2):
    
    return [x * y for x in list1 for y in list2]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = pairwise_product(list1, list2)
print("Pairwise product of the two lists:", result)