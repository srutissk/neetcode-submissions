class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # a TON of interesting trade-offs
        # more than 7 sols provided
        # Kadane's Algorithm
        maxSub, currSum = nums[0], 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub