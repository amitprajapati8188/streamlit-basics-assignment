# Streamlit Basics Assignment

A simple interactive Streamlit app that displays a hardcoded sales dataset and allows filtering by category via a sidebar.

## Project Structure
- `sales_app.py`: The main Python script containing the Streamlit application code.
- `README.md`: Project documentation.

## Features
- Displays a title and subheader.
- Uses a hardcoded pandas DataFrame with Product, Category, and Sales data.
- Includes a sidebar dropdown (selectbox) to filter data by Category.
- Visualizes filtered data using a table (`st.dataframe`) and a line chart (`st.line_chart`).

## How to Run
1. Install Streamlit: `pip install streamlit`
2. Run the app: `streamlit run sales_app.py`