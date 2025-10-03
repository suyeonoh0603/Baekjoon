grid = [list(map(int, input().split())) for i in range(9)]

max = grid[0][0]
max_row, max_col = 1, 1

for i in range(9) :
    for j in range(9) :
        if grid[i][j] > max :
            max = grid[i][j]
            max_row, max_col = i+1, j+1
            
print(max)
print(max_row, max_col)