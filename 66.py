#link: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        x = "".join(map(str, digits))
        m = int(x) + 1
        for i in str(m):
            arr.append(int(i))
        return arr
      
      
#time: O(n)
#space: O(n)
