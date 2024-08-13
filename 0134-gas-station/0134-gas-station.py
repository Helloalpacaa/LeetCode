class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        subtotal, total, start = 0, 0, 0
        for i in range(len(gas)):
            subtotal += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if subtotal < 0:
                start = i + 1
                subtotal = 0
        
        return start if total >= 0 else -1