n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [ [] for _ in range(n+1)]
for u, v in edges :
    graph[u].append(v)
    graph[v].append(u)

def dfs(start) :
    global cnt
    cnt += 1
    visited[start] = 1
    for node in graph[start] :
        if not visited[node] :
            dfs(node)
# Please write your code here.
    cnt += 1

visited = [[0 for _ in range(m+1)] for _ in range(m|1)] 
cnt = 0 
dfs(0)
print(cnt)