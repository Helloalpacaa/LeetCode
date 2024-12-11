class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarrays = 0
        sub_array_sum = sum(arr[:k - 1])

        for i in range(k - 1, len(arr)):
            sub_array_sum += arr[i]

            if i >= k:
                sub_array_sum -= arr[i - k]
            
            if sub_array_sum / k >= threshold:
                subarrays += 1
                print(i, sub_array_sum)
            
            
        
        return subarrays