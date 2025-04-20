"""
File: Stock Portfolio Tracker.py
Author: Revanth sai
Created: April 13, 2025 
"""

import requests
import json
from datetime import datetime
import os
# You can get one for free at https://www.alphavantage.co/
# Configuration
API_KEY = 'S17YBM28C27TZAWI'  # Your personal API key
PORTFOLIO_FILE = 'portfolio.json'

# AAPL ( Apple ) & MSFT ( Microsoft ) & GOOGL ( Google ) & META ( Facebook ) & TSLA ( Tesla ) & NVDA ( NVIDIA)

class StockPortfolioTracker:
    def init(self):
        """Initialize the portfolio tracker"""
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        """Load portfolio data from file or create new if doesn't exist"""
        if os.path.exists(PORTFOLIO_FILE):
            with open(PORTFOLIO_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_portfolio(self):
        """Save the current portfolio to file"""
        with open(PORTFOLIO_FILE, 'w') as file:
            json.dump(self.portfolio, file, indent=4)

    def get_stock_price(self, symbol):
        """Fetch current stock price using Alpha Vantage API"""
        try:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
            response = requests.get(url)
            data = response.json()

            # Check if we got valid data
            if 'Global Quote' in data and '05. price' in data['Global Quote']:
                return float(data['Global Quote']['05. price'])
            else:
                print(f"Error fetching data for {symbol}: {data.get('Note', 'Unknown error')}")
                return None
        except Exception as e:
            print(f"Error fetching stock price: {e}")
            return None

    def add_stock(self, symbol, shares, purchase_price=None):
        """Add a stock to the portfolio"""
        symbol = symbol.upper()

        if symbol in self.portfolio:
            print(f"{symbol} is already in your portfolio. Use 'update' to modify.")
            return False

        current_price = self.get_stock_price(symbol)
        if current_price is None:
            print(f"Could not fetch current price for {symbol}. Not added to portfolio.")
            return False

        # If purchase price not provided, use current market price
        if purchase_price is None:
            purchase_price = current_price

        self.portfolio[symbol] = {
            'shares': float(shares),
            'purchase_price': float(purchase_price),
            'current_price': current_price,
            'purchase_date': datetime.now().strftime('%Y-%m-%d')
        }

        self.save_portfolio()
        print(f"Added {shares} shares of {symbol} to your portfolio.")
        return True

    def remove_stock(self, symbol):
        """Remove a stock from the portfolio"""
        symbol = symbol.upper()

        if symbol not in self.portfolio:
            print(f"{symbol} is not in your portfolio.")
            return False

        del self.portfolio[symbol]
        self.save_portfolio()
        print(f"Removed {symbol} from your portfolio.")
        return True

    def update_prices(self):
        """Update all stock prices in the portfolio"""
        for symbol in self.portfolio:
            current_price = self.get_stock_price(symbol)
            if current_price is not None:
                self.portfolio[symbol]['current_price'] = current_price
        self.save_portfolio()
        print("Portfolio prices updated.")

    def calculate_portfolio_value(self):
        """Calculate total portfolio value and individual positions"""
        total_value = 0
        total_investment = 0
        print("\nPortfolio Summary:")
        print("-" * 50)
        print(f"{'Symbol':<10}{'Shares':>10}{'Avg Cost':>15}{'Current':>15}{'Value':>15}{'Gain/Loss':>15}")
        print("-" * 50)

        for symbol, data in self.portfolio.items():
            shares = data['shares']
            cost = data['purchase_price']
            current = data['current_price']

            position_value = shares * current
            investment = shares * cost
            gain_loss = position_value - investment
            gain_loss_pct = (gain_loss / investment) * 100 if investment != 0 else 0

            total_value += position_value
            total_investment += investment

            print(f"{symbol:<10}{shares:>10.2f}{cost:>15.2f}{current:>15.2f}"
                  f"{position_value:>15.2f}{gain_loss:>15.2f} ({gain_loss_pct:.2f}%)")

        overall_gain = total_value - total_investment
        overall_gain_pct = (overall_gain / total_investment) * 100 if total_investment != 0 else 0

        print("-" * 50)
        print(f"Total Portfolio Value: ${total_value:.2f}")
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"Total Gain/Loss: ${overall_gain:.2f} ({overall_gain_pct:.2f}%)")
        print("-" * 50)

    def display_menu(self):
        """Display the main menu"""
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Prices")
        print("4. View Portfolio")
        print("5. Exit")

    def run(self):
        """Run the portfolio tracker interface"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                symbol = input("Enter stock symbol: ")
                shares = input("Enter number of shares: ")
                price = input("Enter purchase price (leave blank for current price): ")
                try:
                    if price.strip() == '':
                        self.add_stock(symbol, shares)
                    else:
                        self.add_stock(symbol, shares, price)
                except ValueError:
                    print("Invalid input. Please enter numeric values for shares and price.")

            elif choice == '2':
                symbol = input("Enter stock symbol to remove: ")
                self.remove_stock(symbol)

            elif choice == '3':
                self.update_prices()
                self.calculate_portfolio_value()

            elif choice == '4':
                self.calculate_portfolio_value()

            elif choice == '5':
                print("Exiting Stock Portfolio Tracker.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if name == "main":
    # Note: Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with an actual API key

    if API_KEY == 'YOUR_ALPHA_VANTAGE_API_KEY':
        print("Please replace 'YOUR_ALPHA_VANTAGE_API_KEY' with an actual API key from Alpha Vantage.")
    else:
        tracker = StockPortfolioTracker()
        tracker.run()
