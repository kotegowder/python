def f(x):
	d=0
	while x >= 1:
		(x,d) = (x/5, d+1)
	return (d)


def h(n):
	s = 0
	for i in range(2,n):
		if n%i == 0:
			s = s + i
	return (s)

def g(m,n):
	res = 0
	while m > n:
		(res ,m) = (res+1, m/n)
	return (res)

def mys(m):
	if m == 1:
		return(1)
	else:
		return(m+mys(m-1))

print(f(4000))
print(h(36) - h(34))
print(g(637,5))
print(mys(4))
