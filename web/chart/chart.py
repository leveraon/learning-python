import mplfinance as mpf
import pandas as pd

# Sample stock data (replace with your actual data)
data = {
    'Open': [100, 102, 105, 103, 106],
    'High': [105, 107, 108, 105, 108],
    'Low': [98, 100, 102, 101, 104],
    'Close': [102, 104, 103, 105, 107],
    'Volume': [1000, 1200, 900, 1100, 1300]
}
index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-30', '2023-10-31', '2023-11-01'])
df = pd.DataFrame(data, index=index)

# Add a horizontal line
hline = dict(hlines=[104], colors=['g'], linestyle='-.', linewidths=2, alpha=0.2)

# Add a vertical line
vline = dict(vlines=['2023-10-30'], colors=['r'], linestyle='-', linewidths=1)


# Plot the candlestick chart with lines
mpf.plot(df, type='candle', style='yahoo', title='Stock Chart', volume=True, hlines=hline, vlines=vline)
