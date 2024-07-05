import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Stock Comparison App")

    # Default stock tickers
    stock1_ticker = st.text_input("Enter the first stock ticker", "AAPL")
    stock2_ticker = st.text_input("Enter the second stock ticker", "NVDA")

    # Period selection
    period = st.selectbox("Select period", options=["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"])

    # Add a selection box for the polynomial degree
    degree = st.selectbox("Select the polynomial degree for the trend line", options=[1, 2, 3, 4, 5], index=0)

    if st.button("Compare"):
        # Fetch stock data from Yahoo Finance for the selected period
        stock1_data = yf.download(stock1_ticker, period=period)
        stock2_data = yf.download(stock2_ticker, period=period)

        # Create a figure and axis for plotting
        fig, ax = plt.subplots()

        # Plot stock prices and capture the line color
        stock1_line, = ax.plot(stock1_data["Close"], label=stock1_ticker)
        stock1_color = stock1_line.get_color()

        stock2_line, = ax.plot(stock2_data["Close"], label=stock2_ticker)
        stock2_color = stock2_line.get_color()

        # Calculate and plot trend line for stock1 using the selected polynomial degree
        x = np.array(range(len(stock1_data.index)))
        y = stock1_data["Close"].values
        z = np.polyfit(x, y, degree)
        p = np.poly1d(z)
        ax.plot(stock1_data.index, p(x), linestyle="--", color=stock1_color, label=f"{stock1_ticker} Trend")

        # Calculate and plot trend line for stock2 using the selected polynomial degree
        x = np.array(range(len(stock2_data.index)))
        y = stock2_data["Close"].values
        z = np.polyfit(x, y, degree)
        p = np.poly1d(z)
        ax.plot(stock2_data.index, p(x), linestyle="--", color=stock2_color, label=f"{stock2_ticker} Trend")

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.set_title("Stock Prices with Trends")
        ax.legend()
        ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels to 45 degrees for better readability

        # Use the figure object with streamlit's pyplot function
        st.pyplot(fig)

if __name__ == "__main__":
    main()