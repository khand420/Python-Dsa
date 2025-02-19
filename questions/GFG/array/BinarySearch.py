# pos = -1

def binarySearch(start, end):
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            end = mid-1

        elif arr[mid] < key:
            start = mid+1    
    return -1



key = 45 
arr =  [12, 15, 17, 19, 21, 24, 45, 67]
n = len(arr)

result = (binarySearch(0, n-1))
if result != -1:
    print("Element found at index at: ", result)
else:
    print("Element not fond")



# def Search(arr, key):

#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid =low + (high - low)//2

#         if arr[mid] == key:
#             return mid  
#         elif arr[mid] < key: 
#             low = mid+1
#         else:
#             high = mid-1

#     return -1

# arr =  [12, 15, 17, 19, 21, 24, 45, 67]
# # arr = arr.sort()
# key = 45 

# result = (Search(arr, key))
# if result != -1:
#     print("Element found at index at: ", result)
# else:
#     print("Element not fond")

# from util import time_it

# @time_it
# def linear_search(numbers_list, number_to_find):
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return -1

# @time_it
# def binary_search(numbers_list, number_to_find):
#     left_index = 0
#     right_index = len(numbers_list) - 1
#     mid_index = 0

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_number = numbers_list[mid_index]

#         if mid_number == number_to_find:
#             return mid_index

#         if mid_number < number_to_find:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1

#     return -1

# def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
#     if right_index < left_index:
#         return -1

#     mid_index = (left_index + right_index) // 2
#     if mid_index >= len(numbers_list) or mid_index < 0:
#         return -1

#     mid_number = numbers_list[mid_index]

#     if mid_number == number_to_find:
#         return mid_index

#     if mid_number < number_to_find:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1

#     return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

# if __name__ == '__main__':
#     numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
#     number_to_find = 21

#     index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
#     print(f"Number found at index {index} using binary search")