list = [2,3,4,5,6,7,8]
print(type(list))

list[3] = 100   #index 3 te 100 jabe change hobe
print(list)

list.append(200)
print(list)

list.insert(5,600)
print(list)
list.pop()      #last value delete korbe
list.remove(5)  #remove specific value
print(list)
list.sort()     #ascending order
print(list)

#reverse order
list = list[::-1]
print(list)

#descending order

list.sort(reverse = True)
print(list)

#max value
print(max(list))
#length
print(len(list))
#duplicate list
p = list.copy()
print(p)
#clear
p.clear()
print(p) #there will be nothing in the list p

list2 = [4,6.7,"H","Hello",False,5] #different types of data
for i in list2:
    print(i)

