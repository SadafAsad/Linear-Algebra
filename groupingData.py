from csv import reader
import math

def readDataFile(file_name):
    points = list()
    with open(file_name, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            points.append(row)
    return points

def euclideanDistance(point, points):
    distances = list()
    for each_point in points:
        x2 = ( int(point[0])-int(each_point[0]) )**2
        y2 = ( int(point[1])-int(each_point[1]) )**2
        z2 = ( int(point[2])-int(each_point[2]) )**2
        k2 = ( int(point[3])-int(each_point[3]) )**2
        distance = math.sqrt( x2+y2+z2+k2 )
        distances.append(distance)
    return distances

def norm(point):
    x2 = int(point[0])**2
    y2 = int(point[1])**2
    z2 = int(point[2])**2
    k2 = int(point[3])**2
    return math.sqrt( x2+y2+z2+k2 )


points = readDataFile('dataset.csv')