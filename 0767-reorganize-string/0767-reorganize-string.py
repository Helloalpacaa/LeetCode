class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        max_freq = 0
        max_freq_char = s[0]

        for char in s:
            freq[ord(char) - ord('a')] += 1
            if freq[ord(char) - ord('a')] > max_freq:
                max_freq = freq[ord(char) - ord('a')]
                max_freq_char = char
        
        if max_freq > (len(s) + 1) // 2:
            return ""

        ans = [""] * len(s)
        i = 0
        while max_freq > 0:
            ans[i] = max_freq_char
            i += 2
            max_freq -= 1
        
        freq[ord(max_freq_char) - ord('a')] = 0
        i = 1
        for j in range(26):
            while freq[j] > 0:
                ans[i] = chr(j + ord('a'))
                freq[j] -= 1
                i += 2
        
        return "".join(ans)



