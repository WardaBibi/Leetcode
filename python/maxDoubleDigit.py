def maxDoubleDigit(num):
    maxNum=-1;
    arr=str(num)
    for i in range(len(arr) -1):
        subarr=int(arr[i:i+2])
        if subarr > maxNum:
            maxNum= subarr
            
    return maxNum
    
print(maxDoubleDigit(453857))
print(maxDoubleDigit(363223311))
