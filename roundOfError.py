def matrixInitializer(n, num, data):
    matrix = list()
    counter = 0
    for i in range(n):
        row_data = list()
        matrix.append(row_data)
        # if matrix b
        if num==3:
            row_data.append(data[counter])
            counter+=1
        else:
            for r in range(n):
                row_data.append(data[counter])
                counter+=1
    return matrix

def takingSamplesFromTerminal():
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

def readSamplesFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()
    samples = list()
    matrix_num = 1
    for line in file_lines:
        if line!='0':
            line_str = line.split()
            line_length = len(line_str)
            # if matrix's dimension
            if line_length==1:
                sample = list()
                samples.append(sample)
                n = int(line_str[0])
            else:
                # if start of new sample
                if matrix_num==4:
                    matrix_num = 1
                line_list = list()
                i = 0
                while(i<line_length):
                    line_list.append(float(line_str[i]))
                    i = i + 1
                # matrix initialize
                sample.append(matrixInitializer(n, matrix_num, line_list))
                matrix_num+=1
    return samples

def q1(samples):
    counter = 1
    for sample in samples:
        print("Sample " + str(counter) + ": " + str(sample))
        counter+=1 
# ans = readSamplesFromFile("linear_solve.data")
# q1(ans)

def det2_2(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

def makeDetMatrix(row, column, matrix):
    _matrix = list()
    n = len(matrix)
    for i in range(n):
        # 'the' row is eliminated
        if i!=row:
            _matrix_row = list()
            for j in range(n):
                # 'the' column is eliminated
                if j!=column:
                    _matrix_row.append(matrix[i][j])
            _matrix.append(_matrix_row)
    return _matrix

def detn_n(matrix):
    n = len(matrix)
    if n==2:
        return det2_2(matrix)
  
    det = 0
    for counter in range(n):
        # builds 'the' matrix ...
        _matrix = makeDetMatrix(0, counter, matrix)
        # for + and - ...
        if counter%2==0:
            det+=(matrix[0][counter]*detn_n(_matrix))
        else:
            det-=(matrix[0][counter]*detn_n(_matrix))
    return det
# print(detn_n([[6,1,1],[4,-2,5],[2,8,7]]))
# print(detn_n([[0,10,2,3],[1,12,5,11],[12,10,2,4],[1,3,5,10]]))

def q2(samples):
    samples_length = len(samples)
    for i in range(samples_length):
        A_det = detn_n(samples[i][0])
        H_det = detn_n(samples[i][1])
        print("Sample " + str(i+1) + ": " + "det(A)=" + str(A_det) + " det(H)=" + str(H_det) + "\n")
# samples = readSamplesFromFile("linear_solve.data")
# q2(samples)

def minorsMatrix(matrix):
    matrix_length = len(matrix)
    minors = list()
    for i in range(matrix_length):
        row = list()
        for j in range(matrix_length):
            row.append(detn_n(makeDetMatrix(i, j, matrix)))
        minors.append(row)
    return minors
# print(minorsMatrix([[3,0,2],[2,0,-2],[0,1,1]]))

def cofactorsMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                matrix[i][j] = -matrix[i][j]
    return matrix
# print(cofactorsMatrix(minorsMatrix([[3,0,2],[2,0,-2],[0,1,1]])))

def adjugateMatrix(matrix):
    n = len(matrix)
    counter = 0
    for i in range(n):
        for j in range(n):
            if j>=counter:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        counter+=1
    return matrix
# print(adjugateMatrix(cofactorsMatrix(minorsMatrix([[3,0,2],[2,0,-2],[0,1,1]]))))

def multiplyByDetInv(matrix, original_matrix):
    n = len(matrix)
    detInv = detn_n(original_matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j]/=detInv
    return matrix
# print(multiplyByDetInv(adjugateMatrix(cofactorsMatrix(minorsMatrix([[3,0,2],[2,0,-2],[0,1,1]]))),[[3,0,2],[2,0,-2],[0,1,1]]))
            
def matrixInverse(matrix):
    minor_matrix = minorsMatrix(matrix)
    cofactor_matrix = cofactorsMatrix(minor_matrix)
    adjugate_matrix = adjugateMatrix(cofactor_matrix)
    inverse_matrix = multiplyByDetInv(adjugate_matrix, matrix)
    return inverse_matrix 
# print(matrixInverse([[3,0,2],[2,0,-2],[0,1,1]]))
