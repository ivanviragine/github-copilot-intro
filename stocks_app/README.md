# Stock Comparison App

This is a Python application built with Streamlit, Docker, and Docker Compose to compare the performances of two stocks.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:

   ```shell
   git clone https://github.com/your-username/stock-comparison-app.git
   ```

2. Navigate to the project directory:

   ```shell
   cd stock-comparison-app
   ```

3. Build the Docker image:

   ```shell
   docker-compose build
   ```

4. Run the Docker container:

   ```shell
   docker-compose up
   ```

5. Open your web browser and go to `http://localhost:8501` to access the Stock Comparison App.

## Usage

1. Enter the ticker symbol for the first stock in the input field. The default value is `APPL`.

2. Enter the ticker symbol for the second stock in the input field. The default value is `NVDA`.

3. Click the "Compare" button to submit the form.

4. The line chart will display the stock prices of the two stocks.

## Customization

You can customize the default stock tickers by modifying the `app/src/main.py` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.