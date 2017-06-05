from utils.dictionary_words import dictionary_word
from utils.num_patterns import classify_num_string

def find_patterns(password, subs):
	# password = name of password
	# sub = tuple(name, starting index, flag)
	parse_string = True
	substrings = sorted(subs, key=lambda x: x[1])


	end_i = 0
	starting_sub = None
	limit = -1
	pattern = []

	# goes through each subsequence and gets the best pattern
	while parse_string:
		parse_string = False
		start_i = len(password) -1
		for sub in substrings:
			if sub[1] is not None:
				if sub[1] > limit and sub[1] <= start_i and (sub[1] + len(sub[0])-1) > end_i:
					if sub[2]:
						start_i = sub[1]
						end_i = sub[1] + len(sub[0]) -1
						keep_sub = sub
						parse_string = True

		if parse_string:
			# avoiding duplicate entries
			limit = end_i
			pattern.append((keep_sub[0], keep_sub[2]))

			if pattern_beg == None or keep_sub[1] < pattern_beg:
				pattern_beg = keep_sub[1]
			if pattern_end == None or end_i >= pattern_end:
				pattern_end = end_i + 1

	pattern = classify_excess(password, pattern, pattern_beg, pattern_end)

	return pattern

def classify_excess(password, pattern, pattern_beg, pattern_end):
	excess_beg = password[:pattern_beg]
	excess_end = password[pattern_end:]

	# check excess_beg
	if excess_beg.isnumeric():
		if len(excess_beg) == 1:
			pattern.insert(0, (str(excess_beg), 'single number'))
		else:
			# add the check for type of sequence
			num_class = classify_num_string(excess_beg)
			if num_class:
				pattern.insert(0, (num_class[1], num_class[0]))
	elif excess_beg.isalpha():
		# add the check for type of word
		if dictionary_word(excess_beg):
			pattern.insert(0, (excess_beg), 'word'))
		elif female_name(excess_beg):
			pattern.insert(0, (excess_beg), 'female name'))
		elif male_name(excess_beg):
			pattern.insert(0, (excess_beg), 'male name'))
		elif last_name(excess_beg):
			pattern.insert(0, (excess_beg), 'last name'))

	# check excess_end
	if excess_end.isnumeric():
		if len(excess_end) == 1:
			pattern.append((str(excess_end), 'single number'))
		else:
			# add the check for type of sequence
			num_class = classify_num_string(excess_end)
			if num_class:
				pattern.append((num_class[1], num_class[0]))
	elif excess_end.isalpha():
		# add the check for type of word
		if dictionary_word(excess_end):
			pattern.append((excess_end), 'word'))
		elif female_name(excess_end):
			pattern.append((excess_end), 'female name'))
		elif male_name(excess_end):
			pattern.append((excess_end), 'male name'))
		elif last_name(excess_end):
			pattern.append((excess_end), 'last name'))

	return pattern
