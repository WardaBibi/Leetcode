class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels="aeiouAEIOU"

        left=0
        right=len(s)-1

        while(left < right):
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        
        return ''.join(s)
        
#method2
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        temp=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])
        temp=temp[::-1]
        k=0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=temp[k]
                k+=1
        return ('').join(s)

        

       
