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

# ----------------------------------------------2nd attempt-----------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxLength=0
        # for i in range(len(s)):
        #     flag=False
        #     for j in range(i,len(s)):
        #         substr=s[i:j+1]
        #         unique=set()
        #         for k in range(len(substr)):
        #             if substr[k] in unique:
        #                 flag = True
        #                 break   
        #             unique.add(substr[k])
        #             length=k+1
        #             if maxLength < length:
        #                 maxLength = length
                # print(f'i is {i} , j is {j} , k is {k} and length is {length} and substr is {substr}')
        #         if flag == True:
        #             break
        # return maxLength

        l=0
        unique=set()
        maxLength=0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            if maxLength < r-l+1:
                maxLength= r-l+1 
        return maxLength

                
                    
                    



            
        
            


        
