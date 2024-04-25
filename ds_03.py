#Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import os
os.chdir("C:/Users/navit/.pygalaxy")
df = pd.read_csv("twitter_validation.csv")

#Assuming last column
text_column_name = df.columns[-1]

#Create a function to perform sentiment analysis if the data is a string
def analyze_sentiment(text):
    if isinstance(text, str):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        return polarity
    else:
        return 0.0 
    

#Apply sentiment analysis to the text column
df['Sentiment'] = df[text_column_name].apply(analyze_sentiment)
def categorize_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'
    
df['SentimentCategory'] = df['Sentiment'].apply(categorize_sentiment)

#Creating a bar chart 
category_counts = df['SentimentCategory'].value_counts()
categories = category_counts.index.tolist()  # Extract category labels
average_sentiments = [0] * len(categories)  # Initialize with zeros
colors = ['green', 'red','blue']

for i, category in enumerate(categories):
    average_sentiments[i] = df[df['SentimentCategory'] == category]['Sentiment'].mean()

plt.figure(figsize=(8, 6))
bars = plt.bar(categories, average_sentiments, color=colors)
plt.xlabel('Sentiment Category')
plt.ylabel('Average Sentiment Polarity')
plt.title('Sentiment Analysis by Category')

for bar, sentiment in zip(bars, average_sentiments):
    plt.text(bar.get_x() + bar.get_width() / 2, sentiment + 0.02, f'{sentiment:.2f}', fontsize=10, ha='center')

plt.show()

sentiment_counts = df['SentimentCategory'].value_counts()
colors = ['green', 'red','blue']
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Sentiment Distribution')
plt.show()