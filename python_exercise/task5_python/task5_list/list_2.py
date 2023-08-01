# Create a new list with unique elements from an existing list.
def create_unique_list(existing_list):

    unique_list = list(set(existing_list))
    return unique_list

# Example usage:
existing_list = [4,7,7,9,4,5]
new_list = create_unique_list(existing_list)
print("New list with unique elements:", new_list)
