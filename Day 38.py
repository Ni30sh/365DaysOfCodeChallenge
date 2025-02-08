def search(matrix, n, m, x):
    # Start from top-right corner
    i = 0       # row index
    j = m - 1   # column index
    
    while i < n and j >= 0:
        if matrix[i][j] == x:
            return True
        elif matrix[i][j] > x:
            j -= 1    # Move left
        else:
            i += 1    # Move down
    
    return False

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = 3  # rows
m = 3  # columns
x = 5  # element to search

print(search(matrix, n, m, x))  # Output: True