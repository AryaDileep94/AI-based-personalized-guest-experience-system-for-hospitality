import pandas as pd

# Sample guest data
data = {
    'Guest_ID': [1, 2, 3],
    'Name': ['John', 'Jane', 'Doe'],
    'Preferred_Room': ['Suite', 'Deluxe', 'Standard'],
    'Loyalty_Member': [True, False, True],
    'Age': [34, 28, 45]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Simple personalization function
def personalize_guest_experience(df):
    for index, row in df.iterrows():
        if row['Loyalty_Member']:
            print(f"Welcome back, {row['Name']}! Enjoy your complimentary upgrade to a VIP room.")
        else:
            print(f"Hello {row['Name']}, thank you for choosing us. We recommend trying our deluxe room next time!")

        # Customize based on age (just an example)
        if row['Age'] > 40:
            print(f"Since you're over 40, we recommend a more relaxing experience, like a spa package.\n")
        else:
            print(f"Feel free to explore our adventure packages for a more exciting stay!\n")

if __name__ == "__main__":
    personalize_guest_experience(df)


