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

# returns disjoint cycles if matrix p
def decompositionToDisjointCycles(n, data_str):
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

# number of even cycles of the same length most be even (%2==0) 
def hasSquareRoot(cycle_list):
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

# even  : list1, list2 cycle of the same even length
# odd   : list1, list2 both are the same odd cycle
# even  : (a1,a2)(a3,a4) --> (a1,a3,a2,a4)
# odd   : (a1,a2,a3,a4,a5) --> (a1,a4,a2,a5,a3) 
def cycleSquareRoot(list1, list2):
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

# returns a tuple of even cycles list and odd cycles list
def separateOddEvenCycle(cycle_list):
    odd_cycles = list()
    even_cycles = list()
    for cycle in cycle_list:
        if len(cycle)%2==0:
            even_cycles.append(cycle)
        else:
            odd_cycles.append(cycle)
    return (even_cycles, odd_cycles)

# returns square roots of odd cycles
def oddCycleSquareRoot(odd_cycles):
    ans = list()
    for cycle in odd_cycles:
        n = len(cycle)
        middle = n//2
        first = list()
        for i in range(middle+1):
            first.append(cycle[i])
        second = list()
        count = n-middle-1
        for r in range(count):
            second.append(cycle[middle+1])
            middle+=1
        ans.append(cycleSquareRoot(first, second))
    return ans

# returns square roots of even cycles of the same length
def evenCycleSquareRoot(even_cycles):
    ans = list()
    n = len(even_cycles)
    i = 0
    while i<n:
        cycle_len = len(even_cycles[i])
        r = i+1
        while r<n:
            if len(even_cycles[r])==cycle_len:
                new_cycle = cycleSquareRoot(even_cycles[i], even_cycles[r])
                ans.append(new_cycle)
                even_cycles.pop(r)
                even_cycles.pop(i)
                n = len(even_cycles)
                break
            r+=1
        i = 0
    return ans

# odd squares and even squares
def cyclesRoots(cycle_list):
    even_cycles, odd_cycles = separateOddEvenCycle(cycle_list)
    matrix = list()
    if len(odd_cycles)!=0:
        f_odd = oddCycleSquareRoot(odd_cycles)
    else:
        f_odd = []
    if len(even_cycles)!=0:
        f_even = evenCycleSquareRoot(even_cycles)
    else:
        f_even = []
    
    for i in f_odd:
        matrix.append(i)
    for i in f_even:
        matrix.append(i)
    return matrix

def root(p, cycles_root):
    root = list()
    for x in p:
        root.append(0)

    for cycle in cycles_root:
        cycle_len = len(cycle)
        for i in range(cycle_len):
            if i==cycle_len-1:
                x = cycle[i]
                y = cycle[0]
                root[y] = p[x]
            else:
                x = cycle[i]
                y = cycle[i+1]
                root[y] = p[x]
    return root

def permutationSquareRoot(file_name):
    # reading p matrices
    samples = readDataFromFile(file_name)
    samples_temp = readDataFromFile(file_name)

    # finding their disjoint cycles
    cycles = list()
    for sample in samples_temp:
        cycles.append(decompositionToDisjointCycles(len(sample), sample))
    
    # checking if they have square roots
    n = len(cycles)
    for i in range(n):
        if i==15:
            break
        if not hasSquareRoot(cycles[i]):
            print("Sample " + str(i+1) + " impossible")
        else:
            # finding their root
            cycles_roots = cyclesRoots(cycles[i])
            root_ans = root(samples[i], cycles_roots)
            print("Sample "+ str(i+1) + " A=" + str(root_ans))
        i+=1

permutationSquareRoot("data.in")
