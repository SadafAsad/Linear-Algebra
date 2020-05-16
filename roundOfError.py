def matrixInitializer(n, num, data):
    matrix = list()
    counter = 0
    for i in range(n):
        line_data = list()
        matrix.append(line_data)
        # if matrix b
        if num==3:
            line_data.append(data[counter])
            counter+=1
        else:
            for r in range(n):
                line_data.append(data[counter])
                counter+=1
    return matrix

def takingMatrixData():
    _input = input()
    samples = list()
    matrix_num = 1
    while _input!='o':
        _input_str = _input.split()
        _input_length = len(_input_str)
        # if matrix's dimension
        if _input_length==1:
            sample = list()
            samples.append(sample)
            n = int(_input_str[0])
        else:
            # if start of new sample
            if matrix_num==4:
                matrix_num = 1
            _input_list = list()
            i = 0
            while(i<_input_length):
                _input_list.append(float(_input_str[i]))
                i = i + 1
            # matrix initialize
            sample.append(matrixInitializer(n, matrix_num, _input_list))
            matrix_num+=1
        _input = input()
    return samples

def q1(samples):
    counter = 1
    for sample in samples:
        print("Sample " + str(counter) + ": " + str(sample))
        counter+=1
        
# ans = takingMatrixData()
# q1(ans)

def det2_2(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
# print(det2_2([[3,8],[4,6]]))

def makeDetMatrix(n, counter, matrix):
    _matrix = list()
    for i in range(n):
        if i!=0:
            row = list()
            for r in range(n):
                if r!=counter:
                    row.append(matrix[i][r])
            _matrix.append(row)
    return _matrix

def detn_n(matrix):
    n = len(matrix)
    if n==2:
        return det2_2(matrix)
  
    det = 0
    for counter in range(n):
        _matrix = makeDetMatrix(n, counter, matrix)
        if counter%2==0:
            det+=(matrix[0][counter]*detn_n(_matrix))
        else:
            det-=(matrix[0][counter]*detn_n(_matrix))
    return det

# print(detn_n([[6,1,1],[4,-2,5],[2,8,7]]))
# print(detn_n([[0,10,2,3],[1,12,5,11],[12,10,2,4],[1,3,5,10]]))