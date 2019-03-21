fname = input("enter the file name\n")
filehandle = open(fname,'r')
noline = int(input('enter no of line to print\n'))
count=0
for line in filehandle:
	print(line)
	count = count+1
	if(count == noline):
		break
print('done')
