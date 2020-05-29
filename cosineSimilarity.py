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

# sqr( x**2 + y**2 + z**2 + k**2 ) 
def norm(point):
    x2 = float(point[0])**2
    y2 = float(point[1])**2
    z2 = float(point[2])**2
    k2 = float(point[3])**2
    return math.sqrt( x2+y2+z2+k2 )

# (x1 y1 z1 k1).(x2 y2 z2 k2)=(x1*x2 + y1*y2 + z1*z2 + k1*k2)
def dotProduct(point1, point2):
    x = float(point1[0])*float(point2[0])
    y = float(point1[1])*float(point2[1])
    z = float(point1[2])*float(point2[2])
    k = float(point1[3])*float(point2[3])
    return x+y+z+k

#    point1.point2
# ---------------------
#   |point1|*|point2| 
def cosineSimilarity(point, points):
    cosine_similarities = list()
    for each_point in points:
        dot = dotProduct(point, each_point)
        norm1 = norm(point)
        norm2 = norm(each_point)
        cosine_similarities.append(dot/(norm1*norm2))
    return cosine_similarities

# sqr( x**2 + y**2 + z**2 + k**2 )
def findStartDistance(points):
    distances = list()
    for point in points:
        d = math.sqrt(float(point[0])**2+float(point[1])**2+float(point[2])**2+float(point[3])**2)
        distances.append(d)
    return distances

def tmpCluster(cluster):
    tmp = list()
    for i in cluster:
        tmp.append(i)
    return tmp

def kMeans(points):
    p_num = len(points)

    # finding points' distances from start
    start_d = findStartDistance(points)
    # looking for the farthest point
    max_d = 0
    i_max = 0
    for i in range(p_num):
        if start_d[i]>=max_d:
            max_d = start_d[i]
            i_max = i
    # looking for the neartest point
    min_d = start_d[0]
    i_min = 0
    for i in range(p_num):
        if start_d[i]<=min_d:
            min_d = start_d[i]
            i_min = i
    # initializing first centeres
    # nearest and farthest points from start
    center1 = points[i_min]
    center2 = points[i_max]

    cluster1 = list()
    cluster2 = list()

    while(True):
        # saving last clusters
        tmp_cluster1 = tmpCluster(cluster1)
        tmp_cluster2 = tmpCluster(cluster2)

        # cosine similarities between points and center1 and center2
        center1_cosine_similarities = cosineSimilarity(center1, points)
        center2_cosine_similarities = cosineSimilarity(center2, points)
        
        cluster1 = list()
        cluster2 = list()
        center_avg1 = [0,0,0,0]
        center_avg2 = [0,0,0,0]

        # checks each point's similarities with center1 and center2
        # and each point belongs to the cluster more similar to
        # which means higher cosinus
        # at the same time calculates average of points of each cluster
        for i in range(p_num):
            if center1_cosine_similarities[i]>=center2_cosine_similarities[i]:
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

        # if the new clusters are the same as the old ones then our clusters are well separated
        if cluster1==tmp_cluster1 and cluster2==tmp_cluster2:
            break
        # if not centers are the calculated averages
        center1 = center_avg1
        center2 = center_avg2

    return (cluster1, cluster2)

# each points of cluster1 similarities with points of cluster2 are calculated
# and the maximum is s
# maximum cosinus means more similar/close
def calculateS(cluster1, cluster2):
    flag = 0
    for p in cluster1:
        similarities_with_p = cosineSimilarity(p, cluster2)
        if flag:
            local_max = max(similarities_with_p)
            if local_max>=global_max:
                global_max = local_max
        else:
            global_max = max(similarities_with_p)
            flag = 1
    return global_max

def conditionB(file_name):
    points = readDataFile(file_name)
    cluster1, cluster2 = kMeans(points)
    s = calculateS(cluster1, cluster2)

    # if it's in cluster1 --> 0
    # if it's in cluster2 --> 1
    file = open("conditionB.txt", "w")
    for p in points:
        if p in cluster1:
            file.write('0'+'\n')
        else:
            file.write('1'+'\n')
    file.write(str(s))
    file.close()


# with open('result3.csv', 'w',newline='') as write_file:
#     csv_writer = csv.writer( write_file )
#     for c in cluster1:
#         csv_writer.writerow(c)

# with open('result4.csv', 'w',newline='') as write_file:
#     csv_writer = csv.writer( write_file )
#     for c in cluster2:
#         csv_writer.writerow(c)   


conditionB('dataset.csv')

