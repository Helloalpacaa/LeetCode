class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var dict: [String: [String]] = [:]
        
        for str in strs {
            let sorted_str = String(str.sorted())
            dict[sorted_str, default: []].append(str)
        }

        return Array(dict.values)
    }
}