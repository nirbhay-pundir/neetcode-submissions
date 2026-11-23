from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for i, c in enumerate(count):
            if i >= k:
                break
            result.append(count.most_common()[i][0])
        return result