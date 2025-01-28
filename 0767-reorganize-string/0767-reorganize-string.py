class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        max_freq = 0
        char_with_max_freq = s[0]

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] > max_freq:
                max_freq = freq[char]
                char_with_max_freq = char
        
        n = len(s)
        if max_freq > (n + 1) // 2:
            return ""

        ans = [""] * n
        i = 0
        while max_freq > 0:
            ans[i] = char_with_max_freq
            i += 2
            max_freq -= 1
            
        
        del freq[char_with_max_freq]
        for char in freq:
            while freq[char] > 0:
                if i >= n:
                    i = 1
                ans[i] = char
                freq[char] -= 1
                i += 2
                
        return "".join(ans)
                


        