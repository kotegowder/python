def threesquares(n):
	for x in range(0, n):
		for y in range(0, n):
			for z in range(0, n):
				if (x*x + y*y + z*z) == n:
					return True
	return False 

def repfree(s):
	for i in range(0, len(s)):
		cmp_str = s[:i]+s[i+1:]
		if s[i] in cmp_str:
			return False
	return True

def hillvalley(l):
	graph = []
	for i in range(0, len(l)-2):
		if (l[i] < l[i+1]) and (l[i+1] < l[i+2]):
			graph.append(0)
		elif (l[i] > l[i+1]) and (l[i+1] > l[i+2]):
			graph.append(0)
		else:
			graph.append(1)
	if graph.count(1) == 1:
		return True
	else:
		return False

print(threesquares(6))
print(threesquares(143))
print(threesquares(1024))
print(repfree("qwerty!@#2"))
print(repfree("(x+6)(y-5)"))
print(repfree("94templars"))
print(repfree("siruseri"))
print(hillvalley([1,2,3,5,4,3,2,1]))
print(hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]))
print(hillvalley([9,5,4,-1,-2,3,7]))
print(hillvalley([5,4,3,2,1,0,-1,-2,-3]))
