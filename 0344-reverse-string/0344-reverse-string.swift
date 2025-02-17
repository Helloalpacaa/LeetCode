class Solution {
    func reverseString(_ s: inout [Character]) {
        var left = 0
        var right = s.count - 1

        while left < right {
            var tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1
        }
    }
}