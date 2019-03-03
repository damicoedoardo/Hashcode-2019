import numpy as np
import random
from sklearn.preprocessing import MultiLabelBinarizer

def input_reader(filename, header_lines = 1, separator = ' '):
    with open(filename, 'r') as file:
        # store headers line in headers row
        header_rows = []

        for i in range(header_lines):
            row = file.readline()
            row = row.replace('\n', '')
            row = row.split(separator)
            row = list(map(int, row))
            header_rows.append(row)

        # store headers line in headers row
        data_rows = []

        while True:
            row = file.readline()
            if not row:
                break
            row = row.replace('\n', '')
            row = row.split(separator)
            data_rows.append(row)

        return header_rows, data_rows


def num_tags_cluster(filename, header_lines = 1, separator = ' '):
    with open(filename, 'r') as file:
        # store headers line in headers row
        header_rows = []

        for i in range(header_lines):
            row = file.readline()
            row = row.replace('\n', '')
            row = row.split(separator)
            header_rows.append(row)

        # store headers line in headers row
        dictionary = {}

        photo_num = 0
        while True:
            row = file.readline()
            if not row:
                break
            row = row.replace('\n', '')
            row = row.split(separator)
            if row[1] not in dictionary:
                dictionary[row[1]] = [photo_num]
            else:
                dictionary[row[1]].append(photo_num)
            photo_num += 1

        return header_rows, dictionary


def one_hot(dictionary, key, filepath):
    X = []
    position_vec = []
    indeces = dictionary[key]
    with open(filepath, 'r') as data:
        lines = data.readlines()
    photos_number = lines.pop(0)
    for index in indeces:
        position = lines[index].replace('\n','').split(' ')[0]
        position_vec.append(position)
        line = lines[index].replace('\n','').split(' ')[2:]
        X.append(line)
    mlb = MultiLabelBinarizer(sparse_output=True)
    one_hot = mlb.fit_transform(X)
    return indeces, one_hot, position_vec


if __name__ == '__main__':
    filepath = 'dataset/c_memorable_moments.txt'
    h, d = num_tags_cluster(filepath)
    indeces, one_hot, position_vec = one_hot(d, '7', filepath)








