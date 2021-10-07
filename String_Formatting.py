def print_formatted(number):
    for i in range(1,1+n):
        print(str(i).rjust(len(bin(n)[2:]),' '),oct(i)[2:].rjust(len(bin(n)[2:]),' '),hex(i)[2:].upper().rjust(len(bin(n)[2:]),' '),bin(i)[2:].rjust(len(bin(n)[2:]),' '))
    
n=int(input())
print_formatted(n)