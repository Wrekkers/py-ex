# tuples are immutable lists
tup1 = (1, 2, 3, 4, 5)
tup2 = (6,) # single element requires a comma 
tup3 = () # empty tuple
tup4 = ('whatever', 'whereever', 1, 2)
# slicing tuples
print (tup1)
print ("tup1[0:4] {}"  .format(tup1[0:4]))
# print ("tup1[-1:-4] {}" .format(tup1[-1:-4])) means nothing; empty result
print ("tup1[:4] {}" .format(tup1[:4]))
print ("tup1[0:] {}" .format(tup1[0:]))
print ("tup1[4] {}" .format(tup1[4]))
print ("tup1[-3:4] {}" .format(tup1[-3:4]))
print ("tup1[-4:-1] {}" .format(tup1[-4:-1]))
# print ("tup1[-3:-4] {}" .format(tup1[-3:-4])) means nothing; empty result

print (tup3)
del tup3

tup5 = tup1 + tup2
print ("After adding tup1 and tup 2: {}" .format(tup5))

# tuple operations
print ("Length of tuple 5: {}" .format (len(tup5)))
tup6 = tup5 * 3
print ("tup5 repeated 3 times: {}" .format(tup6))
print ("Is 7 in tup5: {}" .format(7 in tup5))

# tuple functions
# print ("comapring tuple 1 and tuple 2: {}" .format(cmp(tup1, tup2))) doesnt work
print ("max in tuple 1 : {}" .format(max(tup1))) # similarly we have min funtion
# converting a list to tuple
list1 = [5,6,7,8,9]
print (list1)
print (tuple(list1))




