import matplotlib.pyplot as plt

o = float(input("Enter initial hourly wage ($): "))
p = float(input("Enter percentage change (e.g., 0.03 for 3%): "))
n = int(input("Enter number of years: "))

final_wage = o * ((1 + p) ** n)
print(f"Final wage after {n} years: ${final_wage:.2f}")

reviews_input = input("Enter sequence of reviews separated by comma (e.g., good, bad, good): ")
reviews = [r.strip() for r in reviews_input.split(",")]

current_wage = o
wage_history = [current_wage]

for review in reviews:
    if review == "good":
        current_wage *= 1.03
    elif review == "bad":
        current_wage *= 0.97
    wage_history.append(current_wage)

print(f"Final wage after review sequence: ${current_wage:.2f}")

plt.plot(range(len(wage_history)), wage_history, marker='o')
plt.xlabel("Year")
plt.ylabel("Hourly Wage ($)")
plt.title("Wage Growth / Decline Over Time")
plt.grid(True)
plt.show()