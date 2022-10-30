
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        a, b = 0, 0
        for index in range(len(cost) - 3, -1, -1):
            step_1 = a + cost[index+1]
            step_2 = cost[index+2] + b 
            a, b = min(step_1, step_2), a
        return a
    