N = int(input())
l = []
for i in range(N):
    b=input().split()
    if b[0]=='insert':
        l.insert(int(b[1]),int(b[2]))
    elif b[0]=='print':
        print(l)
    elif b[0]=='remove':
        l.remove(int(b[1]))
    elif b[0]=='append':
        l.append(int(b[1]))
    elif b[0]=='sort':
        l.sort()
    elif b[0]=='reverse':
        l.reverse()
    else: l.pop()