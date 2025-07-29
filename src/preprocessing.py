import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def filter_and_clean(df):
    products = ['Credit card', 'Personal loan', 'Buy Now, Pay Later', 'Savings account', 'Money transfer']
    df = df[df['Product'].isin(products)]
    df = df[df['Consumer complaint narrative'].notnull()]
    df['cleaned_narrative'] = df['Consumer complaint narrative'].apply(clean_text)
    return df