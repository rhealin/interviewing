def spiral_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    def done():
        return len(result) == width * height

    result = []
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return result

    top_row_index, right_col_index, bottom_row_index, left_col_index = 0, 0, 0, 0
    width, height = len(matrix[0]), len(matrix)
    
    while True:
        # right
        for i in range(left_col_index, width - right_col_index):
            result.append(matrix[top_row_index][i])
        top_row_index += 1
        if done():
            break
    
        # down
        for i in range(top_row_index, height - bottom_row_index):
            result.append(matrix[i][-right_col_index-1])
        right_col_index += 1
        if done():
            break
        
        # left
        for i in range(right_col_index, width - left_col_index):
            result.append(matrix[-bottom_row_index-1][-i-1])
        bottom_row_index += 1
        if done():
            break
        
        # up
        for i in range(bottom_row_index, height - top_row_index):
            result.append(matrix[-i-1][left_col_index])
        left_col_index += 1
        if done():
            break
    
    return result

print(spiral_order([
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]))
## [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(spiral_order([
[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10,11,12]
]))
## [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

print(spiral_order([]))
## []

print(spiral_order([[], []]))
## []