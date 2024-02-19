class Solution:
    def greatCount(self, N: int, S: str) -> int:
        total = 0
        arr = list(S)
        length = len(arr)
        
        for k in range(1, length + 1):
            for i in range(length - k + 1):
                sub_array = arr[i:i+k]
                count = sum(1 for digit in sub_array if digit == '1')
                if count > len(sub_array) // 2:
                    total += 1
        
        return total

obj = Solution()
print(obj.greatCount(3, "11111"))
