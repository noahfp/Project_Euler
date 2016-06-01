from pprint import pprint

data = ['319','680','180','690','129','620','762','689','762','318',
		'368','710','720','710','629','168','160','689','716','731',
		'736','729','316','729','729','710','769','290','719','680',
		'318','389','162','289','162','718','729','319','790','680',
		'890','362','319','760','316','729','380','319','728','716']

data = set(data)

def subset(x, y):
	x = list(str(x))
	y = list(str(y))
	c = x.pop()
	while len(y) > 0 and len(x) > 0:
		if c == y.pop():
			c = x.pop()
	return len(x) == 0

start = set([])
middle = set([])
end = set([])

for datum in data:
	start.add(list(datum)[0])
	middle.add(list(datum)[1])
	end.add(list(datum)[2])

print start
print middle
print end

for n in range(1000000):
	i = '7' + str(n) + '0'
	print i
	fail = 0
	for datum in data:
		if not subset(datum, i):
			fail = 1
			break
	if not fail:
		print "EYYY"
		break

