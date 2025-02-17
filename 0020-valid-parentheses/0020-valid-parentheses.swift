class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []

        for char in s {
            if stack.isEmpty && ")]}".contains(char) {
                return false
            }

            if "([{".contains(char) {
                stack.append(char)
            }

            if char == ")" {
                if stack.last == "(" {
                    stack.popLast()
                } else {
                    return false
                }
            } else if char == "}" {
                if stack.last == "{" {
                    stack.popLast()
                } else {
                    return false
                }
            } else if char == "]" {
                if stack.last == "[" {
                    stack.popLast()
                } else {
                    return false
                }
            }
        }

        return stack.isEmpty
    }
}