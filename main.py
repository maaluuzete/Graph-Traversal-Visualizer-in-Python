import pygame,json,time
from graph import Graph

W,H=900,600
R=14

BG=(20,20,20)
ED=(120,120,120)
ND=(200,200,200)
VS=(0,200,0)
CR=(200,50,50)
SL=(50,150,250)
TX=(220,220,220)

MN=0
ME=1
MS=2

pygame.init()
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("BFS / DFS")
ft=pygame.font.SysFont("consolas",18)
ck=pygame.time.Clock()

g=Graph()
md=MN
sel=-1
st=-1

ord=[]
i=0
lst=0
dl=0.6
vis=set()
cur=-1

def getn(mx,my):
    for k,(x,y) in g.pos.items():
        if (mx-x)*(mx-x)+(my-y)*(my-y)<=R*R:
            return k
    return -1

def draw():
    sc.fill(BG)
    for u in g.adj:
        for v in g.adj[u]:
            if u<v:
                pygame.draw.line(sc,ED,g.pos[u],g.pos[v],2)
    for k,(x,y) in g.pos.items():
        c=ND
        if k in vis:c=VS
        if k==cur:c=CR
        if k==sel or k==st:c=SL
        pygame.draw.circle(sc,c,(x,y),R)
        t=ft.render(str(k),1,BG)
        sc.blit(t,(x-6,y-8))
    m=["NODE","EDGE","START"][md]
    s=f"MODO:{m} N-node E-edge S-start B-BFS D-DFS C-clear K-save L-load"
    sc.blit(ft.render(s,1,TX),(10,10))
    pygame.display.flip()

def step():
    global i,cur
    if i<len(ord):
        cur=ord[i]
        vis.add(cur)
        i+=1

run=1
while run:
    ck.tick(60)
    now=time.time()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=0
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_n:md=MN
            if e.key==pygame.K_e:md=ME;sel=-1
            if e.key==pygame.K_s:md=MS
            if e.key==pygame.K_c:
                ord=[];vis.clear();cur=-1;i=0
            if e.key==pygame.K_b and st!=-1:
                ord=g.bfs(st);vis.clear();cur=-1;i=0
            if e.key==pygame.K_d and st!=-1:
                ord=g.dfs(st);vis.clear();cur=-1;i=0
            if e.key==pygame.K_k:
                with open("graph.json","w") as f:
                    json.dump(g.to_json(),f)
            if e.key==pygame.K_l:
                with open("graph.json") as f:
                    g.from_json(json.load(f))
                ord=[];vis.clear();cur=-1;i=0;sel=-1;st=-1
        if e.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if md==MN:
                g.add_node(mx,my)
            elif md==ME:
                u=getn(mx,my)
                if u!=-1:
                    if sel==-1:sel=u
                    else:g.add_edge(sel,u);sel=-1
            elif md==MS:
                u=getn(mx,my)
                if u!=-1:st=u
    if ord and now-lst>dl:
        step()
        lst=now
    draw()

pygame.quit()
