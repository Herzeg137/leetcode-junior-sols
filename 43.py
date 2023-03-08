#link: https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #1 way -> low, end illegal to the task
        return str(int(num1) * int(num2))
