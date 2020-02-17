def gcd(m,n):

	# Assume m > n
	if m < n:
		(m,n) = (n,m)

	while(m%n) != 0:
		diff = m-n
		# diff > n ? Possible!
		(m,n) = (max(diff, n), min(diff, n))

	return n

print(gcd(14,63))
