def MergeSort(arr):

    # Deviding into subArray

    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[mid:]
        right_arr = arr[:mid]
        MergeSort(left_arr)
        MergeSort(right_arr)

        i = 0
        j = 0 
        k = 0

        # Merging sub-Array
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
                k = k+1
            else:
                arr[k] = right_arr[j] 
                j = j+1  
                k = k+1  
        
        # checking any subArray Left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1    


arr = [5,7,1,5,0,8]

MergeSort(arr)
print(arr)