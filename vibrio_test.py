pat = "CTTGATCAT"
prev_str_piece = ""
current_index = 0
window = 1024
wider_wind = 20

#read from the given file below (Vibrio_cholerae.txt)
with open("Vibrio_cholerae.txt", "r") as file:
    while True:
        seq = file.read(window).strip()
        current_index += window + wider_wind
	#	indices_pattern(seq, pat, current_index)
        if not seq:
            break

# def indices_pattern(seq, pattern, current_index):
#     indices = []
#     len_text = len(seq)
#     len_pattern = len(pattern)
    
#     for i in range((len_text - len_pattern) + 1):
#         seq_piece = seq[i:i + len_pattern]
#         if seq_piece == pattern:
#             indices.append(i)
    
#     return indices

#all indices of the emerged pattern
	len_text = len(text)
	len_pattern = len(pattern)

	indices = []
	for i in range((len_text - len_pattern) + 1):
		current_text = text[i:i + len_pattern]
		if current_text == pattern:
			indices.append(i)
	return indices

#sort indices in a list; 
#indices_pattern(seq, pat).sort()

#write all indices to the "answer_indices_pattern.txt" file, separate with space " "
with open("answer_Vibrio_cholerae.txt", "w+") as text_file:
	for i in indices_pattern(seq, pat):
		text_file.writelines(f"{i} ")
