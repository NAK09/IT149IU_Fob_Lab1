print("1. For-loop classification (1-10):")
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

import pandas as pd

df = pd.DataFrame({'Data': [10, 20, 30, 40, 50, 60]})

print("\n2. Pandas filtering by index:")
even_rows = df[df.index % 2 == 0]
odd_rows = df[df.index % 2 != 0]

print("Even index rows:")
print(even_rows)

print("\nOdd index rows:")
print(odd_rows)