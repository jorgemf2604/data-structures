# A brute force solution
class Solution:
    def runningSum(self, nums):
      result = [0] * len(nums)
      result[0] = nums[0]
      suma_intermedia = 0
      for i in range(1, len(nums)):
        suma_intermedia = 0
        for j in range(0, i+1):
           suma_intermedia += nums[j]
        result[i] = suma_intermedia
      return result
           

    
# Test the algorithm with example inputs
solution = Solution()
print(solution.runningSum([2, 3, 5, 1, 6]))  # Output: [2, 5, 10, 11, 17]
print(solution.runningSum([1, 1, 1, 1, 1]))  # Output: [1, 2, 3, 4, 5]
print(solution.runningSum([-1, 2, -3, 4, -5]))  # Output: [-1, 1, -2, 2, -3]

# Time complexity: O(n^2)
# Space complexity: O(1) 


# A better solution
class Solution2:
    def runningSum(self, nums):
        result = [0] * len(nums)  
        result[0] = nums[0]  # First element is the same
        for i in range(1, len(nums)):  # Start from the second element
            result[i] = result[i-1] + nums[i]  # Add current number to the previous sum
        return result
    
# Test the algorithm with example inputs
solution2 = Solution2()
print(solution2.runningSum([2, 3, 5, 1, 6]))  # Output: [2, 5, 10, 11, 17]
print(solution2.runningSum([1, 1, 1, 1, 1]))  # Output: [1, 2, 3, 4, 5]
print(solution2.runningSum([-1, 2, -3, 4, -5]))  # Output: [-1, 1, -2, 2, -3]

# Time complexity: O(n)
# Space complexity: O(1) 