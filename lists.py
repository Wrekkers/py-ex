# example list
randomlist = ['hello', 'this', 'is', 1, 'list']

# list traversal
for ele in randomlist:
	print (ele)

# build lists on the fly
buildlist = []
for i in range (0,5):
	print ("Enter element for our list")
	# ele = eval(input()) # doesnt take strings??
	ele = input() # what is eval for ???
	buildlist.append(ele)

for ele in buildlist:
	print (ele)

# 2d list
list2d = [[1,2,3], 4]
for ele in list2d:
	print (ele)

alistforwhile = []
i = 0
while i < 4:
	alistforwhile.append(i)
	print (alistforwhile[i])
	i = i + 1

# additional list stuff
# tokenizing
samplestring = "Whatever it is youre doing, just stop."
splitarr = samplestring.split(' ')
listlength = len(splitarr)
i = 0
while i < listlength:
	print (splitarr[i])
	i = i + 1

print ("append as much as you want. press q to quit")
ele = input()
while ele != 'q':
	splitarr.append(ele)
for ele in splitarr:
	print(ele)

# index related stuff
print (splitarr[3:5])
print (splitarr[3])
print (splitarr[1])
print (splitarr[0])
print (splitarr[-1]) # print from end
print (' '.join(splitarr))
# print (join(' ' , splitarr[2:4])) doesnt work???
print ('!'.join(splitarr[1:6])) # square bracket has indices to slice the list
print (splitarr.pop())


