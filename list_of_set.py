s1= set(map(int, input("Enter the elements of first set: ").split()))
s2= set(map(int, input("Enter the elements of second set: ").split()))
l=[s1,s2]
sups=s1.issuperset(s2)
subs=s1.issubset(s2)
diff=s1.difference(s2)
inter=s1.intersection(s2)
uni=s1.union(s2)
print(l)
print(subs)
print(sups)
print(diff)
print(inter)
print(uni)