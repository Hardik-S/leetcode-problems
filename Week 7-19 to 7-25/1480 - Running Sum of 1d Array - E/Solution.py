from itertools import accumulate

class Solution:
    def runningSum(self, nums):
        return accumulate(nums)
