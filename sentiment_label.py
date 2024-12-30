import pandas as pd
import os
import requests
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Set up logging of alert
logging.basicConfig(level=logging.INFO)

# Load API key and email credentials
load_dotenv(r"C:\Users\user\Guest personalization system using AI\.groqenv")
API_KEY = os.getenv('GROQ_API_KEY')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = int(os.getenv('EMAIL_PORT',587))

#Checking if API_KEY and email credentials are loaded correctly
print(f"API Key: {API_KEY}")
print(f"Email User: {EMAIL_USER}")

# Groq API URL for LLaMA 3.3 model
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Creating the prompt template for LLaMA 3.3 model and we are using few-shot prompting and CoT
PROMPT_TEMPLATE = """
You are a helpful assistant analyzing hotel reviews and guest preferences. The review below contains guest feedback and preference details.
Analyze the feedback, correlate it with guest preferences, and determine if the sentiment is positive, neutral, or negative.
Provide a response based on the sentiment, suggest improvements if necessary, and ensure the response addresses specific preferences.

Positive Feedback Example:
Feedback: The spa was amazing, and the staff were very polite.
Preferences: Wellness
Response: Thank you for appreciating our wellness services! We’re glad you enjoyed your stay. Would you like to explore our loyalty program?

Negative Feedback Example:
Feedback: The room was dirty, and the AC didn’t work.
Preferences: Room Preferences, Maintenance
Response: Sorry to hear that. We will work on improving room cleanliness and maintenance. Would you like assistance with this?

Review: {review_text}
Preferences: {preferences}
Sentiment and Response:
"""

# Function to send email alerts
def send_email_alert(to_email, subject, body):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection to the email server
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, to_email, msg.as_string())
        print(f"Email alert sent to {to_email}: {subject}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")


# Function to analyze the review using the Groq LLaMA model
def analyze_review_with_alert(review_text, preferences):
    prompt = PROMPT_TEMPLATE.format(review_text=review_text, preferences=", ".join(preferences))
    
    # Prepare the payload for the API request
    messages = [{"role": "user", "content": prompt}]
    data = {
        "model": "llama-3.3-70b-versatile", 
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 70,
        "n": 1
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Send POST request to the Groq API for inference
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result_text = response.json()["choices"][0]["message"]["content"]
        
        # Determine sentiment based on generated response
        sentiment = "Negative" if "Sorry to hear that" in result_text else ("Positive" if "Thank you!" in result_text else "Neutral")
        
        # Extract department alert if the feedback is negative
        alert = None
        if sentiment == "Negative":
            alert = extract_department_alert(review_text)
            
            # Send email alert with specific details
            if alert:
                email_body = f"Alert: {alert}\n\nReview: {review_text}"
                send_email_alert("hotel.email@example.com", "Hotel Review Alert", email_body)
        
        return sentiment, result_text, alert
    
    else:
        # Debugging: Print the error details to help troubleshoot
        print(f"Error {response.status_code}: {response.json()}")
        return None, None, None

# Function to extract the department responsible for negative feedback
def extract_department_alert(review_text):
    review_text = review_text.lower()
    if "room" in review_text:
        return "Room preference department needs attention about room conditions."
    elif "dining" in review_text or "food" in review_text:
        return "Dining department needs improvement regarding food quality."
    elif "ac" in review_text or "clean" in review_text:
        return "Maintenance and housekeeping need to be notified about AC or cleanliness issues."
    elif "spa" in review_text or "wellness" in review_text:
        return "Wellness department needs to address feedback on spa services."
    elif "pricing" in review_text or "expensive" in review_text:
        return "Pricing department needs to review customer concerns about rates."
    elif "payment" in review_text:
        return "Payment options department needs attention."
    elif "event" in review_text:
        return "Event management department needs improvement."
    elif "sport" in review_text:
        return "Sports facilities department needs attention."
    else:
        return "General feedback - Further investigation needed."

# UI feedback (for testing purposes)
def display_feedback_to_guest(sentiment, response_text):
    if sentiment == "Negative":
        print(f"Sentiment: {sentiment}")
        print(f"Response: {response_text}")
        print(f"Department alert: This issue has been flagged for review.")
    elif sentiment == "Positive":
        print(f"Sentiment: {sentiment}")
        print(f"Response: {response_text}")
    else:
        print(f"Sentiment: {sentiment}")
        print(f"Response: {response_text}")

# Load your dataset
dataset = pd.read_csv(r"C:\Users\user\Guest personalization system using AI\updated_with_detailed_preferences_and_no_preference.csv")

# Limit dataset to first 20 entries
dataset = dataset.iloc[:20]

# Adding columns for sentiment and suggestion
dataset['sentiment'] = ''
dataset['suggestion'] = ''

# Loop over the first 20 reviews and process them
for index, row in dataset.iterrows():
    review_text = row['review_text']
    
    # Extract preferences from columns (assuming these are columns in the dataset)
    preferences = []
    for col in ['dining', 'sports', 'wellness', 'payment options', 'events', 'pricing', 'room preferences']:
        if row.get(col, '').strip().lower() == 'yes':  # Assuming preference is marked as 'yes'
            preferences.append(col.capitalize())
    
    # Call the analysis function
    sentiment, response_text, department_alert = analyze_review_with_alert(review_text, preferences)

    # Display the results in the UI for the guest
    display_feedback_to_guest(sentiment, response_text)

    # Log the department alert to the backend (e.g., log or notify the department responsible)
    if department_alert:
        logging.info(f"Alert to Backend: {department_alert}")

    # Update dataset with sentiment and suggestion
    dataset.at[index, 'sentiment'] = sentiment
    dataset.at[index, 'suggestion'] = response_text

# Save the updated dataset with sentiment labels
dataset.to_csv("Sentiment_updated_hotel_reviews.csv", index=False)






