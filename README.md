# AI-Based Personalized Guest Experience System for Hospitality

Welcome to the AI-driven Guest Personalization System! This project leverages **Large Language Models (LLMs)** and **Sentiment Analysis** to enhance guest experiences in the hospitality industry. By understanding and analyzing guest feedback, it provides personalized recommendations, real-time alerts, and actionable insights to improve guest satisfaction.

---

## Project Overview

The **AI-driven Guest Personalization System** is designed to analyze guest feedback and offer tailored recommendations based on individual preferences and sentiments. It captures emotions and preferences behind each guest’s response, enabling hotels to deliver a more personalized and memorable experience.  

Hotel staff and management receive real-time insights and alerts, helping them address guest concerns proactively. The system is scalable and modular, ensuring seamless integration with different Customer Relationship Management (CRM) platforms.

---

## Features

- **Sentiment Analysis**: Automatically classifies guest feedback into positive, neutral, or negative categories.
- **Real-Time Alerts**: Sends email notifications to hotel management for negative feedback, enabling prompt action.
- **Customizable Preferences**: Allows hotels to define specific guest experience aspects (e.g., dining, wellness) for focused analysis.
- **Streamlit-Based UI**: Intuitive web interface for review submission and sentiment visualization.
- **Personalized Recommendations**: Offers tailored suggestions based on guest preferences and feedback.
- **Scalable and Modular Design**: Easily integrates with various CRM systems for seamless adoption across platforms.

---

## System Architecture

The system's architecture illustrates how different components interact to deliver a seamless and efficient guest experience.

```plaintext
                       +-----------------------+
                       |    Guest User Interface|
                       |  (Frontend)            |
                       +-----------------------+
                               |
            User Input/Interaction (Preferences, Feedback)
                               |
                       +-----------------------+
                       |     API Layer          |
                       |  (Communication Layer) |
                       +-----------------------+
                               |
             +----------------+-----------------+
             |                                  |
       +----------------+                +---------------------+
       | Business Logic |                | User Interaction    |
       | (Processing,    |                | Manager             |
       | Data Handling)  |                | (Track Interactions)|
       +----------------+                +---------------------+
             |                                  |
   +-----------------+                    +-----------------------+
   | Sentiment       |                    | Recommendation Engine  |
   | Analysis Module |                    | (Personalization)      |
   +-----------------+                    +-----------------------+
             |                                  |
     +----------------+                 +---------------------+
     |   Feedback     |                 | Guest Preferences   |
     |   Data Storage |                 | & Historical Data    |
     +----------------+                 +---------------------+
             |                                  |
   +----------------+                    +-----------------------+
   |     Database   |<------------------>|     AI Models         |
   |  (Guest Data,  |                    | - Sentiment Analysis  |
   |   Feedback,    |                    | - Recommendation      |
   |  Interactions) |                    |    Engine             |
   +----------------+                    +-----------------------+
```

---

## Technologies Used

- **Python**  
- **Streamlit**  
- **Large Language Models (LLMs)**: Utilizing `llama-3.3-70b-versatile` for advanced sentiment analysis.  
- **SMTP for Email Alerts**: Uses Python's `smtplib` and `email` modules for secure communication.  
- **Groq API Key**: Powers additional integrations.  

---

## Installation

To set up the project locally, follow these steps:  

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AryaDileep94/AI-based-personalized-guest-experience-system-for-hospitality.git
   cd AI-based-personalized-guest-experience-system-for-hospitality
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.groqenv` file in the project root directory with the following keys:
   ```plaintext
   API_KEY=your_api_key
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_password
   ```

4. **Run the Streamlit UI**:
   ```bash
   streamlit run guest_UI.py
   ```

---

## Usage

1. **Prepare the Dataset**:  
   Use `main.py` to process and clean the booking reviews dataset. Missing values will be handled, irrelevant columns removed, and new features (guest preferences) added.

2. **Analyze Sentiments**:  
   Run `sentiment_label.py` to classify reviews and generate email alerts for negative feedback.

3. **Explore Data**:  
   Use `eda.py` for simple exploratory data analysis on the cleaned dataset.

4. **Launch the UI**:  
   Run the `guest_UI.py` file to access the Streamlit-based web interface for submitting reviews and visualizing sentiment results.

---

## Key Functionalities

- **Real-Time Feedback Analysis**: Analyzes guest feedback instantly and sends alerts for negative reviews.  
- **Personalized Suggestions**: Combines review text and guest preferences to provide tailored recommendations.  
- **Seamless CRM Integration**: Easily adapts to various CRM systems, making it suitable for different hospitality businesses.  

---

## Conclusion

This system aims to optimize the guest experience by leveraging AI to process feedback, provide actionable insights, and offer personalized suggestions. It is scalable, modular, and integrates easily with existing hospitality management systems.
---



