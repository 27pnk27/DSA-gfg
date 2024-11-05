import heapq as hp
def bfs_single_source(graph,source):
    n=len(graph)
    visited=[False]*n
    visited[source]=True
    q=[source]
    res=[]
    while q:
        curr=q.pop(0)
        res.append(curr)
        for i in graph[curr]:
            if(visited[i]==False):
                q.append(i)
                visited[i]=True

    return res

print(bfs_single_source([[2,3],[2],[0,1,4],[0],[2]],3))

def dfs_single_source_iter(graph,source):
    n=len(graph)
    stack=[source]
    visited=[False]*n
    visited[source]=True
    res=[source]
    while stack:
        for i in graph[stack[-1]]:
            #status=0
            if(visited[i]==False):
                status=1
                stack.append(i)
                res.append(i)
                visited[i]=True
                break
        else:
            stack.pop()

    return res

print(dfs_single_source_iter([[2,4],[3,4],[0,4,5],[0,1],[0,1,2,5],[2,4]],0))

def dfs_single_source_recur(graph,source,visited=None,res=None):
    n=len(graph)
    if not visited and not res:
        visited,res=[False]*n,[]

    visited[source]=True
    res.append(source)
    for i in graph[source]:
        if not visited[i]:
            dfs_single_source_recur(graph3,i,visited,res)

    return res
graph3=[[1],[2,3],[3],[4],[]]

print('D',dfs_single_source_recur(graph3,0))


def bfs_disconnected_directed(graph):
    n=len(graph)
    visited=[True]*n
    res=[]
    q=[]
    for i in graph:
        for j in i:
            visited[j]=False

    for i in range(n):
        if(visited[i]):
            q.append(i)
            #res.append(i)

    while q:
        curr=q.pop(0)
        res.append(curr)
        for i in graph[curr]:
            if(not visited[i]):
                q.append(i)
                visited[i]=True

    return res

print(bfs_disconnected_directed([[1],[3],[4],[6],[3,5],[6],[]]))

def detect_cycle_directed(graph):
    n = len(graph)
    indegree = [0] * n
    for i in graph:
        for j in i:
            indegree[j]+=1


    q=[]
    for i in range(n):
        if(indegree[i]==0):
            q.append(i)

    count = 0
    while q:
        curr=q.pop(0)
        count+=1
        for i in graph[curr]:
            indegree[i]-=1
            if(indegree[i]==0):
                q.append(i)

    if(count==n):
        return False

    return True



    #return indegree

print(detect_cycle_directed([[1],[3],[4],[6],[3,5],[6],[]]))
print(detect_cycle_directed([[1],[3],[4],[6],[3],[4],[5]]))

def detect_cycle_undirected(graph):
    n = len(graph)
    visited = [False] * n
    q = [(0, -1)]  # (node, parent)
    visited[0] = True

    while q:
        node, parent = q.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, node))
            elif neighbor != parent:
                # Cycle detected if we visit a visited node that isn't the parent
                return True

    return False

# Example usage
print(detect_cycle_undirected([[1], [0, 3], [4], [1, 4, 6], [2, 3, 5], [4, 6], [3, 5]]))

def topological_sorting_bfs(graph):
    n=len(graph)
    indegree=[0]*n

    for i in graph:
        for j in i:
            indegree[j]+=1
    #print(indegree)
    q=[]
    for i in range(n):
        if(indegree[i]==0):
            q.append(i)

    res=[]
    while q:
        #print('before',q)
        curr=q.pop(0)
        res.append(curr)
        for i in graph[curr]:
            indegree[i]-=1
            if(indegree[i]==0):
                q.append(i)
        #print('sub',q)

    return res

print(topological_sorting_bfs([[1],[3],[4],[6],[3,5],[6],[]]))
#print(topological_sorting_bfs([[1],[3],[4],[6],[3],[4],[5]]))

def topological_sorting_dfs(graph):
    n=len(graph)
    visited=[False]*n
    stack=[]

    def dfs(node):
        visited[node]=True
        for i in graph[node]:
            if not visited[i]:
                dfs(i)
        stack.append(node)

    for i in range(n):
        if(not visited[i]):
            dfs(i)

    return stack[::-1]

print(topological_sorting_dfs([[1],[3],[4],[6],[3,5],[6],[]]))

def distance(graph,source):
    n=len(graph)
    dist=[float('inf')]*n
    dist[source]=0
    q=[source]
    visited=[False]*n
    visited[source]=True
    while q:
        curr=q.pop(0)
        for i in graph[curr]:
            if not visited[i]:
                dist[i]=dist[curr]+1
                visited[i]=True
                q.append(i)

    return dist

print(distance([[1],[3],[4],[6],[3,5],[6],[]],2))


def max_addable_edges(graph):
    n=len(graph)
    topo=topological_sorting_dfs(graph)
    for i in range(n):
        x=topo.index(i)
        graph[i]=topo[x+1:]

    return topo

