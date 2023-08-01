# Find the intersection of two lists without using set operations.
def intersection(list1, list2):
    intersection_result = []
    for element in list1:
        if element in list2 and element not in intersection_result:
            intersection_result.append(element)
    return intersection_result

# Example usage:
list1 = [9,4,3,2,1]
list2 = [3,4,5,1,8]
result =intersection(list1, list2)
print("Intersection of the two lists:", result)
