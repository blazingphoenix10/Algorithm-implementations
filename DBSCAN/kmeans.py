import matplotlib.pyplot as plt
import math
import random
import numpy as np

def distance(p1,p2): # Euclidean distance between 2 tuples
     return(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))

def sse(p1,p2): # Sum squared error between two points
     return((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def kmeans(k,x,y,fname): # input k : no. of clusters , x,y = x,y pts of dataset, fname : filename of dataset
    r,c=[],[] # r - random numbers list, c - centroid list
    for i in range(k):
        r.append(random.randint(0,len(x)))

    for i in range(len(r)):
        c.append((x[r[i]],y[r[i]]))

    for iter in range(101): # Defining k-means over 100 iterations

        dist=[[] for i in range(k)] # list of lists of distances of every centroid from every other pt
        for i in range(k):
            for j in range(len(x)):
                dist[i].append(distance(c[i],(x[j],y[j])))

        arr = np.array(dist) # making the distance array into a numpy array
        labels=np.argmin(arr,0) # compares every indices in the list of list and gets the label of cluster with min distance

        len_labels=[] # list containing number of pts belonging to each label
        for i in range(k):
            len_labels.append(list(labels).count(i))

        cluster_label_list=[[] for i in range(k)] # list of lists of indices belonging to each cluster

        for i in range(len(list(labels))):
            for j in range(k):
                if list(labels)[i]==j:
                    cluster_label_list[j].append(i)

        sum_clusters=[] # list of sums of x coordinates and y coordinates of all points belonging to a cluster
        for i in range(k):
            sum_x,sum_y=0,0
            for j in range(len(cluster_label_list[i])):
                sum_x+=x[cluster_label_list[i][j]]
                sum_y+=y[cluster_label_list[i][j]]
            sum_clusters.append((sum_x,sum_y))

        c.clear() # clearing c_old to update centroid to c_new
        for i in range(k):
            c.append((sum_clusters[i][0]/len_labels[i],sum_clusters[i][1]/len_labels[i]))

        if iter==100: # if iteration is 100, sum squared error is calculated
            sse=0
            print("The final centroids are : ",c)
            for i in range(k):
                print("The number of points in cluster ",i+1,"is : ",len(cluster_label_list[i])) # i is index, hence i+1
            for i in range(k):
                for j in range(len(cluster_label_list[i])):
                    sse+=((c[i][0]-x[cluster_label_list[i][j]])**2+(c[i][1]-y[cluster_label_list[i][j]])**2)
            print("The sum of squared error between the points and their respective centroids is : ",sse)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Dataset : "+str(fname)+" Number of clusters : "+str(k))
    plt.scatter(x,y,c=labels)
    plt.show()

k=input("Please enter number of clusters to be formed: ")
fname=input("Please enter name of dataset - fullmoon or outlier: ")

X,Y = [],[]
with open(fname+'.txt') as f:
	for l in f:
		row = l.split(',')
		X.append(float(row[0]))
		Y.append(float(row[1]))

kmeans(int(k),X,Y,fname)
