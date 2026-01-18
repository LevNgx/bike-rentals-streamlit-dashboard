# Bike Rentals Streamlit Dashboard

This project presents an interactive dashboard built using **Streamlit** to summarize key findings from a bike rentals dataset.

The dashboard is based on the analysis and visualizations developed in Assignments 1 and 2 and allows users to explore temporal, seasonal, and behavioral patterns in bike rentals through interactive filters.

## Features
- Interactive filters for:
  - Year
  - Working vs non-working days
  - Season
- Visualizations include:
  - Mean hourly rentals by hour of the day
  - Hourly rental patterns by day of the week
  - Hourly rental patterns by season
  - Mean rentals by period of the day with 95% confidence intervals
  - Correlation heatmap of numerical variables

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
