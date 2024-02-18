from typing import List
class Solution:
    def findBots(self,usernames:List[str],n : int)->List[int]:
        result=[]
        for elements in usernames:
            counter=set()
            for i in range (0,len(elements),2):
                if elements[i] not in counter:
                    counter.add(elements[i])
            result.append(self.findPrime(len(counter)))
        return result
        
    def findPrime(self,count:int):
        if count == 2:
            return 1
        if count < 2 or count%2 == 0:
            return 0
        for i in range(3,int(count**0.5)+1,2):
            if count %  i == 0:
                return 0
        return 1
        

obj=Solution()
print(obj.findBots(["abcdef","pqrs","xyzuvabb","aaaaaa","bob","foo"],6))

##The advantage of using the square root method is that we only need to check up to the square root of the number
##because if a number n is divisible by a factor x greater than its square root, it would also be divisible by a 
##factor y which is less than its square root. This reduces the number of iterations needed to determine primality, 
##making the algorithm more efficient, especially for large numbers.
