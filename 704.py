class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            g = nums[mid]

            if g == target:
                return mid
            elif g > target:
                r = mid - 1
            else:
                l = mid + 1
        else:
            return -1
          
#link: https://leetcode.com/problems/binary-search/description/?envType=study-plan&id=algorithm-i
#time: O(log n), space: O(n)
