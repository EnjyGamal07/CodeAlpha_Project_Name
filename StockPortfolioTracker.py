import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol not in self.portfolio:
            self.portfolio[symbol] = {'Shares': 0, 'AveragePrice': 0}

        # Fetch current stock data from Alpha Vantage
        api_key = '0IGPLWTXY8V4DWM6'
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, _ = ts.get_quote_endpoint(symbol=symbol)

        current_price = float(data['05. price'].iloc[0])

        # Update portfolio information
        total_shares = self.portfolio[symbol]['Shares'] + shares
        total_investment = self.portfolio[symbol]['Shares'] * self.portfolio[symbol]['AveragePrice']
        total_investment += shares * current_price
        average_price = total_investment / total_shares

        self.portfolio[symbol] = {'Shares': total_shares, 'AveragePrice': average_price}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and shares <= self.portfolio[symbol]['Shares']:
            # Fetch current stock data from Alpha Vantage
            api_key = '0IGPLWTXY8V4DWM6'
            ts = TimeSeries(key=api_key, output_format='pandas')
            data, _ = ts.get_quote_endpoint(symbol=symbol)

            current_price = float(data['05. price'].iloc[0])

            # Update portfolio information
            remaining_shares = self.portfolio[symbol]['Shares'] - shares
            remaining_investment = remaining_shares * self.portfolio[symbol]['AveragePrice']

            self.portfolio[symbol] = {'Shares': remaining_shares, 'AveragePrice': self.portfolio[symbol]['AveragePrice']}
        else:
            print(f"Error: Insufficient shares of {symbol} in the portfolio.")

    def calculate_portfolio_value(self):
        total_value = sum(
            [self.portfolio[s]['Shares'] * float(yf.Ticker(s).info['ask']) for s in self.portfolio])
        return total_value

    def plot_portfolio_performance(self):
        symbols = list(self.portfolio.keys())
        values = [self.portfolio[s]['Shares'] * float(yf.Ticker(s).info['ask']) for s in symbols]

        plt.figure(figsize=(10, 6))
        plt.bar(symbols, values, color='blue')
        plt.xlabel('Stock Symbols')
        plt.ylabel('Portfolio Value')
        plt.title('Portfolio Performance')
        plt.show()

# Example Usage:
portfolio = StockPortfolio()

# Adding stocks to the portfolio
portfolio.add_stock('AAPL', 10)
portfolio.add_stock('GOOGL', 5)

# Displaying the current portfolio
print("Current Portfolio:")
print(portfolio.portfolio)

# Removing some shares
portfolio.remove_stock('AAPL', 3)

# Displaying the updated portfolio
print("\nUpdated Portfolio:")
print(portfolio.portfolio)

# Calculating and displaying the total portfolio value
total_value = portfolio.calculate_portfolio_value()
print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Plotting the portfolio performance
portfolio.plot_portfolio_performance()
