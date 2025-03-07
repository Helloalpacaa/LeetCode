class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack and stack[-1] > 0 and asteroid < 0:
                tmp = asteroid
                while stack and abs(tmp) >= stack[-1]:
                    tmp += stack.pop()
            else:
                stack.append(asteroid)
        
        return stack
