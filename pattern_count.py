seq = ""
pat = ""

with open("dataset_240214_6.txt", "r") as file:
    for line1, line2 in zip(file, file):
        seq = line1.strip()
        pat = line2.strip()
#    print(f"This is the first string:{seq}.")
#    print(f"This is the string:{pat}.")

def pattern_count(text, pattern):
    length_pattern = len(pattern)
    length_text = len(text)
    count = 0
    for i in range((length_text - length_pattern) + 1):
        if text[i:i + length_pattern] == pattern:
            count += 1
    return count

print(pattern_count(seq, pat))