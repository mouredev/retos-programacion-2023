import Foundation

func findCombinations(_ nums: [Int], target: Int) -> [[Int]] {
    var result = [[Int]]()
    var path = [Int]()
    findCombinationsRecursive(&result, &path, nums, target, 0)
    return result
}

func findCombinationsRecursive(_ result: inout [[Int]], _ path: inout [Int], _ nums: [Int], _ target: Int, _ index: Int) {
    if target == 0 {
        result.append(path)
        return
    }
    
    for i in index..<nums.count {
        if nums[i] <= target {
            path.append(nums[i])
            findCombinationsRecursive(&result, &path, nums, target - nums[i], i + 1)
            path.removeLast()
        }
    }
}

let numbers = [1, 5, 3, 2]
let target = 6
let combinations = findCombinations(numbers, target: target)
print(combinations) 
