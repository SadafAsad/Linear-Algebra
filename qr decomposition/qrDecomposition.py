import math

def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()

    sample_counter = int(file_lines[0])
    samples = list()

    n = int(file_lines[1])
    m = int(file_lines[2])
    index = 3
    i_sample = 0
    while(True):
        sample = list()

        # initializing a
        a = list()
        j_index = 0
        # add m empty columns
        for j_index in range(m):
            a.append(list())

        # filling a
        j_index = 0
        element_counter = 0
        for element_counter in range(n*m):
            if j_index==m:
                j_index = 0
            a[j_index].append(float(file_lines[index]))
            index+=1
            j_index+=1
        sample.append(a)

        # initializing and filling y
        y = list()
        i_index = 0
        for i_index in range(n):
            y.append(float(file_lines[index]))
            index+=1
        sample.append(y)

        # adding first sample :[a,y]
        samples.append(sample)
        i_sample+=1

        # end of file
        if i_sample==sample_counter:
            break

        n = int(file_lines[index])
        m = int(file_lines[index+1])
        index = index+2

    return samples

def column_norm(cl):
    summ = 0
    for i in cl:
        summ = summ + (i*2)
    return math.sqrt(summ)