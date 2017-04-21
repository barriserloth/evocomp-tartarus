fitlist = []

for i in range(1,11):
    bestFit = 10
    for line in open("t" + str(i) + "_simBest.txt", 'r'):
        if "Fitness" in line: 
	    if int(line[-2]) < bestFit and int(line[-2]) != 0:
		bestFit = int(line[-2])
    fitlist.append(("Run " + str(i), bestFit))


print fitlist 
