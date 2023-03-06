class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c,num = 0,0
        for i in nums:
            if i == 1:
                c += 1
            else:
                c = 0
            if c > num:
                num = c 
        return num


#Time complexity: o(n)
#Auxilary space: O(2)
#Link to the problem: https://leetcode.com/problems/max-consecutive-ones/
