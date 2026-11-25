class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights) - 1
        max_h = max(heights)

        while i < j:
            if (j - i) * max_h <= max_area:
                break
            h_i, h_j = heights[i], heights[j]
            if h_i < h_j:
                area = (j - i) * h_i
                if area > max_area:
                    max_area = area
                i += 1
                while i < j and heights[i] <= h_i:
                    i += 1
            else:
                area = (j - i) * h_j
                if area > max_area:
                    max_area = area
                j -= 1
                while i < j and heights[j] <= h_j:
                    j -= 1

        return max_area