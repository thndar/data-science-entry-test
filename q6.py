#def find_first_negative(lst):
#    """
#    Task 1
#    - Create a function that finds the first negative number in a list (lst).
#    - Return the first negative number if found, otherwise return "No negatives".
#    - Use a while loop to implement this.
#    """
#    return

def find_first_negative(lst):
    #print(lst)
    #print(len(lst))

    i = 0
    while i < len(lst):
        if (lst[i] < 0):
            print(lst[i])
            return lst[i]


        elif (i == len(lst)-1):
            print("No negatives")        
            
        
        i+=1




# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

thislist = [3, 5, -1, 7, -2, 8]
find_first_negative(thislist)

thislist1 = [2, 10, 7, 0]
find_first_negative(thislist1)

