from csv import reader
import math
import random

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

def separating(d, points):
    group1 = list()
    group2 = list()
    while len(points)!=0:
        point = points[0]
        distances = euclideanDistance(point, points)
        i = len(points)-1
        flag = 0
        while i>0:
            if distances[i]<=d:
                flag = 1
                group1.append(points[i])
                points.pop(i)
            i-=1
        if flag:
            group1.append(points[0])
        else:
            group2.append(points[0])
        points.pop(0)
    return (group1, group2)

def d(group1, group2):
    flag = 0
    for p in group1:
        distances_from_p = euclideanDistance(p, group2)
        if flag:
            local_min = min(distances_from_p)
            if local_min<=global_min:
                global_min = local_min
        else:
            global_min = min(distances_from_p)
            flag = 1

# points = readDataFile('dataset.csv')
# p_num = len(points)

# i1 = random.randint(0, p_num-1)
# i2 = random.randint(0, p_num-1)
# while i1==i2:
#     i2 = random.randint(0, p_num-1)
# center1 = points[i1]
# center2 = points[i2]

# while(True):
#     center1_euclidean_distances = euclideanDistance(center1, points)
#     center2_euclidean_distances = euclideanDistance(center2, points)
#     cluster1 = list()
#     cluster2 = list()
#     center_avg1 = [0,0,0,0]
#     center_avg2 = [0,0,0,0]
#     # d = euclideanDistance(center1, [center2])
#     for i in range(p_num):
#         if center1_euclidean_distances[i]<=center2_euclidean_distances[i]:
#             cluster1.append(points[i])
#             center_avg1[0]+=float(points[i][0])
#             center_avg1[1]+=float(points[i][1])
#             center_avg1[2]+=float(points[i][2])
#             center_avg1[3]+=float(points[i][3])
#             center_avg1[0]/=2
#             center_avg1[1]/=2
#             center_avg1[2]/=2
#             center_avg1[3]/=2
#         else:
#             cluster2.append(points[i])
#             center_avg2[0]+=float(points[i][0])
#             center_avg2[1]+=float(points[i][1])
#             center_avg2[2]+=float(points[i][2])
#             center_avg2[3]+=float(points[i][3])
#             center_avg2[0]/=2
#             center_avg2[1]/=2
#             center_avg2[2]/=2
#             center_avg2[3]/=2

#     if center1==center_avg1 and center2==center_avg2:
#         break
#     center1 = center_avg1
#     center2 = center_avg2

# print(len(cluster1))
# print(len(cluster2))
