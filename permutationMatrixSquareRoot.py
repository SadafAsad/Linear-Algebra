def zeroMatrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()
    sample_counter = int(file_lines[0])
    for i in range(sample_counter):
        n = int(file_lines[2*i])
        one_s_str = file_lines[(2*i)+1].split()
        cycles_list = list()
        cycle = list()
        here = 0
        for r in range(n):
            x = one_s_str[r]
            cycle.append(x)
            if x==r:
                cycles_list.append(cycle)
                cycle = list()
                here = 1
            else:
                here = 0
        if here==0:
            cycles_list.append(cycle)
    return cycles_list

def hasSqr(matrix_str):
    length = len(matrix_str)
    if length==1:
        if len(matrix_str[0])%2==1:
            return 1
        return 0
    elif length%2==0:
        for cycle in range(length):
            if len(matrix_str[cycle])%2==1:
                return 0
        return 1
    else:
        odd_length_num = 0
        even_length_num = 0
        for cycle in range(length):
            if len(matrix_str[cycle])%2==1:
                odd_length_num+=1
            else:
                even_length_num+=1
        if odd_length_num%2==1:
            if even_length_num%2==0:
                return 1
        return 0

samples = readDataFromFile("data.in")
counter = 1
for sample in samples:
    if not hasSqr(sample):
        print("Sample " + str(counter) + "impossible")
    counter+=1