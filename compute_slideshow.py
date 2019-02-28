import scipy.sparse as sps
import numpy as np
from one_hot import one_hot_encoded

# matrix: a csr matrix containing onehot encodings
def compute(matrix):
    first = matrix*matrix.transpose()
    ones = np.ones((matrix.shape[0], matrix.shape[1]), dtype=np.int8)
    a = 1

m,l = one_hot_encoded('dataset/b_lovely_landscapes.txt')
compute(m)
# print(l.toarray())