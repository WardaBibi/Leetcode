class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float('inf')
        second=float('inf')

        for n in nums:
            if n<=first:
                first=n
            elif n<=second:
                second=n
            else:
                return True
        return False
    # class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     if len(nums) < 2:
    #         return False

    #     min_arr = []
    #     for num in nums:
    #         if min_arr and num > min_arr[-1]:
    #             min_arr.append(min_arr[-1])
    #         else:
    #             min_arr.append(num)

    #     max_arr = []
    #     for num in nums[::-1]:
    #         if max_arr and num < max_arr[-1]:
    #             max_arr.append(max_arr[-1])
    #         else:
    #             max_arr.append(num)
    #     max_arr = max_arr[::-1]

    #     for i in range(1, len(nums) - 1):
    #         if min_arr[i] < nums[i] < max_arr[i]:
    #             return True

    #     return False
    
