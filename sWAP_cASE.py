def swap_case(s):
    newstring=''
    for a in s:
        if (a.isupper()) == True:
            newstring+=(a.lower())
        elif (a.islower()) == True: 
            newstring+=(a.upper()) 
        elif (a.isspace()) == True:
            newstring+= a
        else:
            newstring+= a
    return(newstring)

s = input()
print(swap_case(s))