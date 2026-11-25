class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size < 3:
            return 0

        area = 0
        i, j = 0, 1
        temp_area = 0
        while j < size:
            if height[j] >= height[i]:
                area += temp_area
                temp_area = 0
                i = j
            else:
                temp_area += height[i] - height[j]
            j += 1

        peak = i
        i, j = size - 1, size - 2
        temp_area = 0
        while j >= peak:
            if height[j] >= height[i]:
                area += temp_area
                temp_area = 0
                i = j
            else:
                temp_area += height[i] - height[j]
            j -= 1

        return area