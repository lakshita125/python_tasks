# Create a set of all possible subsets from a given set
import itertools  
# Define the set  
s = {1, 2, 3, 4}  
k = 2  
  
# Find all subsets of size k  
subsets_of_set = list(itertools.combinations(s, k))  
# Print the subsets  
print(subsets_of_set)  