#lists in python
fruitlist = 'apple','orange','banana'
veglist = 'potato','carrot','parsnip'
shoppinglist = []
for i in fruitlist:
     shoppinglist.append(i)
for i in veglist:
     shoppinglist.append(i)
print(shoppinglist)
shoppinglist.pop(0)
print(shoppinglist)
