
import re

import pandas as pd


pd.set_option('display.max_rows', 3000)





file_path = r"C:\Users\HI\Desktop\LGBT_Tweets_processed.csv"  
tweets_df = pd.read_csv(file_path, encoding='ISO-8859-1')



def clean_tweet(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text


happy_keywords = ['happy', 'joy', 'love', 'excited', 'pride', 'pleased', 'delighted']
disgusting_keywords = ['disgust', 'disgusted', 'revolted', 'sick', 'nauseating', 'repulsive', 'horrible']


def classify_sentiment(tweet):
    tweet_words = set(tweet.split())
    if any(word in happy_keywords for word in tweet_words):
        return 'happy'
    elif any(word in disgusting_keywords for word in tweet_words):
        return 'disgusting'
    else:
        return 'neutral'


subset_tweets = tweets_df['tweet'].head(3000)
cleaned_tweets = subset_tweets.apply(clean_tweet)
sentiments = cleaned_tweets.apply(classify_sentiment)


results_df = pd.DataFrame({
    'Original Tweet': subset_tweets,
    'Cleaned Tweet': cleaned_tweets,
    'Sentiment': sentiments
})


print(results_df.head())


results_df.to_csv('C:/Users/HI/Desktop/shujufenxi.csv', index=False)

