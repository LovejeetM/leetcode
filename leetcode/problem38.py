"""
Problem 38:

3195. Find the Minimum Area to Cover All Ones I
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
"""

def minimumArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    dim = []
    for i, row in enumerate(grid):
        if 1 in row:
            dim.append(i)
            break

    if not dim:
        return 0


    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == 1:
                dim.append(j)
                break
        if len(dim) == 2:
            break

    for i in range(len(grid) - 1, -1, -1):
        if 1 in grid[i]:
            dim.append(i)
            break
        if len(dim) == 3:
            break

    for j in range(len(grid[len(grid)-1])-1, -1, -1):
        # for i in range(len(grid) -1, -1, -1):
        for i in range(len(grid)):
            if grid[i][j] == 1:
                dim.append(j)
                break
        if len(dim) == 4:
            break

    
    height = dim[2] - dim[0] + 1
    width = dim[3] - dim[1] + 1
    
    return height * width

            
grid = [[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]]
print(minimumArea(grid))
