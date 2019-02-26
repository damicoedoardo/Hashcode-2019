import numpy as np

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
            row = list(map(int, row))
            data_rows.append(row)

        return header_rows, data_rows


if __name__ == '__main__':
    h, d = input_reader('input_example/input1')
    print(h)
    print(d)