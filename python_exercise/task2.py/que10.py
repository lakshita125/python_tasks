def printLongestIncSubArr( arr, n) :
 
   
    m = 1
    l = 1
    maxIndex = 0
      
   
    for i in range(1, n) :
 
       
        if (arr[i] > arr[i-1]) :
            l =l + 1
        else :
            
            if (m < l)  :
                m = l 
                maxIndex = i - m
            l = 1   
    if (m < l) :
        m = l
        maxIndex = n - m
    for i in range(maxIndex, (m+maxIndex)) :
        print(arr[i] , end=" ")
         

arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
n = len(arr)
printLongestIncSubArr(arr, n)
     