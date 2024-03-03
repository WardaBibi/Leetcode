#ist method 
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s=s.strip().split(' ')
#         print(s)
#         a=[]
#         for i in range(len(s)):
#             if s[i]:
#                 a.insert(0,s[i])
#         return ' '.join(a)


    #second method: 2 ptr     
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s=s.split(' ')
#         s=list(filter(None,s))
#         print(s)
#         left=0
#         right=len(s)-1
#         while(left<right):
#             s[left],s[right]=s[right],s[left]
#             left+=1
#             right-=1
#         return ' '.join(s)

#3rd method->fastest
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=reversed(s)
        return ' '.join(s)
