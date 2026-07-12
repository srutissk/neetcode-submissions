class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            result[i] = prod
        return result
        """
        # optimal solution - two pass with O(1) space only prefix/postfix
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

        