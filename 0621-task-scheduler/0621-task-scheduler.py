class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        tasks_with_max_freq = sum(freq == max_freq for freq in task_counts.values())
        
        parts = max_freq - 1
        empty_slots = parts * (n - (tasks_with_max_freq - 1))
        available_tasks = len(tasks) - max_freq * tasks_with_max_freq
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles