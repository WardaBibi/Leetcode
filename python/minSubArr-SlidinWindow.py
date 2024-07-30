class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minLength=float('inf')
        # for i in range(len(nums)):
        #    for j in range(i,len(nums)):
        #         subarr=nums[i:j+1]
        #         if sum(subarr) >= target:
        #             minLength = min(minLength,len(subarr))
        #             break

        # if minLength == float('inf'):
        #     return 0
        # else:
        #     return minLength

        l=0
        length=float('inf')
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while  total >= target:
                length=min(length,r-l+1)
                total-=nums[l]
                l+=1
        if length==float('inf'):
            return 0
        else:
            return length           



# ---------------------------------------------------------2nd attempt----------------------------------
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # for i in range(1,len(nums)+1):
        #     for j in range(len(nums)-i+1):
        #         substr=nums[j:j+i]
        #         # print(f' i is {i} and j is {j}')
        #         # print(substr)
        #         if sum(substr) >= target:
        #             return len(substr)
        # return 0        

        l=0
        total=0
        minLength=float('inf')
        for r in range(len(nums)):
            total=total+nums[r]
            # print(f'r is {r} l is {l} and total is {total}')
            while total >= target:
                minLength=min(r-l+1,minLength)
                # print(f'---------------------r is {r} l is {l} and total is {total}')
                total-=nums[l]
                l+=1
        if minLength == float('inf'):
            return 0
        return minLength


