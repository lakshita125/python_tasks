'''Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5],  k = 6
Sample Output: Pair count: 2
'''
def find_Pair_Count(arr, n, K):         #n=size of arr , 
 
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                count += 1
 
    return count
 
 

arr = [1,2,3,4,5]
n = len(arr)
K = 6
print("Count of pairs is",
      find_Pair_Count(arr, n, K))
