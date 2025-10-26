class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        steps = 1
        queue = deque([beginWord])

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps

                s = list(word)
                for i, c in enumerate(s):
                    for letter in string.ascii_lowercase:
                        if letter == c:
                            continue
                        s[i] = letter
                        if "".join(s) in wordList:
                            queue.append("".join(s))
                            wordList.remove("".join(s))
                        s[i] = c
            
            steps += 1
        
        return 0
                        
            