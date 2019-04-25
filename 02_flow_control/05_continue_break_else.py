shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue # => Or use break instead if you want to avoid the loop continue to the end of elements
    print("Buy {}".format(item))
