class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # adj = defaultdict(list)
        MOD = 10**9 + 7

        # for i in range(0, len(nums1) - 1):
        #     adj[nums1[i]].append(nums1[i + 1])
        
        # for i in range(0, len(nums2) - 1):
        #     adj[nums2[i]].append(nums2[i + 1])
        
        # # print(adj)
        
        # max_sum = 0
        
        # def backtracking(num: int, path: List[int]) -> None:
        #     nonlocal max_sum

        #     if not adj[num]:
        #         max_sum = max(max_sum, sum(path)) % MOD
        #         return
            
        #     for adjacent in adj[num]:
        #         backtracking(adjacent, path + [adjacent])

        # backtracking(nums1[0], [nums1[0]])
        # backtracking(nums2[0], [nums2[0]])

        # return max_sum % MOD

        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        sum1, sum2 = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                current_max = max(sum1, sum2) + nums1[i]
                sum1, sum2 = current_max, current_max
                i += 1
                j += 1
        
        while i < m:
            sum1 += nums1[i]
            i += 1

        while j < n:
            sum2 += nums2[j]
            j += 1
        
        return max(sum1, sum2) % MOD

            
