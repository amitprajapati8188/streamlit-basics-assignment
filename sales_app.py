import streamlit as st
import pandas as pd

# --- Task 1: Build the App ---
st.title("Interactive Sales Summary")
st.subheader("A simple dashboard for non-technical managers to filter sales data.")

# Hardcoded dataset (5 rows, 3 columns)
data = {
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Headphones", "Webcam"],
    "Category": ["Electronics", "Accessories", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Sales": [1200, 50, 300, 80, 150, 200]
}

df = pd.DataFrame(data)

# --- Task 2: Add a Sidebar & Filtering ---
# Adding a selectbox to the sidebar
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category to Filter:", categories)

# Filtering the DataFrame
filtered_df = df[df["Category"] == selected_category]

# Displaying the filtered DataFrame in the main area
st.write(f"### Data for {selected_category}")
st.dataframe(filtered_df)

# Displaying a line chart of Sales values
st.write(f"### Sales Trend for {selected_category}")
st.line_chart(filtered_df.set_index("Product")["Sales"])