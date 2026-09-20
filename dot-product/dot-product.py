import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """

    total = float(0);

    for i in range(len(x)):
        total += x[i] * y[i]
        
    return total