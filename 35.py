#link: https://leetcode.com/problems/search-insert-position/?envType=study-plan&id=algorithm-i
#time: O(log n), space: (n), algo: Binary search
class Solution(object):
    def searchInsert(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while (lo <= hi):
            #mid = lo + (target - A[lo]) * (hi - lo) // (A[hi] - A[lo])
            m = (hi + lo)//2

            if target==nums[m]:return m
            elif target<nums[m]:hi = m - 1
            else:lo = m + 1
        return lo
