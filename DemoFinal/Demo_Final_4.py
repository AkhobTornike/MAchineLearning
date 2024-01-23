import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

student_data = pd.read_excel("Student_data.xlsx")
print(student_data.head())

mean_of_math = np.mean(student_data['Math_Score'])
mean_of_english = np.mean(student_data['English_Score'])
mean_of_science = np.mean(student_data['Science_Score'])
mean_of_total = np.mean(student_data['Total_Score'])
median_of_total = np.median((student_data['Total_Score']))

print(f"Mean of Math Score: {mean_of_math}; \n"
      f"Mean of English Score: {mean_of_english}; \n"
      f"Mean of Science Score: {mean_of_science}; \n"
      f"Mean of Total Score: {mean_of_total}; \n"
      f"Median of Total Score: {median_of_total}; \n")


plt.figure(figsize=(10, 6))
plt.plot(student_data['Name'], student_data['Total_Score'], marker=0, label='Total Score Trend')
for index, row in student_data.iterrows():
    plt.plot(row['Name'], row['Total_Score'], marker='o', label=row['Name'], markersize=10)


plt.xlabel('Student')
plt.ylabel('Total Score')
plt.title('Total Scores Trend for Each Student')
plt.legend()
# plt.show()

X = student_data[['Math_Score', 'English_Score', 'Science_Score']]
y = student_data['Total_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}; \n"
      f"Regression Coefficients:\n\t\t"
      f"Math: {model.coef_[0]};\n\t\t"
      f"English: {model.coef_[1]};\n\t\t"
      f"Science: {model.coef_[2]};\n"
      f"Intercept: {model.intercept_}\n")

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Total Score")
plt.ylabel("Predicted Total Score")
plt.title('Linear Regression: Predicted vs Actual Total Score')
# plt.show()

new_df = pd.DataFrame({"Name": student_data['Name'], "Total_Score": student_data['Total_Score']})
print(new_df)

new_df.to_excel("student_summary.xlsx")

random_array = np.array(np.random.randint(0, 100, size=50))
print(random_array)

student_data = pd.read_excel("Student_data.xlsx")
print(student_data)

student_data['Initial'] = student_data['Name'].str[0]
print(student_data)
print(f"Unique values in the 'Initial' Column is: {student_data['Initial'].unique()}")
