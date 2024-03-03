#A straightforward algorithm for finding the most frequent k-mers in a string Text 
#checks all k-mers appearing in this string (there are |Text| − k + 1 such k-mers) 
#and then computes how many times each k-mer appears in Text. 
#Make sure that your function will work even if the values are all negative.

#from pprint import pprint
from collections import defaultdict

seq = ""
k = 0

#read from the given file below (dataset_240214_13.txt)
with open("dataset_240214_13.txt", "r") as file:
	for line1, line2 in zip(file, file):
		seq = line1.strip()
		k = int(line2.strip())
	# print(f"This is the first string:{seq}.")
	# print(f"This is the number:{k}.")

# the function below has to find all patterns 
#which occur in the given above text(seq = sequence)
def all_patterns(text, k_mer):
	pattern_dict = defaultdict(int)
	l_text = len(text)
	for i in range(l_text - k_mer + 1):
		pattern = text[i:i + k_mer]
		pattern_dict[pattern] += 1
		# if pattern not in pattern_dict:
		# 	pattern_dict[pattern] = 1
		# else:
		# 	pattern_dict[pattern] += 1
	return pattern_dict


#pprint(all_patterns(seq, k))

# the function below has to return all most frequently occure patterns in a text
def frequent_pattern(pattern_dict):
	most_freq = 0
	for value in pattern_dict.values():
		if value > most_freq:
			most_freq = value
	freq_patterns = [k for k, v in pattern_dict.items() if v == most_freq]
	return freq_patterns

# BetterFrequentWords(Text, k)
#     FrequentPatterns ← an array of strings of length 0
#     freqMap ← FrequencyTable(Text, k)
#     max ← MaxMap(freqMap)
#     for all strings Pattern in freqMap
#         if freqMap[pattern] = max
#             append Pattern to frequentPatterns
#     return frequentPatterns

first_func_result = all_patterns(seq, k)
print(frequent_pattern(first_func_result))