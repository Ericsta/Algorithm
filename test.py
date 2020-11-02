class Solution:
    def maxArea(self, matrix):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(matrix), len(matrix[0])

        def dfs(sum_island, x, y):
            # print(sum_island,matrix,x,y)
            if matrix[x][y] != 0:
                sum_island += matrix[x][y]
                matrix[x][y] = 0
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        if matrix[nx][ny] != 0:
                            # a =
                            # print(a)
                            sum_island = dfs(sum_island, nx, ny)
            # print(sum_island)
            return sum_island

        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    # print(matrix)
                    ans = max(ans, dfs(0, i, j))


        return ans


if __name__ == '__main__':
    matrix = [[0, 2, 0, 0, 1, 0], [1, 1, 2, 0, 5, 1], [1, 0, 0, 0, 2, 0], [0, 3, 4, 0, 0, 2], [1, 0, 1, 0, 2, 1]]
    solution = Solution()
    A = solution.maxArea(matrix)
    print(A)
