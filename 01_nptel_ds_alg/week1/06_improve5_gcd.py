def gcd(m,n):

	# Assume m > n
	if m < n:
		(m,n) = (n,m)

	while(m%n) != 0:
		(m,n) = (n, m%n) # m%n < n, always!
	return n

print(gcd(14,63))
