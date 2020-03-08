# written by Jordan on
# 3/6/2020
# this program determines if value 5 in in list

def value(lst):
    for i in lst:
        if i == 5:
         result = "5 is in the list"

    return result

lst = [1,2,3,4,5]
lst2 = [2,3]

print(value(lst))
print(value(lst2))




