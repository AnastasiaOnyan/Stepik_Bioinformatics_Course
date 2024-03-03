seq = ""


#read from the given file below (dataset_240215_2.txt)
with open("dataset_240215_2.txt", "r") as file:
	for line in file:
		seq = line.strip()

#this function is reversing given string
def reverse_str(raw_string):
	rev_string = raw_string[::-1]
	return rev_string

#this function is replacing a nucleotide from given string by a complementary one 
def mk_complementary_str(rev_string):
	answer_string = ""
	for i in rev_string:
		if i == "A":
			answer_string += i.replace("A", "T")
		elif i == "T":
			answer_string += i.replace("T", "A")
		elif i == "G":
			answer_string += i.replace("G", "C")
		else:
			answer_string += i.replace("C", "G")
	return answer_string

with open("complementary.txt", "w+") as text_file:
    text_file.write(mk_complementary_str(reverse_str(seq)))