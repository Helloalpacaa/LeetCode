class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashmap = {}
        substitute = 'a'
        for letter in key:
            if letter.isalpha() and letter not in hashmap.keys():
                hashmap[letter] = substitute
                substitute = chr(ord(substitute) + 1)

        message = list(message)
        for i in range(len(message)):
            if message[i].isalpha():
                message[i] = hashmap[message[i]]
        
        return "".join(message)