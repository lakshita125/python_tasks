'''You are given a set of positive integers . Write a function to find the 
 length of the longest consecutive sequence of numbers that can be 
 formed by arranging the elements in any order. '''     
def longest_consecutive_sequence_length(nums):
    nums_list = sorted(nums)
    max_length = 0
    current_length = 1

    for i in range(1, len(nums_list)):
        if nums_list[i] == nums_list[i - 1] + 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length


num_set = {1,2,5,3,6,7,8,3}
result = longest_consecutive_sequence_length(num_set)
print("Length of the longest consecutive sequence:", result)
 