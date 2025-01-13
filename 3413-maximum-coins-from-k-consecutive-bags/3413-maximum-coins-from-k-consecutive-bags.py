class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        i = 0
        # total hold the value end at coins[j][1], start in coins[i]
        total = 0
        # result hold the value start at coins[i][0], end in coins[j]
        result = 0

        for j in range(len(coins)):
            left_j, right_j, value_j = coins[j]
            # Add the current interval's value
            total += (right_j - left_j + 1) * value_j
            
            # Shrink the current window's length by moving i pointer forward
            while coins[j][1] - coins[i][0] + 1 > k:
                excess = coins[j][1] - coins[i][0] + 1 - k

                # Simulate the result by shrink from right
                result = max(result, total - excess * value_j)

                # Shrink from left
                left_i, right_i, value_i = coins[i]
                # if the length of coins[i] > exceed, we can only remove partial of coins[i]
                if right_i - left_i + 1 > excess:
                    total -= excess * value_i
                    coins[i][0] += excess
                # If the length of coins[i] <= exceed, we can just remove the whole coins[i]
                else:
                    total -= (right_i - left_i + 1) * value_i
                    i += 1
            
            result = max(result, total)

        return result