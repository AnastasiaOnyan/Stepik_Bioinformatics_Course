pattern = "CTTGATCAT"

def current_element():
    with open("Vibrio_cholerae.txt", "r") as file:
        while True:
            el = file.read(1)
            if el in ["A", "T", "G", "C"]:
                yield el
            if el == "":
                break

def compare_pattern():
    n = len(pattern)
    piece = ["0"] * n
    counter = - n
    answer = []
    for c in current_element():
        piece.append(c)
        piece.pop(0)
        counter += 1
        if piece == list(pattern):
            answer.append(counter)
    return answer

print(' '.join(str(x) for x in compare_pattern()))