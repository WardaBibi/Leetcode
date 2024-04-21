def transformArray(numbers):
    newArr=[]
    n=len(numbers)
    for i in range(n//2):
        newArr.append(numbers[i])
        newArr.append(numbers[n-i-1])
    if n%2==1:
        newArr.append(numbers[n//2])
    return newArr
    
print(transformArray([1,2,3,4]))
print(transformArray([1,2,3,4,5]))
