class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter()
        max_freq = 0
        tasks_with_max_freq = 0
        for task in tasks:
            count[task] += 1
            if count[task] > max_freq:
                tasks_with_max_freq = 1
                max_freq = count[task]
            elif count[task] == max_freq:
                tasks_with_max_freq += 1
        
        parts = max_freq - 1
        empty_slots = parts * (n - (tasks_with_max_freq - 1))
        available_tasks = len(tasks) - max_freq * tasks_with_max_freq
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles