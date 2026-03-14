import pandas as pd

trader_data = pd.read_csv("historical_data.csv")
sentiment_data = pd.read_csv("fear_greed_index.csv")

trader_data.head()
trader_data.info()

sentiment_data.head()
sentiment_data.info()

trader_data['Timestamp IST'] = pd.to_datetime(
    trader_data['Timestamp IST'],
    format='%d-%m-%Y %H:%M'
)

trader_data['date'] = trader_data['Timestamp IST'].dt.date

sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])

sentiment_data['date'] = sentiment_data['date'].dt.date

merged_data = pd.merge(trader_data, sentiment_data, on='date', how='left')

merged_data = merged_data.dropna(subset=['classification'])

merged_data.info()

merged_data[['date','classification','Closed PnL']].head()

merged_data.groupby('classification')['Closed PnL'].agg(['mean','median','count'])

merged_data.groupby('classification')['Size USD'].sum()

