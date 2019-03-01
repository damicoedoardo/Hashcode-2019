import scipy.sparse as sps
import numpy as np
from one_hot import one_hot_encoded

def minimum(A, B):
    BisBigger = A-B
    BisBigger.data = np.where(BisBigger.data < 0, 0, 1)
    return A - A.multiply(BisBigger) + B.multiply(BisBigger)

# matrix: a csr matrix containing onehot encodings
def compute_min(matrix):
    ones = sps.csr_matrix(np.ones(matrix.shape), dtype=np.int8)
    matrix_bar = ones - matrix

    fst = matrix*matrix.transpose()
    snd = matrix_bar*matrix.transpose()
    trd = matrix*matrix_bar.transpose()

    result = minimum(fst, snd)
    return minimum(result, trd)

m,l,o = one_hot_encoded('dataset/a_example.txt')
compute(m)
print(m)
