import os
import pandas as pd

base = 200
max_hour = int(input("Enter max hour: "))
step = int(input("Enter step: "))

hours_list = []
bacteria_list = []

print(f"{'Hour':>8}\t{'Number of Bacteria':>20}")

for h in range(0, max_hour + 1, step):
    B = base * (2 ** h)
    hours_list.append(h)
    bacteria_list.append(B)
    print(f"{h:>8}\t{B:>20}")

df = pd.DataFrame({
    "Hour": hours_list,
    "Number of Bacteria": bacteria_list
})

folder = os.path.dirname(__file__)
df.to_csv(os.path.join(folder, "bacteria_growth.csv"), index=False)