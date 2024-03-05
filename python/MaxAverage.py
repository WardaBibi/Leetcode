class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average=sum(nums[0:k])
        maxAvg=average
        for i in range(len(nums)-k):
            average = average - nums[i] + nums[i+k]
            maxAvg=max(average,maxAvg)
        return round(maxAvg/k,6)

            
        
