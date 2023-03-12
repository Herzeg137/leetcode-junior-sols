#link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
#t: O(n) s: O(1)
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            if arr[i]*2 in (arr[:i]+arr[i+1:]):
                return True
        
        return False
