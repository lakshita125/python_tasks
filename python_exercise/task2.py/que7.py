#QUE7:Write a Python program to merge two sorted arrays into a single sorted array.
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
test_list1.sort()
test_list2.sort()
test_list1.extend(test_list2)
test_list1.sort()

print ("merged list : "    + str(test_list1))
