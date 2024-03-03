seq = ""
pat = ""

#read from the given file below (indices_pattern.txt)
with open("indices_pattern.txt", "r") as file:
    for line1, line2 in zip(file, file):
        pat = line1.strip()
        seq = line2.strip()

# print(f"This is the first string:{seq}.")
# print(f"This is the string:{pat}.")

#print all indices of the emerged pattern
def indices_pattern(text, pattern):
	len_text = len(text)
	len_pattern = len(pattern)

	indices = []
	for i in range((len_text - len_pattern) + 1):
		current_text = text[i:i + len_pattern]
		if current_text == pattern:
			indices.append(i)
	return indices


# print(indices_pattern(seq, pat))

#write all indices to the "answer_indices_pattern.txt" file, separate with space " "
with open("answer_indices_pattern.txt", "w+") as text_file:
	for i in indices_pattern(seq, pat):
		text_file.writelines(f"{i} ")
