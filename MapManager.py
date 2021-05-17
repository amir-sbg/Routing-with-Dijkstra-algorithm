import TimeManager
import MapMonitor
import DijkstraHandler
class MapManager:

    def __init__(self):
        self.__nodes = {}
        self.__edges = {}
        self.__graph = {}

    def inputManager(self):
        inp = input().split()
        verticesNumber = int(inp[0])
        edgesNumber = int(inp[1])

        for i in range(verticesNumber):
            inp = input().split()
            self.__nodes[int(inp[0])] = [float(inp[1]), float(inp[2])]
            self.__edges[int(inp[0])]=[]

        for i in range(edgesNumber):
            inp = input().split()
            self.__edges[int(inp[0])].append([int(inp[1]),0])
            self.__edges[int(inp[1])].append([int(inp[0]),0])

        for i in self.__nodes.keys():
             self.__graph[i] = []
             self.__graph[i].append(self.__nodes[i])
             self.__graph[i].append(self.__edges[i])

    def getGraph(self):
        return self.__graph
    def getEdges(self):
        return self.__edges






