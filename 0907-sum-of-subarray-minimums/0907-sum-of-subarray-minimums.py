class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        
        # left[i] = number of consecutive elements to the left of (and including) arr[i] that are greater than or equal to arr[i]
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]

            stack.append(i)

        # right[i] = number of consecutive elements to the right of (and including) arr[i] that are greater than arr[i]
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans += (left[i] * right[i] * arr[i]) % MOD
        
        return ans