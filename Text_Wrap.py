import textwrap
def wrap(string, max_width):
    return(textwrap.fill(string,max_width))

string, max_width = input(), int(input())
print(wrap(string, max_width))