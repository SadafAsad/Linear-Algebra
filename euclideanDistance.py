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
        x2 = ( float(point[0])-float(each_point[0]) )**2
        y2 = ( float(point[1])-float(each_point[1]) )**2
        z2 = ( float(point[2])-float(each_point[2]) )**2
        k2 = ( float(point[3])-float(each_point[3]) )**2
        distance = math.sqrt( x2+y2+z2+k2 )
        distances.append(distance)
    return distances

def tmpCluster(cluster):
    tmp_cluster = list()
    for c in cluster:
        tmp_cluster.append(c)
    return tmp_cluster

points = readDataFile('dataset.csv')
p_num = len(points)
center1 = points[0]
center2 = points[1]

cluster1 = list()
cluster2 = list()

bag = [[0],[0],[0],[0]]

while(True):
    center1_euclidean_distances = euclideanDistance(center1, points)
    center2_euclidean_distances = euclideanDistance(center2, points)
    center_avg1 = 0
    center_avg2 = 0
    for i in range(p_num):
        if center1_euclidean_distances[i]<=center2_euclidean_distances[i]:
            cluster1.append(points[i])
            center_avg1+=float(points[i])
            center_avg1/=2
        else:
            cluster2.append(points[i])
            center_avg2+=float(points[i])
            center_avg2/=2

    cluster1_len = len(cluster1)
    center1 = cluster1[cluster1_len//2]
    cluster2_len = len(cluster2)
    center2 = cluster2[cluster2_len//2]

    # 0 va 1 jadid ha
    bag[0] = cluster1
    bag[1] = cluster2
    if bag[0]==bag[2] and bag[1]==bag[3]:
        break
    bag[2] = tmpCluster(cluster1)
    bag[3] = tmpCluster(cluster2)

print(d)