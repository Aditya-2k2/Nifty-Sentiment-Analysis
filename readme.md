
---

# Sentiment Analysis of Financial News Impacting Indian Markets

## Project Overview

This project analyzes the **sentiment of financial news** articles related to the **Indian stock market** and compares the sentiment trends with **Nifty 50 market data**. The aim is to understand how sentiment from news headlines might correlate with the daily returns of the Nifty index.

## Data Sources

1. **Financial News Data**:
   - The news headlines are extracted from **Google News** using the GNews API.
   - The headlines are related to terms like "Indian stock market", "Sensex", "Nifty", and "Indian finance".
   - The data spans over the **last 250 days** and is stored in a CSV file named `gnews_indian_stock_market_250_days_incremental.csv`.

2. **Nifty 50 Market Data**:
   - Historical **Nifty 50** market data is sourced from a CSV file (`nifty50.csv`), containing daily **closing prices** and corresponding **market returns**.

## Key Steps

### 1. Data Loading
- The project starts by loading the news headlines from the **news CSV file** and the Nifty market data from the **Nifty CSV file**.

### 2. Data Preprocessing
- **News Preprocessing**:
  - Headlines are cleaned by converting them to lowercase, removing punctuation, and lemmatizing the words.
  - Stopwords (e.g., "and", "the") are removed to focus on important keywords.
  
- **Market Data Preprocessing**:
  - The Nifty market data is cleaned by calculating the **daily market return** based on the closing price.
  
### 3. Sentiment Analysis
- **Sentiment Scores**:
  - Each news headline is analyzed using **TextBlob**, a Python library that assigns a **sentiment polarity score**.
  - Scores range from `-1` (negative) to `1` (positive).
  
- **Sentiment Classification**:
  - Sentiment scores are classified into three categories: **Positive**, **Neutral**, and **Negative**.

### 4. Data Merging
- The daily **average sentiment score** from the news is calculated and merged with the corresponding **Nifty market returns** based on the date.

### 5. Correlation and Visualization
- **Correlation**:
  - The correlation between the daily sentiment score and Nifty market returns is calculated to determine whether news sentiment has any predictive value for market performance.
  
- **Visualization**:
  - A **regression plot** is created to visually display the relationship between the sentiment score and the Nifty market returns.

## Results

- The correlation between **sentiment scores** and **market returns** is found to be **0.04**, indicating a very weak positive correlation.
- This suggests that the news sentiment, while slightly positive, does not have a strong linear relationship with Nifty market performance during the analyzed period.

## How to Run the Project

1. **Install Required Libraries**:
   - Install the necessary Python libraries using the following command:
     ```bash
     pip install pandas nltk textblob matplotlib seaborn
     ```

2. **Run the Script**:
   - Run the Python script, which will:
     - Load the data.
     - Perform sentiment analysis.
     - Merge it with the Nifty market data.
     - Visualize the results.

## Files in the Project

- **gnews_indian_stock_market_250_days_incremental.csv**: Contains the extracted news headlines and their respective sentiment scores.
- **nifty50.csv**: Contains the Nifty 50 market data, including daily closing prices and market returns.

## Conclusion

This project successfully demonstrates how sentiment analysis can be applied to financial news data and how it correlates (albeit weakly) with market performance. The analysis and visualizations provide insights into how public sentiment in financial news might align with stock market movements.

---

