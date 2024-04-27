# Trend Minder Stock Predictor - Technical Report/Documentation

## Section 1: Introduction
The Trend Minder Stock Predictor project aims to develop a user-friendly website for interactive stock market pricing prediction. The website enables users to visualize stock market price predictions and gain actionable insights for better and informed decision-making.
WebApp URL:   <Public URL for the application > full URL don’t embed
GitHub URL:   https://github.com/hyadav3/tmsp.git

### Project Purpose
The Trend Minder Stock Predictor project aims to develop a user-friendly website for interactive stock market pricing prediction that enables users to visualize stock market price predictions and gain actionable insights for better and informed decision-making.

### Target Audience: 
The target audience for the project includes stock traders, investors, and financial analysts.

### Project Goals:
1.	Visualization of Stock Data: Provide users with intuitive visualizations of stock market data.
2.	Stock Market Analysis: Perform in-depth analysis of stock market trends and patterns.
3.	Informed Decision Making: Empower users to make informed decisions based on accurate predictions and insights.
4.	Educational Insights for New Users: Provide educational resources and insights for users new to stock trading and investing.
   
## Section 2: Project Build

### Project Build: 
The app is built using a tech stack that includes Python, Streamlit, and Streamlit’s widgets such as buttons, sliders, and text inputs, making it highly scalable and flexible. Streamlit itself is a web application framework primarily used for building interactive data applications in Python. It is often used to visualize and interact with data stored in various formats, including CSV files, Excel sheets, SQLite databases, and even external data sources accessed through APIs. We have used <Database type>
Feel free to enter more details about app build 
 The project also utilizes the LSTM (Long Short-Term Memory) time series-based prediction model to analyze historical data and market trends for predicting future market trends. 
This app is running on Haruko to provide open interface access to the public. 

### Data Sources: 
The app uses data from various sources including stock data from yfinance (Python library) and S&P500 companies' tickers from Wikipedia. Features include market predictions and recommendations based on comprehensive data analysis. 
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
Date: specific calendar date on which a stock market transaction occurred, Data Type - Date (mm-dd-yyyy)
Open: price at which a particular stock begins trading on a given trading day, Data Type - floating
Close: final price at which a particular stock is traded on a given trading day, Data Type - floating
high: highest price at which a particular stock traded during a given trading day, Data Type - floating.
low: lowest price at which a particular stock traded during a given trading day, Data Type- floating.
Volume: total number of shares of a particular stock that are traded during a specified period, Data Type - Integer

### Functionalities:
•	Users can input stock symbols and view predicted trends.
•	Users can input specific date range to see specific time series stock plot accordingly.
•	The application provides visualization of historical and predicted stock trends.
•	Users can look for forecasted plot for given stock for better decision making. 
•	Stock search functionality allows users to search for specific stocks or companies.
•	Comprehensive database of stocks and companies for detailed analysis.

## Section 3: Issues

### Issues:
•	Initially, we faced challenges with data preprocessing due to inconsistencies in data formats. We resolved this by implementing robust data cleaning techniques.

•	Ensuring compatibility and smooth interaction between different Streamlit widgets posed difficulties during the development phase. We conducted thorough testing and debugging to identify and resolve compatibility issues promptly.

•	Managing user inputs and outputs efficiently within the Streamlit framework required thorough testing with available widgets.

•	Integrating the machine learning models with the Streamlit web framework posed some difficulties. We addressed this by carefully structuring our code and utilizing Streamlit's capabilities for model integration.

## References:
Fast EDA :  https://pypi.org/project/fasteda/
Yahoo Finance: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
Kaggle: https://www.kaggle.com/code/faressayah/stock-market-analysis-prediction-using-lstm
Python Plot: https://plotly.com/python/templates/
Python: https://www.python.org/
App Build: https://streamlit.io/

