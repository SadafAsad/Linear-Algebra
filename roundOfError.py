def matrixInitializer(n, num, data):
    matrix = list()
    counter = 0
    for i in range(n):
        line_data = list()
        matrix.append(line_data)
        if num==3:
            line_data.append(data[counter])
            counter+=1
        else:
            for r in range(n):
                line_data.append(data[counter])
                counter+=1
    return matrix

# def matrixDisplay(matrix):

def takingMatrixData():
    _input = input()
    samples = list()
    matrix_num = 1
    while _input!='o':
        _input_str = _input.split()
        _input_length = len(_input_str)
        if _input_length==1:
            sample = list()
            samples.append(sample)
            n = int(_input_str[0])
        else:
            if matrix_num==4:
                matrix_num = 1
            _input_list = list()
            i = 0
            while(i<_input_length):
                _input_list.append(float(_input_str[i]))
                i = i + 1
            sample.append(matrixInitializer(n, matrix_num, _input_list))
            matrix_num+=1
        _input = input()
    return samples

# ans = matrixInitializer(2, [1.0, 3.2, 2.1, 1.1])
# print(ans)

ans = takingMatrixData()
print(ans)
