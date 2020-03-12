# this program was written by Jordan on 3/8/2020
# this program checks to see if items in lists match

def task (lst):
#when we met last week we talked about this that you don't need a for loop here.  
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

 #characterInventory = ["pan","paper","idea","rope","groceries"]
#characterStat = ["slow"]

#def task(characterInventory,characterStat):
#    if "rope" in characterInventory and "coat" in characterInventory and "first_aid_kit" in characterInventory:
#        if "slow" in characterStat:
#            print("Cannot climb a mountain while slow!")
#        else:
#            print("Prepared to climb a mountain!")
#    else:
#        print("Not equipped to climb a mountain!")
        
#    if "pan" in characterInventory and "groceries" in characterInventory:
#        if "small" in characterStat:
#           print("Cannot cook a meal while small!")
#        else:
#            print("Prepared to cook a meal!")
            
#    else:
#        print("Not equipped to cook a meal!")
#    if "pen" in characterInventory and "paper" in characterInventory and "idea" in characterInventory:
#        if "confusion" in characterStat:
#            print("Cannot write a book while confused!")
#        else:
#            print("Prepared to write a book!")
#    else:
#        print("Not equipped to write a book!")
        
#    return()
#task(characterInventory, characterStat)

        





