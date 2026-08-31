import heapq 
class primMST:
    def prim(self,graph,start):
         visited={v: False for v in graph}
         mst_edges=[] 
         total_cost=0
         min_heap=[(0,start,None)]
         while min_heap and len(mst_edges) <len(graph)-1:
            weight ,u,parent =heapq.heappop(min_heap) 
            if visited[u]:  
                continue
            visited[u]=True
            if parent is not None: 
                mst_edges.append((parent,u,weight))
                total_cost+=weight
            for v,w in graph[u]:
                if not visited[v]: 
                    heapq.heappush(min_heap,(w,v,u))
         return mst_edges, total_cost

if __name__=='__main__':
    obj=primMST()
    graph_alpha={'A':[('B',4),('C',2)],'B':[('A',4),('D',3)],'C':[('A',2),('D',1)],'D':[('B',3),('C',1)]}
    mst_alpha,cost_alpha = obj.prim(graph_alpha,start='A')
    print("Prim's MST edges (alphabetic graph):",mst_alpha)
    print("Total minimum cost (alphabetic graph):",cost_alpha)
