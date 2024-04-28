class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = float("-inf")
        vowels = set("aeiou")
        start = 0
        numVowels = 0

        for end in range(0, len(s)):
            if s[end] in vowels:
                numVowels+=1
            if end-start+1 == k:
                max_vowels = max(max_vowels, numVowels)
                if s[start] in vowels:
                    numVowels-=1
                start+=1

        return max_vowels





        