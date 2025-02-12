import streamlit as st
import sqlite3
from sentiment_label import analyze_review_with_alert,log_sentiment
from sentiment_label import log_interaction
from recommendation import combined_recommendation, load_data_from_db, preprocess_tables, generate_activity_embeddings
import base64
from datetime import datetime

# Sample user credentials
USER_DB = {
    "kyrylo1@example.com": {"password": "password123", "Guest_ID": "G0001"},
    "dimitri1@example.com": {"password": "password456", "Guest_ID": "G0002"},
    "virginia1@example.com": {"password": "password150", "Guest_ID": "G0003"},
    "felix1@example.com":{"password": "password140", "Guest_ID": "G0014"},
    "ann1@example.com":{"password": "password220", "Guest_ID": "G0022"},
}

# Connect to SQLite database
conn = sqlite3.connect(r"C:\\Users\\user\\Guest personalization system using AI\\hotel_database.db")
cursor = conn.cursor()

# Set background image
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background: url(data:image/jpg;base64,{base64_str});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_background(r"C:\\Users\\user\\Guest personalization system using AI\\images\\cefalu Hotels.jpg")

# Login Page
def login_page():
    st.markdown(
        "<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);'>Welcome to Cefalù Hotels</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align: center; color: white;'>Login to Enter Your Feedback</h2>",
        unsafe_allow_html=True,
    )

    # Input fields for login
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Login"):
        if email in USER_DB and USER_DB[email]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
            st.session_state["guest_id"] = USER_DB[email]["Guest_ID"]
            st.success(f"Welcome, {email}!")
        else:
            st.error("Invalid email or password!")



# Feedback Page
def feedback_page():
    if "clicked_ads" not in st.session_state:
        st.session_state["clicked_ads"] = {}
    if "review_submitted" not in st.session_state:
        st.session_state["review_submitted"] = False

    st.markdown(
        "<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);'>We Value Your Feedback</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<h3 style='text-align: center; color: white;'>Logged in as: {st.session_state['user_email']} (Guest ID: {st.session_state['guest_id']})</h3>",
        unsafe_allow_html=True,
    )

    # Input for user review
    st.markdown("<h3 style='color: white;'>Enter your review:</h3>", unsafe_allow_html=True)
    review_input = st.text_area("Enter your review here")

    # Review Submission and Sentiment Analysis
    if st.button("Submit review"):
        if review_input.strip():
            preferences = {
                "dining": "Dinner buffet",
                "sports": "Swimming",
                "wellness": "Spa",
                "payment options": "Credit card",
                "events": "Wedding",
                "pricing": "Affordable",
                "room preferences": "Ocean view",
            }
            formatted_preferences = ", ".join(f"{key}: {value}" for key, value in preferences.items())
            sentiment, response, department = analyze_review_with_alert(review_input, formatted_preferences)
            # Log sentiment into the Reviews table
            log_sentiment(
                guest_id=st.session_state["guest_id"],
                review=review_input,
                sentiment=sentiment,
                suggestion=response,
            )
            st.session_state["review_submitted"] = True 
            st.success("Thank you! Your review has been submitted successfully.")
            st.markdown(
                f"""
                <div style="
                    background-color: rgba(0, 0, 0, 0.5);
                    color: white;
                    font-family: Garamond;
                    font-size: 17px;
                    padding: 10px;
                    border-radius: 5px;
                    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
                    margin: 10px auto;
                    width: fit-content;
                ">
                    {response}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error("Please enter a valid review!")

    # Ad interaction section
    st.markdown("<h3 style='color: white;text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7)'>Explore Our Activities (Ads)</h3>", unsafe_allow_html=True)

    # List of ads
    ads = [
        "Hiking Gear", "Spa Kit", "Yoga Class", "Adventure Package",
        "Wellness Retreat", "Italian Cuisine", "Water Sports Package"
    ]

    # Display ads as clickable buttons
    for ad in ads:
        if st.button(f"View {ad}"):
            # Log the interaction to the database
            log_interaction(
                st.session_state["guest_id"],
                ad,
                rating=None,
                time_spent=60
            )
            # Mark the ad as clicked in session state
            st.session_state["clicked_ads"][ad] = True
            st.success(f"Click here to know more about {ad}............")

    # Recommendation Logic
    if st.session_state["review_submitted"] and st.session_state["clicked_ads"]:
        db_path = r"C:\\Users\\user\\Guest personalization system using AI\\hotel_database.db"
        preferences_table, activities_table, interaction_table = load_data_from_db(db_path)
        preferences_table, activities_table, interaction_table = preprocess_tables(
            preferences_table, activities_table, interaction_table
        )
        activities_table = generate_activity_embeddings(activities_table)

        # Generate recommendations
        recommendations = combined_recommendation(
            st.session_state["guest_id"],
            preferences_table,
            activities_table,
            interaction_table,
        )

        #  recommendations as a single sentence
        if recommendations and isinstance(recommendations, str):
            final_recommendation = f" {recommendations} "
        else:
            final_recommendation = "No specific recommendations available at this time."

        # Display recommendations in a popup notification
        st.markdown(
            f"""
            <div style="
                position: fixed;
                top: 20px;
                right: 20px;
                background: rgba(255, 255, 255, 0.9);
                border: 1px solid #ccc;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                border-radius: 10px;
                padding: 15px;
                width: 300px;
                z-index: 1000;">
                <h5 style="margin: 0; font-family: Arial, sans-serif; color: #333;">Recommended for you!</h5>
                <p style="color: #444; font-family: Arial, sans-serif; margin: 10px 0;">
                    {final_recommendation}
                </p>
                <button style="
                    display: block;
                    margin: 10px auto 0 auto;
                    padding: 5px 10px;
                    background: #007BFF;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                " onclick="window.alert('More recommendations feature coming soon!')">View More</button>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Main App
def main():
    st.markdown(
        "<h1 style='text-align: center; font-family: Roman Italic; color: black; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);'>Cefalù Hotels</h1>",
        unsafe_allow_html=True,
    )

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login_page()
    else:
        feedback_page()

if __name__ == "__main__":
    main()
