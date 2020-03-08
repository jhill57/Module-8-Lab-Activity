# this program was written by Jordan on 3/8/2020
# this program determines if a year input is a leap year

def leapyear(year):
    if year % 4 == 0:
        result = True
   
    elif year % 400 == 0:
        result = True
    else:
        result = False
    return result

pickyouryear = int(input("Pick a year!"))
print("(True = leap year, False = no leap year)",leapyear(pickyouryear))
