import numpy as np

def dotProduct(a: list, b: list) -> float:
    total = float(0)

    for i in range(len(a)):
        total += a[i] * b[i]

    return total

def mag(a: list) -> float:
    m = float(0)

    for i in range(len(a)):
        m+= a[i] * a[i]

    return np.sqrt(m)
def cosine_similarity(a: list, b: list) -> float:
    
    """
    Returns the cosine similarity as a Python float.
    """
    if mag(a) == 0 or mag(b) == 0:
        return float(0)
        
    res = float((dotProduct(a,b)) / (mag(a) * mag(b)))

    return res