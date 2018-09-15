# Python Program for recursive binary search.
 
# Returns index of x in arr if present, else -1
def binarySearch (arr, x, l=0, r=None):
    if not r:
        r = len(arr)-1

    # Check base case
    if r >= l:
 
        mid = int((l+r)/2)
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, x, l, mid-1)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, x, mid+1, r)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binarySearch(arr, x)
 
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")


# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns -1
def binarySearch(arr, x, l=0, r=None):
    if not r:
        r = len(arr) - 1

    while l <= r:
 
        mid = int((l+r)/2)
         
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif x > arr[mid]:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binarySearch(arr, x)
 
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")