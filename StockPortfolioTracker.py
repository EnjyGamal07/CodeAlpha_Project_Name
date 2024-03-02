import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': self.get_stock_price(symbol)}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['shares'] -= shares
        else:
            print(f"You don't own any shares of {symbol}.")

    def get_stock_price(self, symbol):
        try:
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
            response = requests.get(url)
            data = response.json()
            return float(data['Global Quote']['05. price'])
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def display_portfolio(self):
        print("\nStock Portfolio:")
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: {data['shares']} shares | Current Price: ${data['price']:.2f}")

if __name__ == "__main__":
    # Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key
    alpha_vantage_api_key = 'EU20HDZIYDWKVJEU'
    
    portfolio_tracker = StockPortfolio(api_key=alpha_vantage_api_key)

    # Example: Adding stocks to the portfolio
    portfolio_tracker.add_stock('AAPL', 10)
    portfolio_tracker.add_stock('GOOGL', 5)

    # Example: Displaying the current portfolio
    portfolio_tracker.display_portfolio()

    # Example: Removing stocks from the portfolio
    portfolio_tracker.remove_stock('AAPL', 3)

    # Example: Displaying the updated portfolio
    portfolio_tracker.display_portfolio()
