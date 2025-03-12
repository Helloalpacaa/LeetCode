class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        n = len(chars)
        while j < n:
            count = 1
            while j + 1 < n and chars[j + 1] == chars[j]:
                count += 1
                j += 1
            
            chars[i] = chars[j]
            i += 1

            if count > 1:
                digit = str(count)
                for char in digit:
                    chars[i] = char
                    i += 1
            j += 1
        
        return i
