x=input('enter a string\n')
def length(f):
	n=0
	try:
	    while f[n] != 0:
		    n=n+1
	except:
		print (n,type(f))
length(x)
print(len(x))
print (type(x))

