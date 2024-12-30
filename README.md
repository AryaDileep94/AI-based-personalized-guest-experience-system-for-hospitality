# AI-based-personalized-guest-experience-system-for-hospitality
Welcome to the AI-driven Guest Personalization System! This system leverages Large Language Models (LLMs) and Sentiment Analysis to enhance the guest experience in the hospitality industry. By understanding and analyzing guest feedback, the system provides personalized recommendations and improves overall guest satisfaction.

The AI-driven Guest Personalization System is designed to enhance the guest experience by automatically processing and analyzing feedback using advanced sentiment analysis. It goes beyond just understanding the words by capturing the emotions and preferences behind each guest’s response. Based on this analysis, the system offers personalized recommendations that cater specifically to individual guest needs, ensuring a tailored experience every time. In real-time, hotel staff and management receive actionable insights, enabling them to make quick and informed decisions that improve guest satisfaction. The system is also scalable and modular, making it easy to integrate with different hospitality businesses and CRM systems, allowing for seamless adoption across various platforms.

## Features

- **Sentiment Analysis**: Automatically classifies guest feedback into positive, neutral, or negative categories.
- **Real-time Alerts**: Sends email notifications to hotel management for negative feedback, enabling prompt action.
- **Customizable Preferences**: Allows hotels to define specific aspects of the guest experience (e.g., dining, wellness) for focused analysis.
- **Scalable and Modular Design**: Easily integrates with various CRM systems for seamless adoption across platforms.
- **Streamlit-based UI**: Intuitive web interface for review submission and sentiment results visualization.
- **Personalized Recommendations**: Provides tailored suggestions based on guest preferences and feedback.

# To setup the project locally
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AryaDileep94/AI-based-personalized-guest-experience-system-for-hospitality
   cd AI-based-personalized-guest-experience-system
2. Install dependencies
   pip install -r requirements.txt
3. Create a .groqenv file in the root directory and add :
   API_KEY=your_api_key
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_password
4. streamlit run guest_UI.py 

This system is designed to analyze guest feedback and provide suggestions in real-time.Alerts are sent to the hotel via email for every negative reviews along with the reason. As the model analyzes the review_text as well as the guest preferences, the system is able to provide more personalized suggestions and reccomendations. Hotel staff and management receive actionable insights in real time, helping them address issues proactively and custom services to individual needs. It can be easily integrated with existing CRM systems, making it adaptable to various hospitality businesses.

# Project Structure
1. guest_UI.py: The Streamlit-based frontend for user interaction.
2. sentiment_label.py: Backend for performing sentiment analysis, handling email alerts and providing real-time sugestions in the UI
3. main.py:Booking reviews dataset is prepared for analysis.Handling missing values, removed unwanted columns and added new columns which contains guest preferences.
4. eda.py: simple EDA is performed on the cleaned dataset
5. .groqenv: Contains sensitive API keys and email credentials (excluded from Git).
6. requirements.txt: Lists all dependencies required for the project.

# Technologies Used
-Python
-Streamlit
-Groq API Key
-SMTP for email alerts(The email alert system leverages Python's built-in smtplib and email modules for secure SMTP communication. No additional installation is required unless you wish to use an external library such as yagmail, which can simplify email handling.)
-Large Language Models (LLMs) for advanced sentiment analysis (llama-3.3-70b-versatile)
   
  
   




