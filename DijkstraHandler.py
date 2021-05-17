import math
import TimeManager
import MinHeap


class DijkstraHandler:
    def __init__(self, graph):
        self.graph = graph
        self.dstnc = {}
        self.prvus = {}
        self.timeM = TimeManager.TimeManager(self.graph)

    def dijkstra(self, start, dest, time):
        self.timeM.managingTime(time)
        nodes = dict(self.graph).keys()
        distance = {}
        previous = {}
        distanceDetails = {}

        for i in dict(self.graph).keys():
            distance[i] = float("inf")
            previous[i] = None

        distance[start] = 0

        notExplored = set(nodes)
        minHeap = MinHeap.MinHeap(notExplored)
        while len(notExplored) > 0:

            current_Node = self.min_in_heap(notExplored, distance)

            currentNode = self.minimum_distance(distance, notExplored)
            if (currentNode == 0):
                break
            notExplored.remove(currentNode)

            if distance[currentNode] == float('inf'):
                break

            neighborhood = (dict(self.graph)[currentNode])[1]
            for vertex in neighborhood:
                #
                self.timeM.graphRestarter()

                # for i in dict(self.graph).keys():
                #     print(i, "  :::  ", self.graph[i])
                self.timeM.managingTime(distance[currentNode] + time)
                wheight = distance[currentNode] + (self.dist_between(currentNode, vertex) * (1 + (0.3 * vertex[1])))

                if wheight < distance[vertex[0]]:
                    distance[vertex[0]] = wheight
                    previous[vertex[0]] = currentNode
        destCP = dest
        print(" ")
        while True:
            print(destCP, end=" <- ")

            try:
                previous[destCP]
                # self.traffic_handler(destCP, previous[destCP])



            except KeyError:
                break

            destCP = previous[destCP]
        print(" ")
        # for i in distance.keys():
        #     print(i," : ",distance[i]*120)

        self.prvus = previous
        self.dstnc = distance
        #
        self.timeM.newRequest(distance, previous, dest, time)
        return previous

    def dist_between(self, i, vertex):
        return math.sqrt(
            math.pow(((((dict(self.graph))[i])[0])[0]) - ((((dict(self.graph))[vertex[0]])[0])[0]), 2) +
            math.pow(((((dict(self.graph))[i])[0])[1]) - ((((dict(self.graph))[vertex[0]])[0])[1]), 2))

    def min_in_heap(self, notExplored, distance):
        minHeap = MinHeap.MinHeap(distance.values())
        minimumDist = minHeap.getAndDeleteMinimum()
        for i in notExplored:
            if distance[i] == minimumDist:
                return i

    def traffic_handler(self, currentNode, vertex):
        for i in self.graph[currentNode][1]:
            if i[0] == vertex:
                i[1] += 1
                break
        for i in self.graph[vertex][1]:
            if i[0] == currentNode:
                i[1] += 1
                break

    def getDistance(self):
        return self.dstnc

    def getPrevious(self):
        return self.prvus

    def minimum_distance(self, dist, notExplored):

        maxTemp = float('inf')
        tmp = 0
        for i in set(notExplored):

            if dist[i] < maxTemp:
                maxTemp = dist[i]
                tmp = i
        return tmp
