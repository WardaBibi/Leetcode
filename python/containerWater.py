class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=float('-inf')
        left=0
        right=len(height)-1
        while(left<right):
            minheight=(min(height[left],height[right]))
            currentArea=(right-left)*minheight
            if  currentArea > maxArea:
                    maxArea=currentArea
            if minheight==height[left]:
                left+=1
            else:
                right-=1
        return maxArea

        
