class Solution:
    def reorganizeString(self, s: str) -> str:
        if s is None or len(s) == 1:
            return s
        
        # Found the most common character
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        prev_freq, prev_char = 0, ''
        ans = ""
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char
        
        return ans if len(ans) == len(s) else ""


        

