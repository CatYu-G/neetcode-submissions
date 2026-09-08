class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robLine(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], houses[i] + dp[i-2])
            return dp[-1]
        
        situationA = robLine(nums[:-1])
        situationB = robLine(nums[1:])

        return max(situationA, situationB)