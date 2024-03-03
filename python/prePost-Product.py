class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre=1
        post=1
        n=len(nums)
        result=[1]*n
        for i in range(n):
            result[i]*=pre
            pre*=nums[i]
            result[n-i-1]*=post
            post*=nums[n-i-1]

        return result
        
