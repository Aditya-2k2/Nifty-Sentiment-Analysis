from gnews import GNews
import pandas as pd
from datetime import datetime, timedelta

# Initialize GNews
google_news = GNews()

# Set language to English
google_news.language = 'en'

# Function to fetch news for smaller date ranges
def fetch_news_for_range(query, from_date, to_date):
    google_news.period = ''  # Reset the period to avoid overriding date range
    google_news.from_date = from_date
    google_news.to_date = to_date
    
    news = google_news.get_news(query)
    
    return news

# Query parameters
query = "Indian stock market OR Sensex OR Nifty OR India finance"
num_days = 250  # Number of days to fetch news for
increment = 10  # Fetch in 30-day increments
all_articles = []

# Fetch news in smaller date ranges (e.g., 30-day intervals)
for i in range(0, num_days):
    to_date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
    from_date = (datetime.now() - timedelta(days=i )).strftime('%Y-%m-%d')
    
    # Fetch news for this date range
    articles = fetch_news_for_range(query, from_date, to_date)
    all_articles.extend(articles)  # Add to the total list of articles
    
    print(f"Fetched {len(articles)} articles from {from_date} to {to_date}")

# Extract relevant information
news_data = []
for item in all_articles:
    source_name = item['publisher']['name'] if 'publisher' in item and 'name' in item['publisher'] else 'Unknown Source'
    
    news_data.append({
        'Date': item['published date'],
        'Title': item['title'],
        'Source': source_name,
        'URL': item['url']
    })

# Convert to DataFrame
df_news = pd.DataFrame(news_data)

# Save to CSV
df_news.to_csv('gnews_indian_stock_market_250_days_incremental.csv', index=False)

# Show the first few rows
print(df_news.head())
