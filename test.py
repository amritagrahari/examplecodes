# version 2.0

# method to generate pattern of length 'k'
def starPattern(k):
	for i in range (k):
		for j in range(i+1):
			print "*",
		print ""	
	
# ask for user input for 'k'
print "Please enter any integer - ", 
k = input ()

# print patter if k is an integer, else print "ERROR"
if (isinstance(k, (int, long))):
	starPattern(k)

else:
	print "ERROR"




