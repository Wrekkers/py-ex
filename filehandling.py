from sys import argv
from os.path import exists
script, filename = argv
# open file and assign it to a var
f = open(filename, 'w+') # to open it for writing + indicates can read too
# other modes are r and a
# read and print file
# print (f.read())
# write to file
# f.write(input("write something: ")) won't work
line1 = "What shall i write" # gotta figure out taking input and writing to file
f.write(line1) # removes other contents and writes this

# read just one line
# print("We'll read first line")
print(f.read()) # wont print anything
# print(f.read()) these wont work
#close
f.close()
# f = open(filename)
# print (f.read()) still wont work. says unreadable
# f.close()

print("Enter filename of your choice")
fnname = input()
ff= open(fnname) # deafult in read mode
print(ff.read()) # file written above can be rad here but not above???
ff.close()