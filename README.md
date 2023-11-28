
# Bike Sharing Data Analysis

This project aims to analyze of bike sharing data in a city. 

### Table of Contents

- [Dataset](#dataset)
- [Analysis](#analysis)
- [Results](#results)
- [Usage](#usage)

## Dataset
The dataset used in this analysis is sourced from [Bike Sharing Dataset from Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset). 
It includes features like:
- **Date and Time:** Timestamps of bike rentals
- **Weather Conditions:** Information about weather (e.g., temperature, humidity, windspeed)
- **Count:** Number of bikes rented

## Analysis

The analysis involves the following steps:

1. **Data Wrangling:**
- Gathering Data : Collecting the required datasets
- Asessing Data : Understanding of the dataset's structure and examining issues such as missing values, inconsistencies, or data types that need modification. 
- Cleaning Data: Handling missing values, converting data types, and ensuring data consistency.
2. **Exploratory Data Analysis (EDA):** Understanding the distributions, correlations, and patterns within the dataset.
3. **Visualizations:** Creating visual representations to better understand the relationships and trends in the data.

## Result
The main findings from the analysis are as follows:
- Revealed the total bike rentals on workdays versus weekends across different seasons
- Trends in bike rentals throughout the day and across different months
- The segmentation of bike rentals based on customer types, distinguishing between casual and registered customers

## Usage

Make sure you have Python installed on your system and have Jupyter Notebook or an IDE where you can run Python scripts. 

Then, you must install all required library :

```bash
    pip install numpy pandas matplotlib seaborn streamlit 
```

Run Streamlit app
```bash
    streamlit run dashboard.py
```
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bike-sharing-data-analysis.streamlit.app)
