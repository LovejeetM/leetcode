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
    col = 0
    
    while start < len(grid[0]):
        row = 0
        col = 0
        row = start

        while row < len(grid) and col < len(grid[0]):
            diagonal_element = grid[row][col]
            temp.append(diagonal_element)
            row += 1
            col += 1
        diagonals.append(sorted(temp, reverse= True))
        
        temp = []
        start += 1
    
    start_col = 1
    row = 0

    while start_col < len(grid):
        col = 0
        row = 0
        row = start_col
        while row < len(grid) and col < len(grid[0]):
            diagonal_element = grid[col][row]
            temp.append(diagonal_element)
            row += 1
            col += 1
        diagonals.append(sorted(temp))
        
        temp = []
        start_col += 1

    zeros = [[0]*len(grid[0]) for _ in range(len(grid))]
    # print(zeros)

    
    start = 0
    col = 0

    diagonal = 0
    ct = 0
    
    while start < len(grid[0]):
        row = 0
        col = 0
        row = start
        while row < len(grid) and col < len(grid[0]):
            zeros[row][col] = diagonals[diagonal][ct]
            ct += 1
            row += 1
            col += 1
        ct = 0
        diagonal += 1
        start += 1
    
    start_col = 1
    row = 0

    while start_col < len(grid):
        col = 0
        row = 0
        row = start_col
        while row < len(grid) and col < len(grid[0]):
            zeros[col][row] = diagonals[diagonal][ct]
            ct += 1
            row += 1
            col += 1
        ct = 0
        diagonal += 1
        start_col += 1

    return zeros

grid = [[1,7,3],[9,8,2],[4,5,6]]

print(sortMatrix(grid))


#Optimal
def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diagonals = defaultdict(list)

    # Step 1: Group elements by diagonals using i - j as the key
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

    # Step 2: Sort diagonals based on the rule
        for key in diagonals:
            if key < 0:
                diagonals[key].sort()  # ascending
            else:
                diagonals[key].sort(reverse=True)  # descending

    # Step 3: Place the sorted values back
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
