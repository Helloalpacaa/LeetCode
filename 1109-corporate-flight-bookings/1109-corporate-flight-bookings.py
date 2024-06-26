class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixSum = [0] * n
        
        for booking in bookings:
            prefixSum[booking[0] - 1] += booking[2]
            if booking[1] < n:
                prefixSum[booking[1]] -= booking[2]
        
        for i in range(1, n):
            prefixSum[i] += prefixSum[i - 1]
        
        return prefixSum
            
        
            