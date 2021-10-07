def count_substring(string, sub_string):
    import re
    match = re.findall('(?='+sub_string+')',string)
    return(len(match))


string = input().strip()
sub_string = input().strip()
print(count_substring(string, sub_string))