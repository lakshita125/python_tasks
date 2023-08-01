# Write a program , which return the key for a given value
def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None


my_dict = {'sharma': 10, 'sinha': 5, 'soni':3}

# Value to find the corresponding key for
target_value = 5
result_key = find_key_by_value(my_dict, target_value)

print(f"Key for the value {target_value}: {result_key}")
