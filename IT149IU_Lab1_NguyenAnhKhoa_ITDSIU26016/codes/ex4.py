eggs = int(input("Enter total eggs: "))
per_box = int(input("Enter eggs per box: "))

boxes = eggs // per_box + (1 if eggs % per_box else 0)
last_box_fill = eggs % per_box if eggs % per_box else per_box
need_to_fill_last = per_box - (eggs % per_box) if eggs % per_box else 0

print("Total eggs:", eggs)
print("Boxes needed:", boxes)
print("Eggs in last box:", last_box_fill)
print("Eggs needed to fill last box:", need_to_fill_last)

print("\nASCII Diagram:")
full_boxes = eggs // per_box
remainder = eggs % per_box

for i in range(1, full_boxes + 1):
    print(f"Box {i}: [" + "o " * per_box + "] (Full)")

if remainder > 0:
    print(f"Box {full_boxes + 1}: [" + "o " * remainder + ". " * need_to_fill_last + "] (Partial)")