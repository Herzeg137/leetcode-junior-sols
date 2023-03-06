class Solution(object):
    def findNumbers(self, nums):
        c = 0
        for i in map(str, nums):
            if len(i) % 2 == 0:
                c += 1
        return c
      
#Time complexity: o(n)
#Space: O(1)
#Link to problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
