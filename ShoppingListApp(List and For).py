shopping_list = ["potato", "apple", "oil", "milk", "toilet paper"]
shopping_list.append("batteries")
shopping_list.insert(0, "chocolate")
shopping_list[0] = "dark chocolate"
shopping_list.pop()

print(shopping_list)

purchased_list = ["dark chocolate", "potato", "apple", "oil", "toilet paper", "fish fingers"]

unavailable_items = []

for check in shopping_list:
  if check not in purchased_list:
    unavailable_items.append(check)

if len(unavailable_items) > 0:
  print(f"Here's a list of items on your shopping list that you did not purchase: {unavailable_items}")

else:
  print(f"Good job! You bought everything on your shopping list!")

special_items = []

for check2 in purchased_list:
  if check2 not in shopping_list:
    special_items.append(check2)

if len(special_items) > 0:
  print(f"Here's a list of items you purchased but were not on your shopping list: {special_items}")
