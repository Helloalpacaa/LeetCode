class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue = deque([startGene])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                s = queue.popleft()

                if s == endGene:
                    return steps

                word = list(s)
                for i, c in enumerate(word):
                    for letter in string.ascii_uppercase:
                        if letter == c:
                            continue
                        word[i] = letter

                        if "".join(word) in bank:
                            queue.append("".join(word))
                            bank.remove("".join(word))
                        
                        word[i] = c
            
            steps += 1
        
        return -1