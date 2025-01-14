class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = set()
        steps = 0

        while queue:
            size = len(queue)

            while size:
                word = queue.popleft()

                if word == endWord:
                    return steps + 1
                
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        if char == word[i]:
                            continue

                        new_word = list(word)
                        new_word[i] = char
                        new_word = "".join(new_word)
                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
                
                size -= 1
            
            steps += 1
        
        return 0



        