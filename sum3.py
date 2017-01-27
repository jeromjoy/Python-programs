# list sorted try checking for sum from both sides 


def checkListWithSum(list,sum):
	low = 0
	high = len(list)-1
	while(low<high):
		s=list[low] + list[high]
		if(s==sum):
			print('the num '+ str(list[low]) + ' at'+
				' '+ str(low) + ' and the num '+ str(list[high]) + ' at'+
				' '+ str(high) + ' gives ' + str(sum))
			return [list[low],list[high]]
		elif (s < sum):
			low = low + 1
		else:
			high = high - 1
	return []
			
	


list = [1,2,3,4]
sum = 8
print(checkListWithSum(list,sum))