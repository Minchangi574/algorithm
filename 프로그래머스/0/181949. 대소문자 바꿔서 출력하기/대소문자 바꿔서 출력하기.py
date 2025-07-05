str = input()
str_list=list(str)
for i in range(len(str_list)):
    char=str_list[i]
    if char.islower():
        str_list[i]=char.upper()
    else:
        str_list[i]=char.lower()
a_str_list="".join(str_list)
print(a_str_list)
