import math

def zeroMatrix(n,m):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix

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
                    i+=1
                # matrix initialize
                sample.append(matrixInitializer(n, matrix_num, line_list))
                matrix_num+=1
    return samples

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
        # for + and -
        if counter%2==0:
            det+=(matrix[0][counter]*detn_n(_matrix))
        else:
            det-=(matrix[0][counter]*detn_n(_matrix))
    return det

def minorsMatrix(matrix):
    matrix_length = len(matrix)
    minors = list()
    # if 2x2 matrix
    if matrix_length==2:
        return matrix
    for i in range(matrix_length):
        row = list()
        for j in range(matrix_length):
            row.append(detn_n(makeDetMatrix(i, j, matrix)))
        minors.append(row)
    return minors

def cofactorsMatrix(matrix):
    n = len(matrix)
    _matrix = zeroMatrix(n,n)
    for i in range(n):
        for j in range(n):
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                _matrix[i][j] = -matrix[i][j]
            else:
                _matrix[i][j] = matrix[i][j]
    return _matrix

def adjugateMatrix(matrix):
    n = len(matrix)
    _matrix = zeroMatrix(n,n)
    counter = 0
    for i in range(n):
        for j in range(n):
            _matrix[i][j] = matrix[i][j]
    # if 2x2 matrix
    if n==2:
        return [
            [_matrix[1][1],_matrix[0][1]],
            [_matrix[1][0],_matrix[0][0]]
        ]
    for i in range(n):
        for j in range(n):
            if j>=counter:
                tmp = _matrix[i][j]
                _matrix[i][j] = _matrix[j][i]
                _matrix[j][i] = tmp
        counter+=1
    return _matrix

def multiplyByDetInv(matrix, original_matrix):
    n = len(matrix)
    _matrix = zeroMatrix(n,n)
    det = detn_n(original_matrix)
    for i in range(n):
        for j in range(n):
            _matrix[i][j] = matrix[i][j]/det
    return _matrix
            
def matrixInverse(matrix):
    minor_matrix = minorsMatrix(matrix)
    cofactor_matrix = cofactorsMatrix(minor_matrix)
    adjugate_matrix = adjugateMatrix(cofactor_matrix)
    inverse_matrix = multiplyByDetInv(adjugate_matrix, matrix)
    return inverse_matrix 

def matrixMultiply(a, b):
    ans = list()
    a_rows_number = len(a)
    a_columns_number = len(a[0])
    b_columns_number = len(b[0])
    for i in range(a_rows_number):
        row_mult = list()
        for k in range(b_columns_number):
            sum = 0
            for j in range(a_columns_number):
                sum+=a[i][j]*b[j][k]
            row_mult.append(sum)
        ans.append(row_mult)
    return ans

def solveXx(a_h, b):
    a_h_inverse = matrixInverse(a_h)
    return matrixMultiply(a_h_inverse, b)

def matrixMinus(a, b):
    row_n = len(a)
    column_n = len(a[0])
    ans = zeroMatrix(row_n,column_n)
    for i in range(row_n):
        for j in range(column_n):
            ans[i][j] = a[i][j]-b[i][j]
    return ans

def residualVector(b, a_h, x):
    a_h_mult_x = matrixMultiply(a_h,x)
    return matrixMinus(b, a_h_mult_x)

def residualVectorNorm(vector):
    sum = 0
    n = len(vector)
    for i in range(n):
        sum+=(vector[i][0])**2
    return math.sqrt(sum)

# ---------- q1 ----------
samples = readSamplesFromFile("linear_solve.data")
n = len(samples)
for i in range(n):
    A = samples[i][0]
    H = samples[i][1]
    b = samples[i][2]
    print("-------------------- Sample " + str(i+1) + "--------------------")
    # ---------- q2 ----------
    A_det = detn_n(A)
    H_det = detn_n(H)
    print("det(A)=" + str(A_det))
    print("det(H)=" + str(H_det))
    if A_det!=0 and H_det!=0:
        # ---------- q3 ----------
        A_inverse = matrixInverse(A)
        H_inverse = matrixInverse(H)
        print("A*-1=" + str(A_inverse))
        print("H*-1=" + str(H_inverse))

        # ---------- q4 ----------
        x1 = solveXx(A, b)
        x2 = solveXx(H, b)
        print("Ax=b => x=" + str(x1))
        print("Hx=b => x=" + str(x2))

        # ---------- q5 ----------
        v1 = residualVector(b, A, x1)
        v2 = residualVector(b, H, x2)
        print("b-Ax=" + str(v1))
        print("b-Hx=" + str(v2))

        # ---------- q6 ----------
        n1 = residualVectorNorm(v1)
        n2 = residualVectorNorm(v2)
        print("||b-Ax||=" + str(n1))
        print("||b-Hx||=" + str(n2))
