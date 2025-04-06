class Solution:
    def reorganizeString(self, s: str) -> str:
        # find the most freq character and its freq
        most_freq_char = ""
        max_freq = 0
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
            if freq[char] > max_freq:
                max_freq = freq[char]
                most_freq_char = char
        
        n = len(s)

        if max_freq * 2 > n + 1:
            return ""

        ans = [""] * n
        i = 0
        while max_freq > 0:
            ans[i] = most_freq_char
            i += 2
            max_freq -= 1
        
        del freq[most_freq_char]
        for char in freq:
            while freq[char]:
                if i >= n:
                    i = 1
                ans[i] = char
                freq[char] -= 1
                i += 2
        
        return "".join(ans)
        
