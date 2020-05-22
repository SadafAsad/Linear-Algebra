import itertools

def zeroMatrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

def decomposition(n, data_str):
    cycles_list = list()
    for r in range(n):
        cycle = list()
        x = int(data_str[r])
        if x!=-1:
            data_str[r] = -1
            cycle.append(x)
            while x!=r:
                tmp = int(data_str[x])
                data_str[x] = -1
                x = tmp
                cycle.append(x)
            cycles_list.append(cycle)
    return cycles_list

def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()
    sample_counter = int(file_lines[0])
    samples = list()
    for i in range(sample_counter):
        index = (2*(i+1))-1
        one_s = file_lines[index+1].split()
        sample = list()
        for i in one_s:
            sample.append(int(i))
        samples.append(sample)
    return samples

def hasSqr(cycle_list):
    n = len(cycle_list)
    for i in range(n):
        x = len(cycle_list[i])
        counter = 0
        if x%2==0:
            for r in range(n):
                if x==len(cycle_list[r]):
                    counter+=1
        if counter%2==1:
            return 0
    return 1

def product(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    n1_index = 0
    n2_index = 0
    list3 = list()
    for i in range(n1+n2):
        if i%2==0:
            list3.append(list1[n1_index])
            n1_index+=1
        else:
            list3.append(list2[n2_index])
            n2_index+=1
    return list3

def separateOddEven(cycle_list):
    odd_cycles = list()
    even_cycles = list()
    for cycle in cycle_list:
        if len(cycle)%2==0:
            even_cycles.append(cycle)
        else:
            odd_cycles.append(cycle)
    return (even_cycles, odd_cycles)

def oddCycleComposition(odd_cycles):
    ans = list()
    for cycle in odd_cycles:
        n = len(cycle)
        middle = n/2
        first = list()
        for i in range(middle+1):
            first.append(cycle[i])
        second = list()
        count = n-middle-1
        for r in range(count):
            second.append(cycle[middle+1])
            middle+=1
        ans.append(product(first, second))
    return ans


samples = readDataFromFile("data.in")
cycles = list()
for sample in samples:
    cycles.append(decomposition(len(sample), sample))
counter = 1
for cycle in cycles:
    if not hasSqr(cycle):
        print("Sample " + str(counter) + " impossible")
    counter+=1