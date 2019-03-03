import numpy as np

def get_score(s1, s2):
  return min([len(s1 & s2), len(s1 - s2), len(s2 - s1)])

def run(filepath, verbose=False):
  X = []
  linecount = 0

  with open(filepath) as f:
    linecount = int(f.readline())

    for index in range(linecount):
      X.append([index] + f.readline().replace('\n','').split(' '))
  
  with open('sub.txt', 'w+') as out:
    res = [0]
    count = 1
    prev = X[0]
    out.write(str(0))
    out.write('\n')
    del X[0]

    tot_score = 0
    
    while(len(X) > 0):
      found = False
      max_candidate = (-1, -999999999, -1)
      s1 = set(prev[3:])
      k = 0
      while(k < len(X) and not found):
        if prev[1] == 'H' and X[k][1] == 'H':
          current_id = X[k][0]
          s2 = set(X[k][3:])
          current_score = get_score(s1, s2)
          # store max until now
          if current_score > max_candidate[1]:
            max_candidate = (k, current_score, current_id)
          # check if good score
          if(current_score >= 5):
            prev = X[k]
            count += 1
            res.append(current_id)
            out.write(str(current_id))
            out.write('\n')
            del X[k]
            found = True
            tot_score += current_score
        k += 1
      if not found: # take the best found
        k = max_candidate[0]
        prev = X[k]
        current_id = max_candidate[2]
        count += 1
        res.append(current_id)
        out.write(str(current_id))
        out.write('\n')
        del X[k]
        tot_score += current_score
      print("Chosen: {}".format(current_id))
      
      # print progress
      print("{} / {} - {}%".format(count, linecount, count / linecount), end='\r')
    
    print()
    print("tot score: {}".format(tot_score))
    #print(res)
    print(count)


if __name__ == "__main__":
  run('dataset/b_lovely_landscapes.txt')
  #run('dataset/a_example.txt')
