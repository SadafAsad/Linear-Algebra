import math
import csv
import random

def readDataFile(file_name):
    points = list()
    with open(file_name, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            points.append(row)
    return points
    
def norm(point):
    x2 = float(point[0])**2
    y2 = float(point[1])**2
    z2 = float(point[2])**2
    k2 = float(point[3])**2
    return math.sqrt( x2+y2+z2+k2 )

def dotProduct(point1, point2):
    x = float(point1[0])*float(point2[0])
    y = float(point1[1])*float(point2[1])
    z = float(point1[2])*float(point2[2])
    k = float(point1[3])*float(point2[3])
    return x+y+z+k

def cosineSimilarity(point, points):
    cosine_similarities = list()
    for each_point in points:
        dot = dotProduct(point, each_point)
        norm1 = norm(point)
        norm2 = norm(each_point)
        cosine_similarities.append(dot/(norm1*norm2))
    return cosine_similarities

def difference(point, points):
    differences = list()
    for each_point in points:
        x = abs(point-each_point)
        differences.append(x)
    return differences

def kMeans(points):
    p_num = len(points)

    i1 = random.randint(0, p_num-1)
    i2 = random.randint(0, p_num-1)
    while i1==i2:
        i2 = random.randint(0, p_num-1)
    center1 = points[i1]
    center2 = points[i2]

    while(True):
        center1_cosine_similarities = cosineSimilarity(center1, points)
        center2_cosine_similarities = cosineSimilarity(center2, points)
        cluster1 = list()
        cluster2 = list()
        center_avg1 = [0,0,0,0]
        center_avg2 = [0,0,0,0]
        for i in range(p_num):
            if center1_cosine_similarities[i]<=center2_cosine_similarities[i]:
                cluster1.append(points[i])
                center_avg1[0]+=float(points[i][0])
                center_avg1[1]+=float(points[i][1])   
                center_avg1[2]+=float(points[i][2])
                center_avg1[3]+=float(points[i][3])
                center_avg1[0]/=2
                center_avg1[1]/=2
                center_avg1[2]/=2
                center_avg1[3]/=2
            else:
                cluster2.append(points[i])
                center_avg2[0]+=float(points[i][0])
                center_avg2[1]+=float(points[i][1])
                center_avg2[2]+=float(points[i][2])
                center_avg2[3]+=float(points[i][3])
                center_avg2[0]/=2
                center_avg2[1]/=2
                center_avg2[2]/=2
                center_avg2[3]/=2

        if center1==center_avg1 and center2==center_avg2:
            break
        center1 = center_avg1
        center2 = center_avg2

    return (cluster1, cluster2)

def calculateS(cluster1, cluster2):
    flag = 0
    for p in cluster1:
        similarities_with_p = cosineSimilarity(p, cluster2)
        if flag:
            local_min = min(similarities_with_p)
            if local_min<=global_min:
                global_min = local_min
        else:
            global_min = min(similarities_with_p)
            flag = 1
    return global_min



points = readDataFile('dataset.csv')
cluster1, cluster2 = kMeans(points)
s = calculateS(cluster1, cluster2)
print(s)

