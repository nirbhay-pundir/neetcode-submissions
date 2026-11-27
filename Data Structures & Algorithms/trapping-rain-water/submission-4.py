class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(h, height[left]) - height[bottom]
                area += width * bounded_height
            stack.append(i)

        return area