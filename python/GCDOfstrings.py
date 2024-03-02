#method1
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         longest=''
#         if len(str1) > len(str2):
#             maxString=str1
#             minString=str2
#         else:
#             maxString=str2
#             minString=str1

#         for k in range(1,len(minString)+1):
#             substr=minString[0:k]
#             if len(maxString) == (maxString.count(substr) * len(substr)) and len(minString)==minString.count(substr)* len(substr) and len(substr) > len(longest):
#                 longest=substr

#         return longest
        
#method2
class Solution:
    def gcdOfStrings(self,str1:string,str2:string)->string:

        if str1+str2!=str2+str1:
            return ""
            
        from math import gcd

        return str1[:gcd(len(str1),len(str2))]


        
