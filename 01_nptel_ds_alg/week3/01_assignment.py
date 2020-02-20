def remdup(l):
	ret_list = []
	for idx in range(len(l)):
		if l[idx] not in ret_list:
			ret_list.append(l[idx])
	return ret_list

def sumsquares(l):
	(odd_sum, even_sum) = (0, 0)
	for item in l:
		if (item & 1) != 0:
			odd_sum += (item*item)
		else:
			even_sum += (item*item)
	return ([odd_sum, even_sum])


def transpose(m):
	ret_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
	return (ret_m)

print(remdup([3,1,3,5]))
print(remdup([7,3,-1,5]))
print(remdup([3,5,7,5,3,7,10]))

print(sumsquares([1,3,5]))
print(sumsquares([2,4,6]))
print(sumsquares([-1,-2,3,7]))

print(transpose([[1,2,3],[4,5,6]]))
print(transpose([[1],[2],[3]]))
print(transpose([[3]]))
		
