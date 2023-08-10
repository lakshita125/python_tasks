'''Write a Python program to create a list of given strings individually of the list using Python
map function.
Eg.
Input: 
['Red', 'Blue', 'Black', 'White', 'Pink']
'''
input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
    
individual_lists = list(map(list, input_list))

print(individual_lists)
