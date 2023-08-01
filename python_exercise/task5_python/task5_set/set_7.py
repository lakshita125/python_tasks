'''' Write a function to perform set division (A/B) where A and B are sets ,
 and the result is a set of tuples (a,b) for each a in A and b in B , 
 where a is divisible by b in '''
def set_division(A, B):
    result = set()
    for a in A:
        for b in B:
            if a % b == 0:
                result.add((a, b))
    return result

# Example sets
A = {10, 15, 20, 25}
B = {2, 5}

# Perform set division
result_set = set_division(A, B)

print("Set Division (A/B):", result_set)