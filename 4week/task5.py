class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        n = len(matrix)
        while i < n/2 + 1:
            for j in range(i, n - i - 1):
                t = matrix[i][j]
                r = matrix[j][n-i-1]
                b = matrix[n-i-1][n-j-1]
                l = matrix[n-j-1][i]
                matrix[i][j] = l
                matrix[j][n-i-1] = t
                matrix[n-i-1][n-j-1] = r
                matrix[n-j-1][i] = b
            i += 1