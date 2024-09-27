class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        step = 1
        visited = set([beginWord])

        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        if char == word[i]:
                            continue
                        newWord = list(word)
                        newWord[i] = char
                        newWord = "".join(newWord)
                        if newWord == endWord:
                            return step + 1
                        if newWord in wordSet and newWord not in visited:
                            queue.append(newWord)
                            visited.add(newWord)
                        
            step += 1
        
        return 0

