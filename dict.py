# dictionaries are name value pairs, lookup tables
details = {'name' : 'dipannita', 'dob' : '2406', 'city' : 'delhi', 'college' : 'usict'}

# print an item in dictionary
print (details['name'])
# print (details[1])

# add to the dictionary
details['edu'] = 'postgrad'

# remove from dictionary
del details['edu']

details # print in curly braces form
print (details)
# print both fields
for fields, det in details.items():
	print ("{} : {}" .format(fields, det))

# safely get a field's value that may not be there
detail = details.get('age')
if not detail:
	print ("sorry no data found")
else:
	print(detail)

# if data is not there we provide a default one
addr = details.get('address', "Not gonna tell")
print (addr)
# collections.OrderedDict