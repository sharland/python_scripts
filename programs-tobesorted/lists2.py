#lists in python
#create list of fruit
fruitlist = 'apple','orange','banana'
print('fruit list = ',fruitlist)
#create list of veg
veglist = 'potato','carrot','parsnip'
print('veg list = ',veglist)
#create shopping list, with both fruit and veg
shoppinglist = []
for i in fruitlist:
     shoppinglist.append(i)
for i in veglist:
     shoppinglist.append(i)
print('shopping list = ',shoppinglist)
fruitlist += veglist
print('fruit & veg list = ',fruitlist)
#remove the first item from the list
shoppinglist.pop(0)
print('popped (first) shopping list = ',shoppinglist)
shoppinglist.pop()
print('popped (last) shopping list = ',shoppinglist)
shoppinglist.append('grape')
#print fruit by name
length = len(fruitlist)
for i in range(0,length):
     print('I want a ',fruitlist[i])
#print shoppinglist by name
length = len(shoppinglist)
for i in range(0,length):
     print('shopping list item ',i,' = ',shoppinglist[i])
#access an individual item in the shopping list (number 3)
print('item no 3 in shopping list = ',shoppinglist[3])
#Get the length of the shoppinglist
print('length of shopping list = ',len(shoppinglist))
#sort  the shoppinglist
shoppinglist.sort()
print('sorted shopping list = ',shoppinglist)
#reverse the shoppinglist
shoppinglist.reverse()
print('reversed shopping list = ',shoppinglist)
