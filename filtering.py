import pandas as pd

df = pd.read_csv("student_database.csv")

print("Original Data:")
print(df)

df = df[df["Marks"] > 85]

print("\nFiltered Data:")
print(df)

df = df.sort_values(by="Marks", ascending=False)

print("\nSorted Data:")
print(df)

# Conditional Selection
print("\nStudents with Marks greater than 90:")
print(df[df["Marks"] > 90])

# Value Assignment
df.loc[df["Marks"] > 90, "Grade"] = "Excellent"
df.loc[(df["Marks"] > 85) & (df["Marks"] <= 90), "Grade"] = "Very Good"

print("\nData after Value Assignment:")
print(df)

df.to_csv("student_database.csv", index=False)