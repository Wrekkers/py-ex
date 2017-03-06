from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print ("Copy from {} to {}" .format(fromfile, tofile))

fr = open(fromfile)
data = fr.read()

print ("Length to be copied: {}" .format(len(data)))
print ("Does the file exist: {}" .format(exists(tofile)))

to = open(tofile, 'w')
to.write(data)

print ("All done now")

fr.close()
to.close()