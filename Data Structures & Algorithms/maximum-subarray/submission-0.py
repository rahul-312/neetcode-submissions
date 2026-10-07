class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # best = nums[0]
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         best = max(best, total)
        # return best
        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        return best