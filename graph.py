import math
from collections import deque

MD=30

class Graph:
    def __init__(self):
        self.pos={}
        self.adj={}
        self.n=0

    def add_node(self,x,y):
        for px,py in self.pos.values():
            if math.hypot(px-x,py-y)<MD:
                return -1
        i=self.n
        self.pos[i]=(x,y)
        self.adj[i]=set()
        self.n+=1
        return i

    def add_edge(self,u,v):
        if u==v:return
        if v in self.adj[u]:return
        self.adj[u].add(v)
        self.adj[v].add(u)

    def bfs(self,s):
        vis=set()
        q=deque([s])
        ord=[]
        vis.add(s)
        while q:
            u=q.popleft()
            ord.append(u)
            for v in self.adj[u]:
                if v not in vis:
                    vis.add(v)
                    q.append(v)
        return ord

    def dfs(self,s):
        vis=set()
        ord=[]
        def go(u):
            vis.add(u)
            ord.append(u)
            for v in self.adj[u]:
                if v not in vis:
                    go(v)
        go(s)
        return ord

    def to_json(self):
        return {
            "pos":self.pos,
            "adj":{k:list(v) for k,v in self.adj.items()}
        }

    def from_json(self,d):
        self.pos={int(k):tuple(v) for k,v in d["pos"].items()}
        self.adj={int(k):set(v) for k,v in d["adj"].items()}
        self.n=len(self.pos)
