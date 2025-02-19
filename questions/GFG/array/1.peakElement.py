def peakElement(arr):
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] >= arr[j+1]:
                temp = arr[j]    
                arr[j] = arr[j+1]
                arr[j+1] = temp
        return arr[i]        


arr = [3,4,1,16,5,8,10,0]
n = len(arr)
print(peakElement(arr))



def findPeak(arr, n) :
 
    # first or last element is peak element
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
  
    # check for every other element
    for i in range(1, n - 1) :
  
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
             
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
