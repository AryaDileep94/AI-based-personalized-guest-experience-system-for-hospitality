import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data_path = "updated_with_detailed_preferences_and_no_preference.csv"
df = pd.read_csv(data_path)

# Data Information
print("Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()
print(f"\nNumber of duplicate rows after removal: {df.duplicated().sum()}")

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Separate numerical and categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

print("\nCategorical Columns:", categorical_columns)
print("Numerical Columns:", numerical_columns)

# Handle 'reviewed_at' if date processing is required
df['reviewed_at'] = pd.to_datetime(df['reviewed_at'], errors='coerce')

# Visualize rating distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'], bins=10, kde=True, color='skyblue')
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Analyze missing data if present
missing_data = df.isnull().sum()
if missing_data.sum() > 0:
    print("\nColumns with missing values:")
    print(missing_data[missing_data > 0])
else:
    print("\nNo missing data.")

# Save cleaned data for further use
cleaned_data_path = "cleaned_dataset.csv"
df.to_csv(cleaned_data_path, index=False)
print(f"\nCleaned dataset saved to {cleaned_data_path}")

# Handle `tkinter` font warnings: Adjust matplotlib settings
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Arial']

print("\nAll issues resolved. Analysis completed.")

