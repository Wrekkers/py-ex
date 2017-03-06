print ("Hello Python")
print ("Check check")
print ("Let's do this :D")
print ("Shil out!") 
print ("We need emojis") # 2.x doesnt require round brackets
print (5> -1)
print (5-7)
print (2/4)
print (5/2) # 2.x requires using 5.0 and 2.0 to get floating point answer
def add_num(x, y):
	return x+y
print (add_num(1, 2))
x = add_num(1, 2) # var definition is so easy peasy
print (x)
# print (6 % 0) gives undefined
# mod operations
print ("6 mod -4 is " , 6 % -4)
print ("6 mod 10 is " , 6 % 10)
print ("6 mod -10 is " , 6 % -10)
print ("6 mod 10.5 is " , 6 % 10.5)
# string formatting
str = "oo na na"
print ("%s What's my name" %str)
str2 = 'okay just shutup' # single quotes work just as well
print ('%s %s' %(str, str2))
# round function
print (round(2.67))
print ("first string {} , second string {}" .format(str, str2))
# look at pythonformat.info
print ("." * 10) # note
# raw formatting
print ("%r" %('whatever'))
print ("%r" %("whatever"))
print ("%r" %(True))
# newline character
var = "What\na\nwaste\nof\ntime"
print ("see this" , var)
print ("see this %s" %var)
# print in separate lines
print (""" can i really print
	in 
	separate lines.
	man, that is cool
even tabs are being 
		counted.
	""")
# also use \t for tabs \ is an escape character
print ("this is \\ a slash that required 2 \\")
print ("\\n")
print ("enter name")
name = input()
print ("enter age")
# age = raw_input() works only in python 2.x
age = input()
print ("input entered is {} {}" .format(name, age))
# prompting the user
details = input("will you enter your name again")
