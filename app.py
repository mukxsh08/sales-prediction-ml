import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load('models/sales_model.pkl')
feature_columns = joblib.load('models/feature_columns.pkl')

# Page config
st.set_page_config(page_title="Sales Predictor", page_icon="📊", layout="centered")

# Header
st.title("📊 Sales Prediction App")
st.markdown("Enter customer and product details to predict sales.")
st.divider()

# Input fields
col1, col2 = st.columns(2)

# with col1:
#     quantity     = st.number_input("Quantity",          min_value=1,   max_value=50,    value=10)
#     unit_price   = st.number_input("Unit Price (₹)",    min_value=100, max_value=10000, value=2000)
#     discount     = st.selectbox("Discount (%)", [0, 5, 10, 15, 20])

# with col2:
#     ad_spend     = st.number_input("Advertising Spend (₹)", min_value=500, max_value=20000, value=5000)
#     customer_age = st.number_input("Customer Age",      min_value=18,  max_value=70,    value=35)
with col1:
    quantity     = st.number_input("Quantity",               min_value=1,   max_value=50,    value=10,   step=1)
    unit_price   = st.number_input("Unit Price (₹)",         min_value=100, max_value=10000, value=2000, step=100)
    discount     = st.selectbox("Discount (%)", [0, 5, 10, 15, 20])

with col2:
    ad_spend     = st.number_input("Advertising Spend (₹)",  min_value=500, max_value=20000, value=5000, step=500)
    customer_age = st.number_input("Customer Age",           min_value=18,  max_value=70,    value=35,   step=1)
st.divider()

col3, col4 = st.columns(2)

with col3:
    region  = st.selectbox("Region",  ["East", "North", "South", "West"])

with col4:
    product = st.selectbox("Product", ["Clothing", "Electronics", "Food", "Furniture"])

st.divider()

# Predict button
if st.button("🔮 Predict Sales", use_container_width=True, type="primary"):

    # Build input dataframe
    input_data = {col: [False] for col in feature_columns}

    input_data['Quantity']         = [quantity]
    input_data['UnitPrice']        = [unit_price]
    input_data['Discount']         = [discount]
    input_data['AdvertisingSpend'] = [ad_spend]
    input_data['CustomerAge']      = [customer_age]
    input_data[f'Region_{region}']   = [True]
    input_data[f'Product_{product}'] = [True]

    df_input = pd.DataFrame(input_data)[feature_columns]

    # Predict
    prediction = model.predict(df_input)[0]
    prediction = max(0, prediction)  # No negative sales

    # Show result
    st.success(f"### 💰 Predicted Sales: ₹{prediction:,.2f}")

    # Breakdown
    st.markdown("#### Input Summary")
    summary = {
        "Quantity": quantity,
        "Unit Price": f"₹{unit_price}",
        "Discount": f"{discount}%",
        "Ad Spend": f"₹{ad_spend}",
        "Region": region,
        "Product": product
    }
    st.table(pd.DataFrame(summary.items(), columns=["Field", "Value"]))