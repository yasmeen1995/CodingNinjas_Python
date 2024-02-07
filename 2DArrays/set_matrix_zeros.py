def set_matrix_zeros(matrix):
    first_row_zero = False
    first_col_zero = False
    n = len(matrix)
    m = len(matrix[0])

    for i in range(m):
        if matrix[0][i] == 0:
            first_row_zero = True
            break

    for i in range(n):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if first_col_zero:
        for i in range(n):
            matrix[i][0] = 0
    
    if first_row_zero:
        for i in range(m):
            matrix[0][i] = 0

    return matrix


output = set_matrix_zeros([[1,2,3],[2,0,0],[3,4,5]])
print(output)

