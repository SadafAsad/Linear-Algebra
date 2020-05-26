from csv import reader

def readDataFile(file_name):
    points = list()
    with open(file_name, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            points.append(row)




points = readDataFile('dataset.csv')