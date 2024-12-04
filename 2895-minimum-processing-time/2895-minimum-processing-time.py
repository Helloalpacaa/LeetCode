class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # 1. sort tasks, heavier tasks will be arranged earlier
        tasks.sort(reverse=True)
        processorTime.sort()

        # 2. add processor time to each task
        i = 0
        for i in range(0, len(tasks)):
            tasks[i] += processorTime[i // 4]

        # 3. return the max finishing process time(maximum of the new tasks array)
        return max(tasks)
