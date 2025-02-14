class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            left_match = right - 1
            while left_match > left and s[left_match] != s[left]:
                left_match -= 1
            
            right_match = left + 1
            while right_match < right and s[right_match] != s[right]:
                right_match += 1
            
            if right - left_match <= right_match - left:
                for i in range(left_match, right):
                    s[i], s[i + 1] = s[i + 1], s[i]
                    moves += 1
            else:
                for i in range(right_match - 1, left - 1, -1):
                    s[i], s[i + 1] = s[i + 1], s[i]
                    moves += 1
            
            left += 1
            right -= 1
        
        return moves
        

        

                
                