print((max_addable_edges([[],[],[3],[1],[0,1],[0,2]])))

def shortest_path_WDAG(graph,source):
    n=len(graph)
    indegree=[0]*n
    dist=[float('inf')]*n
    for i in graph:
        for j in i:
            indegree[j[0]]+=1

    q=[]
    for i in range(n):
        if(indegree[i]==0):
            q.append(i)

    dist[source]=0
    while q:
        curr=q.pop(0)
        for i in graph[curr]:
            indegree[i[0]]-=1
            if(indegree[i[0]]==0):
                q.append(i[0])

            dist[i[0]]=min(dist[curr]+i[1],dist[i[0]])


    return dist




print((shortest_path_WDAG([[],[],[(3,1)],[(1,8)],[(0,1),(1,7),(2,3),(3,7)],[(0,2),(2,3)]],4)))


'''Spanning Tree - Weighted Acyclic Graph with n nodes and n-1 edges
                   Every node is reachable from every other node
                   
   Minimum Spanning Tree - Any tree with the least sum of edge weights'''

def prims(graph):
    n=len(graph)
    visited=set()
    mst=[[] for i in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            graph[i][j]=graph[i][j][::-1]
            y=list(graph[i][j])
            y.append(i)
            graph[i][j]=tuple(y)

    heap=[]
    for i in graph[0]:
        hp.heappush(heap,i)
    visited.add(0)
    while len(visited)<n:
        x=hp.heappop(heap)
        if x[1] in visited:
            continue
        mst[x[2]].append((x[1],x[0]))
        mst[x[1]].append((x[2],x[0]))
        visited.add(x[1])
        for i in graph[x[1]]:
            if i[1] not in visited:
                hp.heappush(heap,i)

    return mst

graph2=[[(1,2),(4,4),(3,1),(5,15)],[(0,2),(3,3),(2,3)],[(3,5),(1,3),(5,8)],[(4,9),(1,3),(2,5)],[(0,4),(3,9)],[(2,8),(0,15)]]

print(prims(graph2))

def dijkstra(graph,source):
    n=len(graph)
    dist=[float('inf')]*n
    dist[source]=0
    heap=[]
    hp.heappush(heap,(0,source))
    visited=set()
    while heap:
        curr_dist,vertex=hp.heappop(heap)
        if vertex in visited:
            continue
        visited.add(vertex)
        for i in graph[vertex]:
            if i[1] not in visited:
                new_dist=curr_dist+i[0]
                if new_dist<dist[i[1]]:
                    dist[i[1]]=new_dist
                    hp.heappush(heap,(new_dist,i[1]))

    return dist


print(dijkstra(graph2, 5))


def spanningTree(V, adj) -> int:
    visited = set()
    heap = []
    for i in adj:
        if (i[0] == 0):
            hp.heappush(heap, (i[2], i[1], i[0]))
        elif (i[1] == 0):
            hp.heappush(heap, (i[2], i[0], i[1]))

    visited.add(0)
    cost = 0

    while len(visited)<V:
        x = hp.heappop(heap)
        if x[1] in visited:
            continue
        visited.add(x[1])
        cost += x[0]
        for i in adj:
            if (i[0] == x[1] and i[1] not in visited):
                hp.heappush(heap, (i[2], i[1], i[0]))
            elif (i[1] == x[1] and i[0] not in visited):
                hp.heappush(heap, (i[2], i[0], i[1]))

    return cost

print(spanningTree(3,[[0,1,5],[1,2,3],[0,2,1]]))

def transpose(graph):
    n=len(graph)
    grapht=[[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            grapht[j].append(i)

    return grapht

graph4=[[1],[3],[3,4],[5],[3],[]]

#print(transpose(graph4))

def kosaraju_dfs_util(graph,stack=None,visited=None):
    n=len(graph)
    if not stack and not visited:
        stack,visited,instack=[],[False]*n,[False]*n
    def dfs(graph,source):
        visited[source]=True
        for i in graph[source]:
            if not visited[i]:
                dfs(graph,i)
        if not instack[source]:
            stack.append(source)
            instack[source]=True

    for i in range(n):
        dfs(graph,i)

    return stack

graph5=[[1],[2],[3,4],[0],[5],[6],[4],[6,8],[]]
print(kosaraju_dfs_util(graph5))


def kosaraju_scc(graph):
    n=len(graph)
    res=[]
    stack=kosaraju_dfs_util(graph)
    visited=[False]*n
    new_graph=transpose(graph)
    scc=[]
    def dfs(graph,source,res=None):
        if not res:
            res=[]
        res.append(source)
        visited[source]=True
        for i in graph[source]:
            if not visited[i]:
                dfs(graph,i,res)

        return res

    while stack:
        x=stack.pop()
        if not visited[x]:
            scc.append(dfs(new_graph,x,res))

    return scc

print(kosaraju_scc(graph5))
















































































































































































