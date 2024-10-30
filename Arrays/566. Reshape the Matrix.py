# 566. Reshape the Matrix

def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    if m*n != r*c:
        return mat
    res = [[0 for _ in range(c)] for _ in range(r)]
    rows = r
    cols = c
    r, c = 0, 0
    for i in range(m):
        for j in range(n):
            res[r][c] = mat[i][j]
            c += 1
            if c == cols:
                r += 1
                c = 0
    return res
