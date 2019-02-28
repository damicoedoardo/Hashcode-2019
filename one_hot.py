from sklearn.preprocessing import MultiLabelBinarizer

def one_hot_encoded(filepath, verbose=False):
  X = []

  #with open('dataset/b_lovely_landscapes.txt') as f:
  with open(filepath) as f:
    linecount = int(f.readline())

    for i in range(linecount):
      line = f.readline().replace('\n','').split(' ')[2:]
      X.append(line)

  if verbose:
    print(X)

  mlb = MultiLabelBinarizer()
  one_hot = mlb.fit_transform(X)

  if verbose:
    print(one_hot)
  
  return one_hot, mlb.classes_


if __name__ == "__main__":
    a,b = one_hot_encoded('dataset/a_example.txt', verbose=True)
    print(b)