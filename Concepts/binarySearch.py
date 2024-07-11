
def binary_search(arr,key):
    left=0
    right=len(arr)-1
    
    while(left  <= right):
        mid= left + (right-left ) //2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
print(binary_search([1,5,8,90,150,678,945,1000,4560],678))
