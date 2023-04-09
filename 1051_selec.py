#I solved this again but with selection sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        exp = heights
        lst = heights[:]
        for i in range(len(heights)):
            min_ind = i
            for j in range( i + 1, len(heights)):
                if heights[min_ind] > heights[j]:
                    min_ind = j
            heights[min_ind], heights[i] = heights[i], heights[min_ind]
        
        c = 0
        for i in range(len(heights)):
            if lst[i] != exp[i]:
                c += 1
        
        return c
