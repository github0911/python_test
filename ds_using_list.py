shopList = ["apple", "banana", "orange", "mango", "watermelon", "sugar cane", "pear"]

print("I have", len(shopList), "items to purchase")

print("These items are:", end=' ')

for item in shopList:
    print(item, end=' ')

print("\nI also have to buy rice .")
# append
shopList.append("rice")
print(shopList)
# insert
shopList.insert(2, "corn")
print(shopList)
# sort
shopList.sort()
print(shopList)
print('The first item I will buy is', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('I bought the', oldItem)
print('My shopping list is now', shopList)


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
