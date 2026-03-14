from data_cleaning import merged_data
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='classification', y='Closed PnL', data=merged_data)
plt.xticks(rotation=45)
plt.title("Trader Profit vs Market Sentiment")
plt.show()