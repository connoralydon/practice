# transpose.py

def transpose_square(matrix):
    #transposing a squaare matrix without using more memory. It just swaps elements.
    
    
    # this algo iterates over the trianle on the top left
    
    # iterate over all rows
    left_offset = 0
    for old_row in range(len(matrix)-1):
        for old_col in range(len(matrix[0])-1, left_offset, -1):
            matrix[old_col][old_row], matrix[old_row][old_col] = matrix[old_row][old_col], matrix[old_col][old_row]

        left_offset += 1 
        # +1 because it is looking at right triangle
    
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    # transposed across 1 5 9
    # [[1 4 7]
    #  [2 5 8]
    #  [3 6 9]]
    #
    
    return matrix

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows == cols: # square matrix
        return transpose_square(matrix)
    
    transposed = []
    for k in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][k]) # appending opposite one
        transposed.append(row)
        
    return transposed


