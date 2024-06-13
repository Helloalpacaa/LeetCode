class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0
        while i < len(chars):
            currChar = chars[i]
            count = 0
            while i < len(chars) and chars[i] == currChar:
                i += 1
                count += 1
            
            chars[ans] = currChar
            ans += 1
            
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        
        return ans
            
            