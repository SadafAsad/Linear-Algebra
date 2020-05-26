import math
from csv import reader

def readDataFile(file_name):
    points = list()
    with open(file_name, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            points.append(row)
    return points
    
def norm(point):
    x2 = int(point[0])**2
    y2 = int(point[1])**2
    z2 = int(point[2])**2
    k2 = int(point[3])**2
    return math.sqrt( x2+y2+z2+k2 )

def dotProduct(point1, point2):
    x = int(point1[0])*int(point2[0])
    y = int(point1[1])*int(point2[1])
    z = int(point1[2])*int(point2[2])
    k = int(point1[3])*int(point2[3])
    return x+y+z+k

def cosineSimilarity(point, points):
    cosine_similarities = list()
    for each_point in points:
        dot = dotProduct(point, each_point)
        norm1 = norm(point)
        norm2 = norm(each_point)
        cosine_similarities.append(dot/(norm1*norm2))
    return cosine_similarities