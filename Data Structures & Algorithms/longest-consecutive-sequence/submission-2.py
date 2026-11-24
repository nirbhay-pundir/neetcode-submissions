class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max_length = 0
        length = 0
        prev_num = 0
        for n in nums:
            if max_length == 0:
                length = 1
                max_length = 1
            elif n - prev_num == 1:
                length += 1
            elif n - prev_num != 0:
                length = 1
            prev_num = n
            if max_length <= length:
                max_length = length
        return max_length