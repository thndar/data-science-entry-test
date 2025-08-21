#def find_and_replace(lst, find_val, replace_val):
#    """
#    Task 1
#    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
#    - lst must be a list.
#    - Return the modified list.
#    """
#    return

def find_and_replace(lst, find_val, replace_val):

  i=0
  while i < len(lst):
    if lst[i]==find_val :
         lst[i] = replace_val
    i=i+1

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

mylist1 = [1, 2, 3, 4, 2, 2]
print("List1 Before replace ", mylist1)
find_and_replace(mylist1, 2, 5)
print("List1 After replace ", mylist1)


mylist2 = ["apple", "banana", "apple"]
print("List2 Before replace ", mylist2)
find_and_replace(mylist2, "apple", "orange")
print("List2 After replace ", mylist2)
