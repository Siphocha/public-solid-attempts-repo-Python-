#defining what the algorithm function is
def linear_search(arr,p):
#used "i" as a way of expressing the potential integer
    for i in range(len(arr)):
        if arr[i] == p:
            return i
    return p-1
#we returned "p-1" because p is the user integer. So whatever they put minus .
#this gets the index value. (positioning).
arr = ["1","2","3","4", "5", "6", "7", "8", "9", "10"]
p = int(input("What is the number you looking for hime? "))
print("Element was found at the index " +str(linear_search(arr, p)))

