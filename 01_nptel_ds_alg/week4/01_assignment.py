def orangecap(d):
	p_s_d = {}
	for match in d.keys():
		for p_r in d[match].keys():
			if p_r not in p_s_d.keys():
				p_s_d[p_r] = d[match][p_r]
			else:
				p_s_d[p_r] = p_s_d[p_r] + d[match][p_r]

	(player, score) = ('',0)
	for p_r in p_s_d.keys():
		if p_s_d[p_r] > score:
			(player, score) = (p_r, p_s_d[p_r])

	return((player,score))

def addpoly(p1, p2):
	# ret = {'exponent' : coefficint}
	ret_d = {}
	for ele in p1:
		if (ele[0] != 0) and (ele[1] not in ret_d.keys()):

			ret_d[ele[1]] = ele[0]

	for ele in p2:
		if (ele[0] != 0):
			if ele[1] not in ret_d.keys():
				ret_d[ele[1]] = ele[0]
			elif (ret_d[ele[1]] + ele[0]) == 0:
				del ret_d[ele[1]]
			else:
				ret_d[ele[1]] = ret_d[ele[1]] + ele[0]

	ret_l = []
	for x in sorted(ret_d.keys(), reverse=True):
		ret_l.append((ret_d[x], x))

	return (ret_l)

def multpoly(p1, p2):
	exp = 1
	quo = 0
	ret_d = {}
	for item1 in p1:
		for item2 in p2:
			if item1[exp]+item2[exp] not in ret_d.keys():
				ret_d[item1[exp]+item2[exp]] = item1[quo]*item2[quo]
			else:
				ret_d[item1[exp]+item2[exp]] = ret_d[item1[exp]+item2[exp]] + (item1[quo]*item2[quo])

	ret_l = []
	for x in sorted(ret_d.keys(), reverse=True):
		if ret_d[x] != 0:
			ret_l.append((ret_d[x], x))
	return (ret_l)

print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))
print(orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}}))
print(addpoly([(4,3),(3,0)], [(-4,3),(2,1)]))
print(addpoly([(2,1)], [(-2,1)]))
print(multpoly([(1,1),(-1,0)], [(1,2),(1,1),(1,0)]))
