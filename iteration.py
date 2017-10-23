# iteration pattern

# [1, 5, 7, 8, 4, 3]

def iterate(list):
	#Standard loop with range
	#for i in range(0, len(list)):
		#print list[i]

	#for each loop
	for item in list:
		print item

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i], "scored", scores[i]
