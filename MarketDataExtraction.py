
# Loading data ---------------------------
import pandas as pd;
df_market = pd.read_csv('./Data/nifty50.csv')

#print(df_market.columns)

# Preparing market data --------------------
df_market.columns=df_market.columns.str.strip()
# Convert 'Date' to datetime
df_market['Date'] = pd.to_datetime(df_market['Date'])
# Calculate daily returns
df_market['Market_Return'] = df_market['Close'].pct_change()
# Keep necessary columns
df_market = df_market[['Date', 'Close', 'Market_Return']]

#print(df_market)

# -------------------------------------------------------

# Merging news and market data ------------------

# Ensure date columns are datetime type
df_news['Date'] = pd.to_datetime(df_news['Date'])
# Merge DataFrames on 'Date'
df_merged = pd.merge(df_news, df_market, on='Date', how='inner')



# Calculate correlation -----------------------------

# Group by date to get average sentiment per day
df_daily_sentiment = df_news.groupby('Date')['Sentiment_Score'].mean().reset_index()
# Merge with market data
df_analysis = pd.merge(df_daily_sentiment, df_market, on='Date', how='inner')


# Calculate correlation -------------------
correlation = df_analysis['Sentiment_Score'].corr(df_analysis['Market_Return'])
print(f"Correlation between sentiment and market return: {correlation}")


# Visualize the relationship -----------------

plt.figure(figsize=(10,6))
sns.regplot(x='Sentiment_Score', y='Market_Return', data=df_analysis)
plt.title('Correlation between Sentiment Score and Market Return')
plt.show()

