"""
Problem 42:

3446. Sort Matrix by Diagonals
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output:[[8,2,3],
        [9,6,7],
        [4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105
"""


# def sortMatrix(grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: List[List[int]]
#     """
    
#     diagonals = []
#     temp = []
#     start = 0
#     row_l =len(grid)
#     col = 0
    
#     while start < len(grid[0]):
#         for i in range(start, row_l):
#             diagonal_element = grid[i][col]
#             temp.append(diagonal_element)
#             col += 1
#         diagonals.append(sorted(temp, reverse= True))
#         col = 0
#         temp = []
#         start += 1
    
#     start_col = 1
#     row = 0
#     while start_col < len(grid):
#         for i in range(start_col, len(grid[0])):   
#             diagonal_element = grid[row][i]
#             temp.append(diagonal_element)
#             row += 1
#         diagonals.append(sorted(temp))
#         row = 0
#         temp = []
#         start_col += 1

#     zeros = [[0]*len(grid[0]) for _ in range(len(grid))]
#     print(zeros)

        
    
#     return diagonals



def sortMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    
    diagonals = []
    temp = []
    start = 0
    row_l =len(grid)
    col = 0
    
    while start < len(grid[0]):
        row = 0
        col = start

        while row < len(grid) and col < len(grid[0]):
            diagonal_element = grid[row][col]
            temp.append(diagonal_element)
            row += 1
            col += 1
        diagonals.append(sorted(temp, reverse= True))
        col = 0
        temp = []
        start += 1
    
    start_col = 1
    row = 0

    while start_col < len(grid):
        row = start_col
        col = 0
        while row < len(grid) and col < len(grid[0]):
            diagonal_element = grid[row][col]
            temp.append(diagonal_element)
            row += 1
            col += 1
        diagonals.append(sorted(temp))
        row = 0
        temp = []
        start_col += 1

    zeros = [[0]*len(grid[0]) for _ in range(len(grid))]
    # print(zeros)

    diagonal_index = 0
    start = 0

    while start < len(grid[0]):
        current_diagonal = diagonals[diagonal_index]
        elem_index = 0
        row = 0
        col = start
        while row < len(grid) and col < len(grid[0]):
            zeros[row][col] = current_diagonal[elem_index]
            row += 1
            col += 1
            elem_index += 1
        start += 1
        diagonal_index += 1

    
    start_col = 1

    while start_col < len(grid):
        current_diagonal = diagonals[diagonal_index]
        elem_index = 0
        row = start_col
        col = 0

        while row < len(grid) and col < len(grid[0]):
            zeros[row][col] = current_diagonal[elem_index]
            row += 1
            col += 1
            elem_index += 1
        start_col += 1
        diagonal_index += 1

    # return diagonals
    return zeros




grid = [[1,7,3],[9,8,2],[4,5,6]]

print(sortMatrix(grid))

