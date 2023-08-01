# Remove the maximum element from a set without using the max() function
laksh1={1,2,3,4}

largest_number = None

for number in laksh1:
    if largest_number is None or largest_number < number:
        largest_number = number

#  get the largest number
print(largest_number)  
