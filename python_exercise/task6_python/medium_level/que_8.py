'''Write a Python function that finds the median of a list of numbers. '''
 
def find_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)

    if n % 2 == 1:
        
        median = sorted_list[n // 2]
    else:
       
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    return median

list = [7, 2, 5, 1, 9, 3]

median = find_median(list)
print("Median:", median)
