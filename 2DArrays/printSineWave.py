def print_sine_wave(matrix, n, m):
    ans = []
    for col in range(0, m):
        if col % 2==0 :
            #even: top to bottom:
            for row in range(0, n):
                ans.append(matrix[row][col])
        else:
            # Odd: Bottom to Top
            for row in range(n-1, -1, -1):
                ans.append(matrix[row][col])

    return ans


print(print_sine_wave([[1,2,3],[4,5,6],[7,8,9]],3,3 ))