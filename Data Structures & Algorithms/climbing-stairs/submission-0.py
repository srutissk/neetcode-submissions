class Solution:
    def climbStairs(self, n: int) -> int:
        #4 dynammic p (space optimized)
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one