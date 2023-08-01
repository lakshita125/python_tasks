# Write a program to check , two sets are equal or not
def check_sets_equality(set1, set2):
    if set1 == set2:
        print("The sets are equal.")
    else:
        print("The sets are not equal.")

# Example sets
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 4}

# Check if the sets are equal
check_sets_equality(set1, set2)
check_sets_equality(set1, set3)




