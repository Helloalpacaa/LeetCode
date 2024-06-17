class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        ans = 0
        i = 0
        
        for j in range(len(s)):
            # put s[j] into counter
            # if s[j] is already in counter, it won't affect k
            # if s[j] is not in counter, we are putting a new value into counter, k--
            if s[j] not in counter:
                k -= 1
            counter[s[j]] += 1
            
            # k < 0 说明counter里的elements已经超过了k，需要从i开始移除
            while k < 0:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    #这里一定要删掉，不然之后再次遇到同一个character，会认为它还在window里，window里只存放当前valid的window的characters
                    del counter[s[i]] 
                    k += 1
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans
            