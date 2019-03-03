import scipy.sparse as sps

def o_creator(matrix, initial_row, position_vec):
    with open('sub.txt', 'w+') as sub:
        row_index = initial_row
        while(True):
            row = matrix.getrow(row_index)
            c = row.argmax()




            #matrix.setrow(row_index)
            #matrix.setcol(c)
            sub.write(row_index)
            row_index = c



if __name__ == '__main__':
    matrix, _ = one_hot_encoded('dataset/c_memorable_moments.txt')
    o_creator(matrix,0)

