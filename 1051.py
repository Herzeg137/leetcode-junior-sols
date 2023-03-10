class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        lst = heights[:]
        for i in range(len(heights)):
            for i in range(len(heights) - 1):
                if heights[i] > heights[i + 1]:
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
                    
        exp = heights
        for i in range(len(heights)):
            if lst[i] != exp[i]:
                c+= 1
        return c
      
#I solwed it using bubble sort algorithm
#Time: O(n**2), Space: O(n)
