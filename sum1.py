
#Time consumming

def checkListWithSum(list,sum):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if(list[i]+list[j]==sum):
				print('the num '+ str(list[i]) + ' at'+
					' '+ str(i) + ' and the num '+ str(list[j]) + ' at'+
					' '+ str(j) + ' gives ' + str(sum))
				return [list[i],list[j]]
	return []


list = [1,2,3,4]
sum = 8
print(checkListWithSum(list,sum))
