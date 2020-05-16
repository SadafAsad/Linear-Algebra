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

def makeDetMatrix(n, counter, matrix):
    _matrix = list()
    for i in range(n):
        # first row of matrix is eliminated
        if i!=0:
            row = list()
            for r in range(n):
                # 'the' column is eliminated
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
        # builds 'the' matrix ...
        _matrix = makeDetMatrix(n, counter, matrix)
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
