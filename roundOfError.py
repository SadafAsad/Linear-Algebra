def matrixInitializer(n, data):
    matrix = list()
    counter = 0
    for i in range(n):
        line_data = list()
        matrix.append(line_data)
        for r in range(n):
            line_data.append(data[counter])
            counter+=1
    return matrix

# def matrixDisplay(matrix):

def takingMatrixData():
    

ans = matrixInitializer(2, [1.0, 3.2, 2.1, 1.1])
print(ans)