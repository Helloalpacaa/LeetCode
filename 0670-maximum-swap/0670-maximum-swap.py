class Solution:
    def maximumSwap(self, num: int) -> int:
        # 从后往前，找到一个最大的值，再找到这个最大值index之前的比它更小的值（尽量往前）
        digits = [int(x) for x in str(num)]

        largest_seen_idx = len(digits) - 1
        swap_small_idx = 0
        swap_large_idx = 0

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[largest_seen_idx]:
                largest_seen_idx = i
            elif digits[i] < digits[largest_seen_idx]:
                swap_small_idx = i
                swap_large_idx = largest_seen_idx
        
        digits[swap_small_idx], digits[swap_large_idx] = digits[swap_large_idx], digits[swap_small_idx]

        return int("".join([str(x) for x in digits]))




        