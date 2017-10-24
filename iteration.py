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

#filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

def favorite_class(names, the_class):
	for i in range(0, len(the_class)):
		print names[i], "'s favorite class is", the_class[i]