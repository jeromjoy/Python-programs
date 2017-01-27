# list unsorted try checking for sum from both sides 

def checkListWithSum(list,sum):
	complements = set()
	for value in list:
		if(value in complements):
			print('the num '+ str(value) +
			' and the num '+ str(sum-value) +
			' gives ' + str(sum) )
			return [value,sum - value]
		else:
			complements.add(sum-value)
	return []
			

list = [1,4,4,6]
sum = 8
print(checkListWithSum(list,sum))