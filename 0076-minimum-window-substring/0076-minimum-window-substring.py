class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        matched = 0
        ans = ""
        left = 0

        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] == 0:
                    matched += 1
            
            while matched == len(counter):
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left: right + 1]
                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]] > 0:
                        matched -= 1
                left += 1
        
        return ans
                
