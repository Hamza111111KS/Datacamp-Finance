# Select portfolio asset prices for the middle of the crisis, 2008-2009
asset_prices = portfolio.loc['2008-01-01':'2009-12-31']

# Plot portfolio's asset prices during this time
ax=asset_prices.plot()
ax.set_ylabel("Closing Prices, USD")
plt.show()
