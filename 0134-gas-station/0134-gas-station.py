class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果从start point出发，到i时油不够了，那么不管从start point 到i之间的哪个point出发都是不行的
        # 所以我们重置start point到i + 1
        # 因为同时在tracking total，如果遍历完总体的gas - cost < 0的话说明没有valid的start point
        subtotal, total, start = 0, 0, 0
        for i in range(len(gas)):
            subtotal += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if subtotal < 0:
                start = i + 1
                subtotal = 0
        
        return start if total >= 0 else -1