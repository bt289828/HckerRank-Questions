n=int(input())
if not(n%2==0):
   print("Weird")
elif n%2==0 and n in range(2,5):
    print("Not Weird")
elif n%2==0 and n in range(6,21):
    print("Weird")  
elif n>20 and n%2==0:
    print("Not Weird")