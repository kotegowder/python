def gcd(m,n):

	# Assume m > n
	if m < n:
		(m,n) = (n,m)

	if (m%n) == 0:
		return n
	else:
		diff = m-n
		# diff > n ? Possible!
		return(gcd(max(diff, n), min(diff, n)))

print(gcd(14,63))
