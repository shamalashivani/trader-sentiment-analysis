# Trader Behavior vs Market Sentiment Analysis

## Project Overview

This project analyzes the relationship between **Bitcoin market sentiment** and **trader performance**. The objective is to determine whether traders perform differently during periods of **Fear, Neutral sentiment, or Greed** in the cryptocurrency market.

By combining historical trading data with the **Bitcoin Fear & Greed Index**, this analysis explores how sentiment affects profitability, trading volume, and trader behavior.

## Datasets Used

### 1. Historical Trader Data (Hyperliquid)

This dataset contains individual trade records from traders, including:

* Account (trader identifier)
* Coin traded
* Execution Price
* Trade Size (Tokens and USD)
* Trade Direction (Long/Short)
* Closed PnL (profit or loss)
* Transaction details
* Timestamp of trade

### 2. Bitcoin Fear & Greed Index

This dataset provides daily sentiment indicators for the Bitcoin market:

* Timestamp
* Sentiment value (0–100)
* Classification (Extreme Fear, Fear, Neutral, Greed, Extreme Greed)
* Date

## Objective

The main goal of this analysis is to explore whether **market sentiment influences trader performance** and to uncover patterns that could help inform smarter trading strategies.

Key questions explored:

* Do traders perform better during Greed markets?
* Does Fear lead to higher trading losses?
* Does trading activity increase during certain sentiment phases?

## Data Processing Steps

1. Loaded both datasets using Python and Pandas.
2. Converted timestamps to proper datetime format.
3. Extracted the **date** from the trading timestamp.
4. Standardized date formats in both datasets.
5. Merged trader data with the Fear & Greed sentiment dataset based on date.
6. Cleaned rows where sentiment data was unavailable.

## Analysis Performed

The following analyses were conducted:

* Profit distribution across different market sentiments
* Average trader profit during Fear vs Greed periods
* Trading volume comparison across sentiment categories
* Visualization of profit distribution across sentiment phases

## Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Visual Studio Code

## Key Insights

1. Trader profits show significant variability across all sentiment phases.
2. Most trades generate small profits or losses, while a few trades create large outliers.
3. Strong sentiment periods (Fear or Greed) tend to produce more extreme profit and loss outcomes.
4. Market sentiment influences trader behavior and trading intensity.

## Visualization

The project includes visualizations such as:

* Profit vs Market Sentiment plots
* Distribution of trader PnL across sentiment categories

These visualizations help illustrate how trading performance varies with market emotions.

## Conclusion

The analysis suggests that market sentiment has a noticeable influence on trading outcomes. While sentiment alone does not guarantee profitability, periods of strong market emotion often correspond with higher volatility in trader performance.

Understanding these relationships can help traders and analysts design better strategies and risk management approaches.

## Author

Shivani
Junior Data Science Candidate
