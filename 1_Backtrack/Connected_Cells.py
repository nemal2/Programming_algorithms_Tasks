import sys

def maxRegion(grid):
    max_cell = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                region_cell_count = count_region_cells(grid,row,col)
                max_cell = max(max_cell, region_cell_count)

    return max_cell

def count_region_cells(grid,row,col):

    if any([row<0, col<0, row>= len(grid), col>= len(grid[0])]):
        return 0
    
    if grid[row][col] == 0:
        return 0

    cell_count=1
    grid[row][col]=0


    for r in range(row-1,row+2):
        for c in range(col-1, col+2):
            if any([row!=r , col!=c]):
                cell_count += count_region_cells(grid, r, c)

    return cell_count


arr = [[0,0,1],[1,1,0],[1,1,1]]
ans = maxRegion(arr)
print(f"cell connected = {ans}")
