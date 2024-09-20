class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        visited = set([beginWord])
        step = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                word = list(queue.popleft())
                for i in range(len(word)):
                    letter = word[i]
                    for char in string.ascii_lowercase:
                        if char == letter:
                            continue
                        word[i] = char
                        newWord = "".join(word)
                        if newWord == endWord:
                            return step + 1
                            
                        if newWord in wordSet and newWord not in visited:
                            queue.append(newWord)
                            visited.add(newWord)
                    
                        word[i] = letter
            step += 1
        
        return 0