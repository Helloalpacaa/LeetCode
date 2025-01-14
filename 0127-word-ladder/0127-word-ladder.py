class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        steps = 0
        queue = deque([beginWord])
        visited = set(beginWord)

        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return steps + 1

                for i in range(len(word)):
                    new_word = list(word)

                    for char in string.ascii_lowercase:
                        if char == word[i]:
                            continue

                        new_word = list(new_word)
                        new_word[i] = char
                        new_word = "".join(new_word)

                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            
            steps += 1
        
        return 0

