class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var index = 0
        for i in 0..<nums.count {
            if nums[i] != 0 {
                nums[index] = nums[i]
                index += 1
            }
        }

        while index < nums.count {
            nums[index] = 0
            index += 1
        }
    }
}