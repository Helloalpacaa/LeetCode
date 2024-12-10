class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # maintain a window with size k, keep sliding it and update the maximum number of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}

        i = 0
        max_vowels = 0
        cur_vowels = 0
        for j in range(len(s)):
            if j - i + 1 > k:
                if s[i] in vowels:
                    cur_vowels -= 1
                i += 1

            if s[j] in vowels:
                cur_vowels += 1

            if j - i + 1 == k:
                max_vowels = max(max_vowels, cur_vowels)
            
            if max_vowels == k:
                return max_vowels
        
        return max_vowels

        # optimization: break the iteration if max_vowels == k