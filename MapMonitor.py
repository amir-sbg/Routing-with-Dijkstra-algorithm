import matplotlib.pyplot as plt
import numpy as np
class MapMonitor:
    def __init__(self,distance,previous,graph,dest):
        self.distance =dict(distance)
        self.previous = dict(previous)
        self.graph = dict(graph)
        self.dest=dest

    def ploter(self):
        pointsX=[]
        pointsY=[]

        for node in self.graph.keys():
            pointsY.append(self.graph[node][0][0])
            pointsX.append(self.graph[node][0][1])

        pointsX=np.array(pointsX)
        pointsY=np.array(pointsY)
        plt.scatter(pointsX,pointsY)
        for node in self.graph.keys():
            for edge in self.graph[node][1]:
                plt.plot([self.graph[node][0][1],self.graph[edge[0]][0][1]],[self.graph[node][0][0],self.graph[edge[0]][0][0]],'grey')
        destCP = self.dest
        while True:
            try:
                self.previous[destCP]
                plt.plot([self.graph[destCP][0][1], self.graph[self.previous[destCP]][0][1]],
                         [self.graph[destCP][0][0], self.graph[self.previous[destCP]][0][0]], 'red')
            except KeyError:
                break
            destCP = self.previous[destCP]
        plt.show()



