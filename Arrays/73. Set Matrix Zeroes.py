# 73. Set Matrix Zeroes
def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r, c = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for i in range(m):
            for j in range(n):
                if i in r or j in c:
                    matrix[i][j] = 0
        
        return matrix
