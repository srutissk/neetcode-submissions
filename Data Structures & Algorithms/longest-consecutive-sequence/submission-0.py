class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force / sorting / hashmap solutions exist
        # below is hash set solution (3)
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        