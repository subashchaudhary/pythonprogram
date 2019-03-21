fname = input('enter the file name\n')
fhandle = open(fname,'r')

for line in fhandle:
	if(line.startswith('email')):
		print(line)

 