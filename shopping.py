shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#use square brackets for lists

# for item in shoppingList:
#     if item != "spam":
#         print("Buy " + item)

for item in shoppingList:
    if item == "spam":
        break
        # the loop terminated when it got to spam
    print("Buy " + item)
