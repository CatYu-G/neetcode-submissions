class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #i, i-1(cursum)
        curSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum
        #1, 2, -5, 3
    