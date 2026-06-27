import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset from GitHub
url = "https://raw.githubusercontent.com/LakshyaSoni4151/Data-Science-45days/main/moviesTMBD.csv"

df = pd.read_csv(url)

# Display Dataset
print("First 5 Rows")
print(df.head())

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

# Select Required Columns
df = df[["popularity", "vote_average"]]

# Remove Missing Values
df = df.dropna()

# Features and Target
X = df[["popularity"]]
y = df["vote_average"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Model Details
print("\nModel Details")
print("--------------------------")
print("Coefficient :", model.coef_[0])
print("Intercept   :", model.intercept_)

# Model Accuracy
print("\nModel Accuracy")
print("--------------------------")
print("Mean Squared Error :", mean_squared_error(y_test, y_pred))
print("R2 Score           :", r2_score(y_test, y_pred))

#graph
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="popularity", y="vote_average")
plt.title("Popularity vs Vote Average")
plt.xlabel("Popularity")
plt.ylabel("Vote Average")
plt.show()

#box plot
plt.figure(figsize=(8,5))
sns.boxplot(y=df["vote_average"])
plt.title("Vote Average Box Plot")
plt.show()
# Sort by popularity
df = df.sort_values("popularity")

plt.figure(figsize=(10,6))

sns.lineplot(
    data=df,
    x="popularity",
    y="vote_average",
    marker="o"
)

plt.title("Popularity vs Vote Average")
plt.xlabel("Popularity")
plt.ylabel("Vote Average")
plt.grid(True)

plt.show()

# Save Model
joblib.dump(model, "model.joblib")

print("\nModel Saved Successfully!")

# Sample Prediction
popularity = float(input("\nEnter Movie Popularity: "))

prediction = model.predict([[popularity]])

print("Predicted Vote Average:", round(prediction[0], 2))