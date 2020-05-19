import itertools

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
    samples = list()
    for i in range(sample_counter):
        index = (2*(i+1))-1
        n = int(file_lines[index])
        one_s_str = file_lines[index+1].split()
        cycles_list = list()
        for r in range(n):
            cycle = list()
            x = int(one_s_str[r])
            while x!=r:
                cycle.append(x)
                x = int(one_s_str[x])
            cycle.append(x)
            cycles_list.append(cycle)

        for cycle in cycles_list:
            cycle.sort()

        cycles_list.sort()
        new_cycles_list = list(cycles_list for cycles_list,_ in itertools.groupby(cycles_list))

        samples.append(new_cycles_list)
    return samples

def hasSqr(cycle_list):
    odd_num = 0
    even_num = 0
    for cycle in cycle_list:
        if len(cycle)%2==0:
            even_num+=1
        else:
            odd_num+=1
    if even_num%2==0:
        if odd_num==0 or odd_num%2==1:
            return 1
    return 0

samples = readDataFromFile("data.in")
print(samples[0])
print(samples[5])
counter = 1
for sample in samples:
    if not hasSqr(sample):
        print("Sample " + str(counter) + " impossible")
    counter+=1