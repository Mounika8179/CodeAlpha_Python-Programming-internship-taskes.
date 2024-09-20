import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, ticker, shares):
        """Add a stock to the portfolio."""
        if ticker in self.stocks:
            self.stocks[ticker]['shares'] += shares
        else:
            self.stocks[ticker] = {'shares': shares, 'purchase_price': self.get_stock_price(ticker)}

    def remove_stock(self, ticker, shares):
        """Remove a stock from the portfolio."""
        if ticker in self.stocks:
            if self.stocks[ticker]['shares'] >= shares:
                self.stocks[ticker]['shares'] -= shares
                if self.stocks[ticker]['shares'] == 0:
                    del self.stocks[ticker]
            else:
                print("Error: Not enough shares to remove.")
        else:
            print("Error: Stock not found in portfolio.")

    def get_stock_price(self, ticker):
        """Fetch the current stock price."""
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]

    def track_performance(self):
        """Display the performance of the portfolio."""
        total_investment = 0
        total_current_value = 0
        
        print("\nYour Stock Portfolio:")
        for ticker, data in self.stocks.items():
            current_price = self.get_stock_price(ticker)
            investment_value = data['shares'] * data['purchase_price']
            current_value = data['shares'] * current_price
            total_investment += investment_value
            total_current_value += current_value
            
            print(f"{ticker}: {data['shares']} shares, Purchase Price: ${data['purchase_price']:.2f}, "
                  f"Current Price: ${current_price:.2f}, Investment Value: ${investment_value:.2f}, "
                  f"Current Value: ${current_value:.2f}")
        
        print(f"\nTotal Investment: ${total_investment:.2f}")
        print(f"Total Current Value: ${total_current_value:.2f}")
        print(f"Overall Gain/Loss: ${total_current_value - total_investment:.2f}")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
