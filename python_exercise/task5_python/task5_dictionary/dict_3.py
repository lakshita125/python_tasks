# Write a python program to get keys with maximum and minimum value in a Dictionary
def get_key_with_max_value(dictionary):
    if not dictionary:
        return None

    max_key = max(dictionary, key=dictionary.get)
    return max_key

def get_key_with_min_value(dictionary):
    if not dictionary:
        return None

    min_key = min(dictionary, key=dictionary.get)
    return min_key

# Example dictionary
my_dict = {'laksh': 21, 'harsh': 20, 'nav': 22, 'atul': 23}

# Get key with maximum value
max_key = get_key_with_max_value(my_dict)

# Get key with minimum value
min_key = get_key_with_min_value(my_dict)

print("Key with maximum value:", max_key)
print("Key with minimum value:", min_key)
