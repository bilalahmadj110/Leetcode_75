

class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        next_two = 1, 1
        possible = 0
        for _ in range(n - 2, -1, -1):
            possible = sum(next_two)
            next_two = possible, next_two[0]
        
        return possible
    
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
        
    