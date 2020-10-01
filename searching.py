shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

itemToFind = "albatross"
foundAt = None
# None is a constant that's used to show that something doesnt have a value

# for index in range(6)

# for index in range(len(shoppingList)):
#     if shoppingList[index] == itemToFind:
#         foundAt = index
#         break


# len is short for length
# indexing a list is just like indexing a string, starting at 0

if itemToFind in shoppingList:
    foundAt = shoppingList.index(itemToFind)
if foundAt is None:
    print("Item found at position {}".format(foundAt))
else:
    print("{} not found".format(itemToFind))

# break is good for jumping out of a for loop
