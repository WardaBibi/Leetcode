def longestPattern(strArr):
    lp=''
    
    for i in range(len(strArr)):
        for j in range(i+1,len(strArr)):
            substr=strArr[i:j+1]
            # print(substr)
            if len(substr) > len(strArr[i:])//2:
                break
            else:
                if strArr.count(substr) >=2 and len(substr) > len(lp):
                    lp=substr
    if lp !='':
        return "yes "+lp
    return "No null"
    
    
print(longestPattern("aabejiabkfabed"))
print(longestPattern("da2kr32a2"))
print(longestPattern("sskfssbbb9bbb"))
print(longestPattern("123224"))
print(longestPattern("abbbaac"))
