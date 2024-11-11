class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return Counter(s) == Counter(t)

        arr = [0] * 26
        for char in s:
            arr[ord(char) - ord('a')] += 1
        
        for char in t:
            arr[ord(char) - ord('a')] -= 1
        
        return all(count == 0 for count in arr)
