# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         count=0
#         index=0
#         while len(nums) > 1:
#             target=k-nums[index]
#             nums=nums[index+1:]
#             if target in nums:
#                 count+=1
#                 nums.pop(nums.index(target))
#         return count

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         left=0
#         right=len(nums)-1
#         count=0
#         while(left < right):
#             if k-nums[left] < nums[right]:
#                 right-=1
#             elif k-nums[left] > nums[right]:
#                 left+=1
#             else:
#                 left+=1
#                 right-=1
#                 count+=1
#         return count

        
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ct = Counter(nums)
        res = 0
        for n in ct:
            tmp = k - n
            if n == tmp:
                res += ct[n] // 2
                continue    
            if n < tmp:
                res += min(ct[n], ct[tmp])
        return res
