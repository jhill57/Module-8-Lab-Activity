# written by Jordan Hill on
# 3/6/2020
# this program determines
# whether inputs are equal or not

def equality (x,y):

    if x == y:
        result = "these numbers equal each other"
    else:
        result = "these numbers do not equal each other"
        

    return result

x = int(input("first number?"))

y = int(input("second number?"))

print (equality(x,y))

    
