class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. created a hashmap with key(sorted string): value(List[str])
        hashmap = dict()

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hashmap:
                hashmap[sorted_s] = []
            hashmap[sorted_s].append(s)
        
        ans = []
        for key, value in hashmap.items():
            ans.append(value)
        
        return ans
