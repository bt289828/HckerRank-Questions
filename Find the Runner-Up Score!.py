n = int(input())
arr = map(int, input().split())
ls=list(arr)
ls.sort()
p=max(ls)
while p in ls:
    ls.remove(p)
print(ls[-1])