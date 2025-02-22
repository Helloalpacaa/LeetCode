class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = defaultdict()
        stack = deque()

        for num in nums2:
            while stack and num > stack[-1]:
                hash_map[stack[-1]] = num
                stack.pop()
            
            stack.append(num)
        
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in hash_map:
                ans[i] = hash_map[nums1[i]]
        
        return ans