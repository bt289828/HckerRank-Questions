N,M = input().split()
N=int(N)
M=int(M)
p=".|."
s='WELCOME'
for i in range(1, N, 2): 
    print((p*i).center(M, '-'))
print(s.center(M, '-'))
for i in range(N-2, -1, -2): 
    print((p*i).center(M, '-'))