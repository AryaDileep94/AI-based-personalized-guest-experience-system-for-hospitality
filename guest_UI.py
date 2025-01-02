import streamlit as st
from sentiment_label import analyze_review_with_alert  # Import from backend

def analyze_single_review_with_ui(review):
    # Extract preferences (UI can later allow dynamic input)
    preferences = {
        "dining": "Dinner buffet",
        "sports": "Swimming",
        "wellness": "Spa",
        "payment options": "Credit card",
        "events": "Wedding",
        "pricing": "Affordable",
        "room preferences": "Ocean view"
    }

    # Format preferences as string for backend
    formatted_preferences = ", ".join(f"{key}: {value}" for key, value in preferences.items())

    # Call the backend function
    sentiment, response, department = analyze_review_with_alert(review, formatted_preferences)
    
    # Log sentiment and department for backend processing
    print(f"Sentiment: {sentiment}")
    print(f"Department Alert: {department}")

    # Display only the suggestion in the UI
    st.write(response)

st.title("Hotel Review Sentiment Analysis")

# Input for user review
review_input = st.text_input("Enter your review:")
if st.button("Analyze"):
    if review_input.strip():
        analyze_single_review_with_ui(review_input)
    else:
        st.write("Please enter a valid review!")








