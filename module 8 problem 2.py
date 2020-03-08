# written by Jordan on
# 3/6/2020
# this program determines if the sum of inputs is greater than,
# less than or equal to 10

def comparison (x,y):
    if x + y < 10:
        result = "The sum is less than 10"
    elif x + y > 10:
        result = "The sum is greter than 10"
    else:
        result = "The sum equals 10"
    return result

x = int(input("What is your first number?"))

y = int(input("What is your second number?"))

print(comparison(x,y))

        

    
