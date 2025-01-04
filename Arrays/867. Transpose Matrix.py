# Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        ans = [[None] * rows for _ in range(cols)]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
