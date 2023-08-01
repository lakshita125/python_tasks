list1 = [10, 20, 20, 4, 85, 45, 45, 199, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])