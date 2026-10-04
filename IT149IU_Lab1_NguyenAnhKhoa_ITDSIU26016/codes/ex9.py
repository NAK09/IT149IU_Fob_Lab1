import os
import pandas as pd

courses = {}

while True:
    name = input("Enter course name (or 'done' to stop): ")
    if name == 'done':
        break
    grade = int(input(f"Enter grade for {name}: "))
    courses[name] = grade

s = pd.Series(courses)

df = pd.DataFrame({"course": list(courses.keys()), "grade": list(courses.values())})

folder = os.path.dirname(__file__)
df.to_csv(os.path.join(folder, "course_grades.csv"), index=False)

print("\nSummary Statistics:")
print(s.describe())