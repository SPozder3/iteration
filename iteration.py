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

# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total


def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

# homework -> 
	# a) write a function that finds the average of the scores
	# b) write a second function that also finds the average, 
	#    but drops the lowest 2 scores

def average(numbers):
	total = 0
	for n in numbers:
		total += n
	
	av = total/float(len(numbers))

	return av

def remove_min(numbers):
	current_min = numbers[0]
	for n in numbers:
		if n <= current_min:
			current_min = n
	numbers.remove(current_min)
	return numbers

def curved_average(numbers):
<<<<<<< HEAD
	numbers1 = remove_min(numbers)
	numbers = remove_min(numbers)

	return average(numbers)
=======
	numbers = remove_min(numbers)
	numbers1 = remove_min(numbers)

	total = 0
	for n in numbers1:
		total += n
	avg = total / float(len(numbers1))

	return avg
>>>>>>> 2ad9ffdec1e57ad877656a39d6f6f5884e6c5823
