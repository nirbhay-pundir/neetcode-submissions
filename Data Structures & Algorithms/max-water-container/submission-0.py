class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        size = len(heights)
        i, j = 0, size - 1

        while i < j:
            max_area = max((j - i) * min(heights[i], heights[j]), max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area