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

#def remove_min(numbers):
	#current_min = numbers[0]
	#for n in numbers:
		#if n <= current_min:
			#current_min = n
	#numbers.remove(current_min)
	#return numbers

#def curved_average(numbers):

	#numbers = remove_min(numbers)
	#numbers1 = remove_min(numbers)

	#total = 0
	#for n in numbers1:
		#total += n
	#avg = total / float(len(numbers1))

	#return avg

def min(numbers):
	current_min = numbers[0]

	for n in numbers:
		if n < current_min:
			current_min = n

	return current_min

def second_min(numbers):
	current_min = min(numbers)
	current_second_min = [0]

	for n in numbers:
		if current_min < n < current_second_min:
			current_second_min = n

	return current_second_min

def fixed_curved_average(numbers):
	first_minimum = min(numbers)
	second_minimum = second_min(numbers)

	
	total = sum(numbers)
	new_total= total - first_minimum - second_minimum
	avg = new_total / float(len(numbers)-2)

	return avg