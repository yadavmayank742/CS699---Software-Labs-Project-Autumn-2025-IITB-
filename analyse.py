import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    "Age": np.random.randint(18, 65, 200),
    "Salary": np.random.normal(50000, 12000, 200).astype(int),
    "Department": np.random.choice(["IT", "HR", "Finance", "Marketing"], 200),
    "Experience": np.random.randint(1, 20, 200)
}
df = pd.DataFrame(data)

print("Summary statistics:\n", df.describe())

avg_salary_dept = df.groupby("Department")["Salary"].mean()
print("\nAverage salary by department:\n", avg_salary_dept)

print("\nCorrelation matrix:\n", df.corr(numeric_only=True))

top_earners = df.nlargest(5, "Salary")[["Age", "Salary", "Department"]]
print("\nTop 5 earners:\n", top_earners)

plt.scatter(df["Experience"], df["Salary"], alpha=0.6)
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
