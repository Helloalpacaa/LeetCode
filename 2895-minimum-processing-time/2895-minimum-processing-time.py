class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        min_processing_time = 0

        for i in range(0, len(tasks)):
            tasks[i] += processorTime[i // 4]
            min_processing_time = max(min_processing_time, tasks[i])
        
        return min_processing_time