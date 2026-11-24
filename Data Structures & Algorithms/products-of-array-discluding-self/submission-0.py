class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        length = len(nums)
        for i in range(1, length):
            prefix_products.append(prefix_products[i-1] * nums[i-1])
            
        suffix_products = [1]*length
        for i in reversed(range(0, length-1)):
            suffix_products[i] = suffix_products[i + 1] * nums[i+1]

        return [(p*s) for p, s in zip(prefix_products, suffix_products)]