import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.figsize'] = (20, 10)

file_path = "F:\\schulich\\datacamp\\applied finance\\2- Quantitative Risk Management in Python\\FourBanksFinancialCrisis.xlsx"
# Read in the excelfile and parse dates
portfolio = pd.read_excel(file_path, parse_dates = ['Date'], index_col='Date')
portfolio


# Select portfolio asset prices for the middle of the crisis, 2008-2009
asset_prices = portfolio.loc['2008-01-01':'2009-12-31']

# Plot portfolio's asset prices during this time
ax=asset_prices.plot()
ax.set_ylabel("Closing Prices, USD")
plt.show()
