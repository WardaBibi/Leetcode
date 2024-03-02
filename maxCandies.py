class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # result=[]
        # maxCandies=max(candies)
        # for i in candies:
        #     if i+extraCandies >=maxCandies:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

    # another method
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        return [candy+extraCandies >=maxCandies for candy in candies]
        
        
