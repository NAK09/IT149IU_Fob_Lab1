def name_score(name):
    return sum(ord(c) for c in name)

def winner(names_list):
    best_name = ""
    max_score = -1
    for name in names_list:
        score = name_score(name)
        if score > max_score:
            max_score = score
            best_name = name
    return best_name

raw_input = input("Enter names (separated by comma): ")
names_list = [name.strip() for name in raw_input.split(",")]

for name in names_list:
    print(f"{name} score: {name_score(name)}")

top_winner = winner(names_list)
print(f"{top_winner} goes first!")