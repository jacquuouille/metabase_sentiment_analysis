import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import re

# Download VADER Lexicon (run once)
nltk.download('vader_lexicon')

# === CONFIGURATION ===
input_csv = "/my_pathname/my_file.csv"  # Input CSV
output_csv = "/my_pathname/my_file.csv"  # Output CSV
text_column = "review_text"  # Original text column

# === LOAD DATA ===
df = pd.read_csv(input_csv)

# Check if column exists
if text_column not in df.columns:
    raise ValueError(f"Column '{text_column}' not found. Available columns: {df.columns.tolist()}")

# === CREATE CLEAN COLUMN ===
clean_column = "review_text_clean"
df[clean_column] = df[text_column]  # Duplicate the original column

# === PREPROCESS CLEAN COLUMN ===
neutral_phrases = [
    "nothing", "nothing,", "nothing.", "nothing!", "nothing, it was really great",
    "niets", "there are no negative things", "nothing to dislike",
    "none", "it was no problem for us", "no complaints"
]

def clean_text(text):
    """
    Remove misleading phrases anywhere in the text.
    Handles punctuation and capitalization.
    """
    if pd.isna(text):
        return ""
    text_clean = str(text)
    for phrase in neutral_phrases:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        text_clean = pattern.sub("", text_clean)
    return text_clean.strip()

# Apply cleaning to the duplicate column
df[clean_column] = df[clean_column].apply(clean_text)

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# === ANALYZE CLEAN COLUMN ===
def analyze_text(text):
    text = str(text)

    # TextBlob sentiment
    blob = TextBlob(text)
    tb_polarity = blob.sentiment.polarity
    tb_subjectivity = blob.sentiment.subjectivity

    # VADER sentiment
    vs = sia.polarity_scores(text)
    vader_compound = vs['compound']
    vader_pos = vs['pos']
    vader_neg = vs['neg']
    vader_neu = vs['neu']

    return pd.Series([tb_polarity, tb_subjectivity,
                      vader_compound, vader_pos, vader_neg, vader_neu])

df[['tb_polarity', 'tb_subjectivity',
    'vader_compound', 'vader_pos', 'vader_neg', 'vader_neu']] = df[clean_column].apply(analyze_text)

# === SAVE OUTPUT ===
df.to_csv(output_csv, index=False)
print(f"Sentiment analysis completed. Results saved to {output_csv}")
