# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n=len(nums)
#         i=0
#         j=0
#         while(j<n):
#             # print(f'index is {i} and val is {nums[i]}')
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#                 i=i-1
#             i+=1
#             j+=1
#             # print(nums)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        slow = 0
        fast = 0
        while fast < leng:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,leng):
            nums[i] = 0
        
