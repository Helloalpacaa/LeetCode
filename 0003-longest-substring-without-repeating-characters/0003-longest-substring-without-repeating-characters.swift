class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var window: Set<Character> = Set()
        var longest = 0

        let array = Array(s)
        var left = 0

        for right in 0..<array.count {
            while window.contains(array[right]) {
                window.remove(array[left])
                left += 1
            }

            window.insert(array[right])

            longest = max(longest, window.count)
        }

        return longest
    }
}