import streamlit as st
from sentiment_label import analyze_review_with_alert  # Import from backend

def analyze_single_review_with_ui(review):
    # Define default preferences for the analysis
    preferences = {
        "dining": True,
        "sports": False,
        "wellness": True,
        "payment options": False,
        "events": True,
        "pricing": True,
        "room preferences": True
    }
    # Call the backend function with both the review and preferences
    sentiment, response, alert = analyze_review_with_alert(review, preferences)
    if alert:
        # Log the alert to the backend (it is not shown to the user)
        print(alert)
    return response

st.title("Hotel Review Sentiment Analysis")

# Input for user review
review_input = st.text_input("Enter your review:")
if st.button("Analyze"):
    if review_input.strip():
        response = analyze_single_review_with_ui(review_input)
        st.write(response)
    else:
        st.write("Please enter a valid review!")

