class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        let matching: [Character: Character] = [")": "(", "}": "{", "]": "["]

        for char in s {
            if "({[".contains(char) {
                stack.append(char)
            } else {
                if stack.isEmpty || stack.last != matching[char] {
                    return false
                }
                stack.popLast()
            }
        }

        return stack.isEmpty
    }
}