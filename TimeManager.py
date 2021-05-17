import threading
class TimeManager:
    def __init__(self,  graph):

        self.graph = dict(graph)
        self.trafficGraph={}
        for i in self.graph.keys():
                self.trafficGraph[i]={}
        for i in self.graph.keys():
                for j in self.graph[i][1]:
                    self.trafficGraph[i][j[0]]=[]

    def newRequest(self , distance, previous , dest,time ):

        destCP=dest
        while True:
            # print(destCP, end=" <- ")
            try:
                if previous[destCP]==None:
                    break
            except KeyError:
                break
    
            dict(self.trafficGraph[destCP])[dict(previous)[destCP]].append([distance[previous[destCP]]+time,distance[destCP]+time])
            dict(self.trafficGraph[dict(previous)[destCP]])[destCP].append([distance[previous[destCP]]+time,distance[destCP]+time])
            destCP=previous[destCP]

        for i in self.trafficGraph.keys():
            for j in dict(self.trafficGraph[i]).keys():
                 print(i, "_" ,j,"     :  ",self.trafficGraph[i][j])
                
    def managingTime(self,currTime):
        for node in self.trafficGraph.keys():
            for neib in dict(self.trafficGraph[node]).keys():
                for i in  self.trafficGraph[node][neib]:
                    if i[1]>=currTime and i[0]<= currTime:
                        self.trafficChanger(node,neib,'+')

    def trafficChanger(self,base,dest,char):
      for i in self.graph[base][1]:
          if i[0]==dest:
              if char  ==  '+' :
                  i[1]  +=  1
              if char  ==  '-' :
                  i[1]  -=  1
              break

    def graphRestarter(self):
        for  i in self.graph.keys():
            for j in self.graph[i][1]:
                j[1]=0

              
              
        