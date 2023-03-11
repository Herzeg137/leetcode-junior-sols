#link: https://leetcode.com/problems/sort-an-array/
#t: O(n log n), s: O(n)
#algo: heap sort 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst = nums
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                max_heapify(heap_size, largest)

        # heapify original lst
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)

        # use heap to sort elements
        for i in range(len(lst) - 1, 0, -1):
            # swap last element with first element
            lst[i], lst[0] = lst[0], lst[i]
            # note that we reduce the heap size by 1 every iteration
            max_heapify(i, 0)
        return lst
