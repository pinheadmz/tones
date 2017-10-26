def list(n):
	p = [1.0/1, 16.0/15, 9.0/8, 6.0/5, 5.0/4, 4.0/3, 25.0/18, 3.0/2, 8.0/5, 5.0/3, 9.0/5, 15.0/8, 2.0/1]
	q = ["Uni", "min 2", "Maj 2", "min 3", "Maj 3", "Perf 4", "Tritone", "Perf 5", "min 6", "Maj 6", "min 7", "Maj 7", "Oct"]
	x = 2 ** (1.0/n)
	for i in range(n+1):
		note = 1 * (x ** i)
		print str(i+1) + ":  " + str(note)
		for v, k in enumerate(p):
			# high tolerance = 0.01, low tolerance = 0.005
			if abs(k-note)<0.005:
				print " match: " + q[v]
				print " diff:  " + str(abs(k-note))
	return

for j in range(12,36):
	print
	print
	print
	print "*******"
	print j
	print "*******"
	list(j)
