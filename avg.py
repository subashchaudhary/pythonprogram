num = int(input('enter the no fo items\n'))
list1 = list()
for n in range(0,num) :
	item = int(input('enter the item : '))
	list1.append(item);
total = sum(list1)
avg = total/num
print('average is :',avg)
