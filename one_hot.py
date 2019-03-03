import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

def one_hot_encoded(filepath, verbose=False):
  X = []
  orientations = []

  #with open('dataset/b_lovely_landscapes.txt') as f:
  with open(filepath) as f:
    linecount = int(f.readline())

    for i in range(linecount):
      line = f.readline().replace('\n','').split(' ')
      orientations.append(line[0])
      X.append(line[2:])
  
  orientations = np.array(orientations)

  mlb = MultiLabelBinarizer(sparse_output=False)
  one_hot = mlb.fit_transform(X)

  if verbose:
    print(X)
    print(orientations)
    print(one_hot)
  
  return one_hot, mlb.classes_, orientations


if __name__ == "__main__":
    a,b,c = one_hot_encoded('dataset/b_lovely_landscapes.txt')
    print(a)
    print(b)
    print(c)