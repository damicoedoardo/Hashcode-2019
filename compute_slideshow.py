import scipy.sparse as sps
import numpy as np
from one_hot import one_hot_encoded

# matrix: a csr matrix containing onehot encodings
def compute(matrix):
    first = matrix*matrix.transpose()



l,m = one_hot_encoded('dataset/a_example.txt')
print(m.toarray())