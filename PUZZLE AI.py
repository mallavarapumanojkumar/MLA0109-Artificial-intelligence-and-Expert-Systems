from heapq import heappush, heappop

goal="123456780"

def h(s):
    return sum(abs(i//3-goal.index(c)//3)+abs(i%3-goal.index(c)%3)
               for i,c in enumerate(s) if c!="0")

def moves(s):
    i=s.index("0"); r,c=divmod(i,3); out=[]
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            j=nr*3+nc; lst=list(s)
            lst[i],lst[j]=lst[j],lst[i]
            out.append("".join(lst))
    return out

def solve(start):
    pq=[(h(start),start,[])] ; seen=set()
    while pq:
        _,s,path=heappop(pq)
        if s==goal: return path+[s]
        if s in seen: continue
        seen.add(s)
        for m in moves(s):
            heappush(pq,(len(path)+h(m),m,path+[s]))

start="283164705"
res=solve(start)

print("Solution Steps:\n")
for s in res:
    print(s[0:3], s[3:6], s[6:9], "\n")
