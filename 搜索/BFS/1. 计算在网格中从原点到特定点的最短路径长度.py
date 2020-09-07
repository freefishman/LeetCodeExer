# 1091. Shortest Path in Binary Matrix(Medium)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for i in range(n)]
        if n == 1 and m == 1:
            return 1
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        x = [-1,-1,-1,0,0,1,1,1]
        y = [-1,0,1,-1,1,-1,0,1]
        stack = [(0,0)]
        visited[0][0] = 1
        step = 1
        tmp_list = []
        while len(stack):
            cur_x, cur_y = stack.pop()
            step = visited[cur_x][cur_y]
            step += 1
            for i in range(8):
                next_x ,next_y = cur_x + x[i], cur_y + y[i]
                if next_x == n-1 and next_y == m-1:
                    return step
                elif 0 <= next_x <= n-1 and 0 <= next_y <= m-1 and grid[next_x][next_y] == 0 and visited[next_x][next_y]==0:
                    tmp_list.append((next_x,next_y))
                    visited[next_x][next_y] = step
                else:
                    continue
            if len(stack) == 0:
                stack = tmp_list.copy()
                tmp_list = []
        return -1