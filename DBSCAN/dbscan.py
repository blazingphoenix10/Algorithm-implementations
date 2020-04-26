import matplotlib.pyplot as plt
import numpy as np

def DBSCAN(fname,D,eps,MinPts):
    labels=[0]*len(D) # Intitially assign labels of all points as zero
    C=0   # C is the ID of the current cluster
    temp=0  # temp variable for calculating number of core points
    for P in range(0,len(D)):
        if (labels[P]!=0):
           continue
        NeighborPts=regionQuery(D,P,eps)
        if len(NeighborPts)<MinPts:
            labels[P]=-1 # labelled as noise
        else:
            C+=1  # else labelled as new cluster
            temp+=growCluster(D,labels,P,NeighborPts,C,eps,MinPts)
    label_color={}
    colors=['r','g','b','y','m','y','k',(0.5,0.3,0.1),(0.1,0.2,0.5),(0.3,0.4,0.9),(0.6,0.7,0.8),(0.2,0.6,0.3),(0.1,0.5,0.9),(1,0,0.5),(1,1,0.1),'w']
    unique_labels=list(set(labels))
    for i in range(len(unique_labels)):
        label_color[unique_labels[i]]=colors[i]
    for i in range(len(D)):
        plt.scatter(D[i][0],D[i][1],c=label_color[labels[i]])
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
    plt.title("Dataset : "+str(fname)+" MinPts : "+str(MinPts)+" Epsilon : "+str(eps))
    print(" The number of noise points are : ",labels.count(-1),"\n","The number of core points are : ",temp+C,"\n","The number of border points are : ",len(D)-(temp+C)-labels.count(-1))
    return(plt.show())

def growCluster(D,labels,P,NeighborPts,C,eps,MinPts):
    '''
      `D`      - The dataset (a list of vectors)
      `labels` - List storing the cluster labels for all dataset points
      `P`      - Index of the seed point for this new cluster
      `NeighborPts` - All of the neighbors of `P`
      `C`      - The label for this new cluster.
      `eps`    - Threshold distance
      `MinPts` - Minimum required number of neighbors
    '''
    labels[P]=C # assigning label to core pt
    sum_core_pts=0  # it's sum of core pts in one iteration

    i=0
    while i<len(NeighborPts): #For FIFO queue
        Pn=NeighborPts[i]
        if labels[Pn]==-1: # NOTE: noise pts are revisited none other pts are
           labels[Pn]=C
        elif labels[Pn]==0:
            labels[Pn]=C
            PnNeighborPts=regionQuery(D,Pn,eps)
            if len(PnNeighborPts)>=MinPts:
                sum_core_pts+=1
                NeighborPts=NeighborPts+PnNeighborPts
        i+=1
    return(sum_core_pts)

def regionQuery(D,P,eps):
    neighbors=[]
    for Pn in range(0,len(D)):
        if np.linalg.norm(D[P]-D[Pn])<eps: # finding if point is withing eps radius
           neighbors.append(Pn)
    return(neighbors)

fname=input("Please enter name of dataset - fullmoon or outlier: ")
min_points=input("Please enter number of minimum points for core point: ")
epsilon=input("Please enter epsilon value: ")

x,y=[],[]
with open(fname+".txt") as fh:
    for line in fh:
        pt=line.split(',')
        x.append(float(pt[0]))
        y.append(float(pt[1]))

d=np.vstack((x,y)).T
DBSCAN(fname,d,float(epsilon),int(min_points))
