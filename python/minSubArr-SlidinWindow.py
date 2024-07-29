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




