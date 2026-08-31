import heapq #heapq provides a priority queue (min-heap) for efficient

class primMST:
    def prim(self,graph,start):
         #initialise visited dictory for all verticies
         visited={v: False for v in graph}
         mst_edges=[] #store edges that form MST 
         total_cost=0
         #Heap stores(weight,current_vertex,parent_vertex)
         #start with chosen vertex (start),weight=0,parent=None
         min_heap=[(0,start,None)]
         #continue until MST has (n-1)edges
         while min_heap and len(mst_edges) <len(graph)-1:
            weight ,u,parent =heapq.heappop(min_heap) #pick smallest element
            if visited[u]: #skip if vertex already in MST 
                continue
                visited[u]=True #mark vertex as included in MST
                if parent is not None: #skip dummy edge for starting vertex
                    mst_edges.append((parent,u,weight))
                    total_cost+=weight
                    #Explore all neighbours of u
                    for v,w in graph[u]:
                        if not visited[v]: #only consider edges to vertices outside
                            heapq.heappush(min_heap,(w,v,u))
                return mst_edges, total_cost

if __name__=='__main__':
    obj=primMST()
    graph_alpha={'A':[('B',4),('C',2)],'B':[('A',4),('D',3)],'C':[('A',2),('D',1)],'D':[('B',3),('C',1)]}
    mst_alpha,cost_alpha=obj.prim(graph_alpha,start='A')
    print("Prim's MST edges (alphabetic graph):",mst_alpha)
    print("Total minimum cost (alphabetic graph):",cost_alpha)
