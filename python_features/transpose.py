def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for k in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][k]) # appending opposite one
        transposed.append(row)
        
    return transposed