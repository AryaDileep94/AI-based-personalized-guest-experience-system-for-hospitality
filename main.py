import pandas as pd
import faker
import random
from collections import defaultdict



# Load the dataset
data = pd.read_csv(r"C:\Users\user\Guest personalization system using AI\archive\booking_reviews copy.csv")
print(data.head())
#checking for missing values
print(data.isnull().sum())

# Create a Faker object to generate random names
fake = faker.Faker()

# Load your dataset
data = pd.read_csv(r"C:\Users\user\Guest personalization system using AI\archive\booking_reviews copy.csv")

# Check for missing values in the 'reviewed_by' column
print(data['reviewed_by'].isnull().sum())  # Display how many missing values

# Replace missing values in 'reviewed_by' with random names
data['reviewed_by'] = data['reviewed_by'].apply(lambda x: x if pd.notnull(x) else fake.name())

# Verify the changes
print(data[['reviewed_by', 'review_text']].head())  # Check the first few rows

# Save the updated dataset to a new CSV file
data.to_csv('modified_booking_reviews.csv', index=False)


# Fill missing 'reviewed_at' values with 'Unknown'
data['reviewed_at'] = data['reviewed_at'].fillna('Unknown')

# List of nationalities
nationalities = ['American', 'British', 'Canadian', 'Indian', 'Australian']
# Fill missing 'nationality' values with random nationality from the list
data['nationality'] = data['nationality'].apply(lambda x: random.choice(nationalities) if pd.isnull(x) else x)

# Fill missing 'hotel_name' values with 'Unknown Hotel'
data['hotel_name'] = data['hotel_name'].fillna('Unknown Hotel')

# Fill missing 'tags' values with 'No tags'
data['tags'] = data['tags'].fillna('No tags')

# Drop rows where 'rating' or 'review_text' is missing
data = data.dropna(subset=['rating', 'review_text'])

# Verify the changes
print(data[['rating', 'review_text']].head()) 

# Drop the specified columns
columns_to_drop = ['images', 'crawled_at', 'url', 'hotel_url', 'avg_rating', 'raw_review_text', 'meta']
data.drop(columns=columns_to_drop, inplace=True)
data = data.dropna(subset=['review_title'])



# Verify the changes by checking the columns
print(data.columns)


# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Display the number of missing values per column
print(missing_values)

# Load your dataset
data = pd.read_csv("modified_booking_reviews.csv")

# Initialize a defaultdict to track email counts for duplicates
email_counts = defaultdict(int)

# Function to generate unique email IDs
def generate_unique_email(name):
    if pd.notnull(name):  # Check if name is not null
        clean_name = name.lower().replace(" ", ".")  # Replace spaces with dots
        email_counts[clean_name] += 1  # Increment the count for this name
        return f"{clean_name}{email_counts[clean_name]}@example.com"  # Append count and domain
    return "unknown@example.com"  # Default for missing names

# Apply the function to create the email column
data['customer_email'] = data['reviewed_by'].apply(generate_unique_email)

# Drop the specified columns
columns_to_drop = ['images', 'crawled_at', 'url', 'hotel_url', 'avg_rating', 'raw_review_text', 'meta']
data.drop(columns=columns_to_drop, inplace=True)
data = data.dropna(subset=['review_title'])

# Replace NaN or float values with an empty string
data['review_text'] = data['review_text'].fillna('')

# Save the updated dataset to a new CSV file
data.to_csv("updated_booking_reviews_v2.csv", index=False)


# Display first few rows to verify
print(data[['reviewed_by', 'customer_email']].head())