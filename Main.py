import MapMonitor,MapManager,TimeManager,DijkstraHandler

mapM = MapManager.MapManager()
mapM.inputManager()
dijH=DijkstraHandler.DijkstraHandler(mapM.getGraph())

while True:
    inStr=input().split()
    dijH.dijkstra(float(inStr[1]) ,float(inStr[2]),float(inStr[0])/120 )
    monM=MapMonitor.MapMonitor(dijH.dstnc,dijH.prvus ,mapM.getGraph(),float(inStr[2]))
    monM.ploter()
    print( "Time :{}\n_____________________________________________________________________________\n ".format(dijH.dstnc[float(inStr[2])]*120))
