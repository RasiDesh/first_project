#Sentiment analysis using matplotlib and textblob library

import matplotlib.pyplot as plt
from textblob import TextBlob


# A list of example sentences
sentences = [
    "I love this new phone; it is excellent!",
    "The company's service is atrocious",
    "The customer service is atrocious",
    "The phone has new features and they are absolutely fantastic.",
    "Mobile phones were introduced in India on July 31, 1995",
]

print("--- TextBlob Sentiment Analysis ---")
for sentence in sentences:
    # Create a TextBlob object
    blob = TextBlob(sentence)

    # Get the sentiment scores
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    print(f"\nSentence: {sentence}")
    print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")

    # Classify based on polarity
    if polarity > 0:
        print("Overall Sentiment: Positive")
    elif polarity < 0:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")


# Use a standard dictionary to store the sentiment counts
sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

for sentence in sentences:
    analysis = TextBlob(sentence)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment_counts['Positive'] += 1
    elif polarity < 0:
        sentiment_counts['Negative'] += 1
    else:
        sentiment_counts['Neutral'] += 1

# Extract data for plotting from the dictionary
sentiment_labels = list(sentiment_counts.keys())
counts = list(sentiment_counts.values())
colors = ['green', 'red', 'blue']

# Create the bar chart
plt.figure(figsize=(8, 6))
plt.bar(sentiment_labels, counts, color=colors)
plt.title('Sentiment Analysis Results using TextBlob')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
