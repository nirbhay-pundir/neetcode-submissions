class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if len(height) < 3:
            return 0

        area = 0
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        

        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(size))