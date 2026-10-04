import matplotlib.pyplot as plt

base = 200
max_hour = int(input("Enter maximum hour: "))
step = int(input("Enter step size: "))

hours = list(range(0, max_hour + 1, step))
bacteria = []

print("Hour\tNumber of Bacteria")
for h in hours:
    B = base * (2 ** h)
    bacteria.append(B)
    print(f"{h}\t{B}")

plt.plot(hours, bacteria, marker='o')
plt.xlabel('Hour')
plt.ylabel('Number of Bacteria')
plt.title('Bacteria Growth Curve')
plt.grid(True)
plt.show()