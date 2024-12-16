import pandas as pd

# Load the new feedback data
new_feedback_data = pd.read_csv("new_feedback.csv")

# Simple keyword-based sentiment mapping
def keyword_sentiment(feedback):
    feedback = feedback.lower()
    if any(word in feedback for word in ["good", "great", "excellent", "amazing", "happy"]):
        return "Positive"
    elif any(word in feedback for word in ["bad", "poor", "terrible", "sad", "slow"]):
        return "Negative"
    else:
        return "Neutral"

# Apply the keyword_sentiment function
new_feedback_data["sentiment"] = new_feedback_data["feedback"].apply(keyword_sentiment)

# Save the results back to a new CSV file
new_feedback_data.to_csv("predicted_feedback.csv", index=False)

print("Sentiment analysis completed. Results saved to 'predicted_feedback.csv'.")
