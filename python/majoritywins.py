#User function Template for python3
from collections import Counter
class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, x, y):
        countElement=Counter(arr)
        xcount=countElement[x]
        ycount=countElement[y]
        if xcount > ycount or (xcount == ycount and x < y):
           return x
        else:
            return y
        
        
                
            
 
obj=Solution()
arr=[1,2,3,4,3,2,3,3,4,21,4,2]
print(obj.majorityWins(arr,2,3))
    
