# list sorted try binary but still slow

def binarySearch(alist,item, first, last):
	found = False
	midpoint = -1
	while first<=last and not found:
		midpoint = (first + last)//2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1

	if(found):
		return midpoint
	else:
		return -1

def checkListWithSum(list,sum):
	for i in range(len(list)):
		lookingFor = sum - list[i]
		foundAt = binarySearch(list,lookingFor, i+1, len(list)-1)
		if(foundAt>=0):
			print('the num '+ str(list[i]) + ' at'+
				' '+ str(i) + ' and the num '+ str(lookingFor) + ' at'+
				' '+ str(foundAt) + ' gives ' + str(sum))
			return [list[i],lookingFor]
	return []


list = [1,2,3,6]
sum = 8
print(checkListWithSum(list,sum))