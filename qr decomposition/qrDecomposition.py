def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()

    sample_counter = int(file_lines[0])
    samples = list()

    n = int(file_lines[1])
    m = int(file_lines[2])
    index = 3
    for i in range(sample_counter):
        sample = list()

        # initializing a
        a = list()
        j_index = 0
        # add m empty columns
        for j_index in range(m):
            a.append(list())

        # filling a
        j_index = 0
        for index in range(n*m):
            if j_index==m:
                j_index = 0
            a[j_index].append(int(file_lines[index]))
            j_index+=1
        sample.append(a)

        # initializing and filling y
        y = list()
        i_index = 0
        for i_index in range(n):
            y.append(int(file_lines([index])))
            index+=1
        sample.append(y)

        # adding first sample :[a,y]
        samples.append(sample)

        n = int(file_lines[index])
        m = int(file_lines[index+1])
        index = index+2

    return samples

