class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_a = 0
        while left < right:
            width = right - left
            curr_h = min(heights[left], heights[right])
            curr_a = width * curr_h
            max_a = max(max_a, curr_a)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_a