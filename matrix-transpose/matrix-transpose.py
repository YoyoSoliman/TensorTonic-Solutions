import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    row = len(A)
    col = len(A[0])

    transposedMatrix = np.zeros((col,row))

    for i in range (row):
        for j in range (col):
            transposedMatrix[j][i] = A[i][j]
    
    return transposedMatrix
