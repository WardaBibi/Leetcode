class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels='aeiouAEIOU'
        count=maxVowel= sum([1 for i in s[:k] if i in vowels])

        for i in range(len(s)-k):
            count=count-(s[i] in vowels) + (s[i+k] in vowels)
            if maxVowel < count:
                maxVowel=count
        return maxVowel

