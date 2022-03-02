# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the
# current row, you may move to either index i or index i + 1 on the next row.

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 1. The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# 2. Find the path
from _ast import List


def minimumTotal(self, a: List[List[int]]) -> int:
    n = len(a)
    dp = [0] * n
    dp[0] = a[0][0]
    for i in range(1, n):
        for j in range(i, -1, -1):
            dp[j] = a[i][j] + min(dp[j] if j < i else float('inf'), dp[j - 1] if j >= 1 else float('inf'))
    return min(dp)