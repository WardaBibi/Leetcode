class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        # maxLength=1
        # for i in range(len(s)-1):
        #     flag=0
        #     for j in range(i+2,len(s)+1):
        #         substr=s[i:j]
        #         print(substr)
        #         empty=set()
        #         for k in substr:
        #             if k in empty:
        #                 flag=1  
        #                 break
        #             else:
        #                 empty.add(k)
        #         length=len(empty)
        #         print(length)
        #         if maxLength < length:
        #             maxLength=length
        #         if flag==1:
        #             break
        # return maxLength
        maxLength=0
        left=0
        unique=set()
        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            length=len(s[left:right])+1
            if maxLength < length:
                maxLength=length
        return maxLength

            
        
            


        
