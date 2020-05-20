def binary_search(arr, start, end, k):
    if not start < end:
        return -1

    #checking if x would be present in mid
    mid = (start + end)//2
    if arr[mid] < k:
        return binary_search(arr,mid + 1, end,k)
    elif arr[mid] > k:
        return binary_search(arr,start, mid,k)
    else:
        return mid

#The missing referenced variable
arr = ["2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36","38","40","42","44","46","48","50"]
arr = [int(x) for x in arr]
k = int(input("The number to search for: "))

index = binary_search(arr, 0, len(arr), k)
if index < 0:
    print("{} was not found hime.".format(k))
else:
    print("{} bro, I found it at index {}.".format(k, index))

            
    
    