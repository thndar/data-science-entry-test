#def update_dictionary(dct, key, value):
#    """
#    Task 1
#    - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
#    - Return the updated dictionary.
#    """
#    return

def update_dictionary(dct, key, value):

    if key in dct:
        dct[key] = value

    else:
        print(dct)    
        

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


# Create  dictionary

thisdict = {
"name": ["Irene", "Bryan", "Conard"],
"age": ["25", "25", "24"],
}

#print(thisdict)
update_dictionary(thisdict, "name", "Alice")
update_dictionary(thisdict, "age", "26")
print(thisdict)