class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == '':
            return True

        index = 0
        # iterate through 's', add pointer to 't'
        for i in t:
            if i == s[index]:
                index += 1
                if index == len(s):
                    return True

        return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         t=list(t)
#         for ch in s:
#             if ch in t:
#                 indexOf=t.index(ch)+1
#                 t=t[indexOf:]
#             else:
#                 return False
        
#         return True
        
