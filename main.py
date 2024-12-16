import pandas as pd

# Guest feedback data
data = {
    'guest_id': ['G12345', 'G12346', 'G12347'],
    'guest_name': ['Nithya', 'Arun', 'Tara'],
    'feedback': [
        'The room was clean and the service was great.',
        'The check-in process was slow, and the staff was unhelpful.',
        'The room was okay, nothing special. The food was average.'
    ],
    'sentiment': ['Positive', 'Negative', 'Neutral']
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Simple function to process the feedback
def personalize_guest_experience(df):
    for index, row in df.iterrows():
        print(f"\nFeedback for {row['guest_name']} (ID: {row['guest_id']}):")
        print(f"Original feedback: {row['feedback']}")

        # Personalized message based on sentiment
        if row['sentiment'] == 'Positive':
            print(f"Thank you, {row['guest_name']}! We're glad you had a great experience.")
        elif row['sentiment'] == 'Negative':
            print(f"Sorry to hear that, {row['guest_name']}. We'll work on improving our service.")
        else:
            print(f"Thanks for your feedback, {row['guest_name']}. We're always looking to improve.")

        print("\n---\n")

if __name__ == "__main__":
    personalize_guest_experience(df)




