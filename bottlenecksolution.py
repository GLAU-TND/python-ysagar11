n=int(input())
h=list(map(int,input().split(',')))
print(max([h.count(i) for i in h]))
