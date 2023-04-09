class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst = nums
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j

            lst[min_index], lst[i] = lst[i], lst[min_index]
        return lst
