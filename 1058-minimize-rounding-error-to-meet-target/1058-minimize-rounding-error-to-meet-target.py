class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        n = len(prices)
        floats = [float(price) for price in prices]
        min_sum = sum(math.floor(x) for x in floats)
        max_sum = sum(math.ceil(x) for x in floats)

        print(min_sum, max_sum)

        if target < min_sum or target > max_sum:
            return "-1"
        
        # number we need to ceil
        k = target - min_sum

        print(k)

        ceil_diff = []
        for x in floats:
            if x != math.floor(x):
                diff = math.ceil(x) - x
                ceil_diff.append(round(diff, 3))
        
        if len(ceil_diff) < k:
            return "-1"

        ceil_diff.sort()

        print(ceil_diff)

        error = 0
        for i in range(k):
            error += ceil_diff[i]
        
        for i in range(k, len(ceil_diff)):
            error += 1.0 - ceil_diff[i]
        
        return "{:.3f}".format(error)
