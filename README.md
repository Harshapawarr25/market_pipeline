# Market Data Pipeline

A Python-based Market data pipeline for fetching, cleaning, preprocessing, and visualizing stock market data using APIs and Pandas.

---

## Features

- Fetches stock market data from an API
- Cleans and preprocesses raw data
- Handles invalid values
- Converts and formats date columns
- Saves processed datasets to CSV
- Generates data visualizations using Matplotlib
- Modular pipeline architecture

---

## Project Structure

market_pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── charts/
│
├── fetch_data.py
├── clean_data.py
├── preprocessing.py
├── visualization.py
├── output.py
├── main.py
└── README.md

## Technologies Used
Python
Pandas
Matplotlib
Requests
CSV Handling
REST API Integration
Installation

Clone the repository:

git clone <https://github.com/Harshapawarr25/market_pipeline>

Install dependencies:
pip install -r requirements.txt


Run the data pipeline using:
python main.py

## Pipeline Flow
Fetch stock market data from API
Convert API response into a DataFrame
Clean invalid data
Preprocess date and numeric columns
Save processed dataset
Generate visualizations and outputs
Example Outputs
Processed Dataset
Cleaned CSV files stored in:
data/processed/
# Charts
## Generated charts stored in:
charts/


## Future Improvements
Add SQLite/PostgreSQL database support
Add real-time stock streaming
Create interactive dashboards using Streamlit
Add machine learning prediction models
Deploy pipeline to cloud platforms

## Learning Goals

This project was built to practice:

ETL pipeline development
Data preprocessing
API integration
Data visualization
Modular Python project structure

# Author

Harsha Pawar