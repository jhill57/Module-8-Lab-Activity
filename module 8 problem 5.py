# this program was written by Jordan on 3/8/2020
# this program checks to see if items in lists match

def task (lst):
    for i in (lst):
        if i == [task1]:
            result = "You have picked up enough items to perform task 1!"
        elif i == [task2]:
            result = "You have enough items to perform task 2!"
        elif i == [task3]:
            result = "You have enough items to perform task 3!"
        else:
            result = "You do not have enough items to perform these tasks!"
    return result
 
task1 = ["needsrope", "coat", "firstaidkit", "cannothaveslow"]
task2 = ["needspan", "groceries", "cannothavesmall"]
task3 = ["needspen", "paper", "idea", "cannothaveconfusion"]

thelist= ["pan", "paper", "idea", "groceries", "slow"]

print(task(thelist))

        





