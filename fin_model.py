import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investment Growth Dashboard", layout="wide")

st.title("Investment Growth Dashboard")

# Sidebar inputs
st.sidebar.header("Adjust Parameters")
monthly_investment = st.sidebar.slider("Monthly Investment (PKR)", 1000, 100000, 5000, step=1000)
annual_return = st.sidebar.slider("Annual Return (%)", 1, 30, 15)
years = st.sidebar.slider("Years", 1, 30, 5)

# Convert values
r = annual_return / 100 / 12
n = years * 12

# Calculate investment growth
def calculate_growth(P, r, n):
    values = []
    total = 0
    for i in range(1, n + 1):
        total = (total + P) * (1 + r)
        values.append(total)
    return values

values = calculate_growth(monthly_investment, r, n)
months = np.arange(1, n + 1)

# Create dataframe
df = pd.DataFrame({
    "Month": months,
    "Portfolio Value": values
})

# Show final value
st.metric("Final Portfolio Value", f"Rs. {int(values[-1]):,}")
st.metric("Total Invested", f"Rs. {monthly_investment * n:,}")
st.metric("Profit", f"Rs. {int(values[-1] - monthly_investment * n):,}")

# Plot graph
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Portfolio Value"])
ax.set_xlabel("Months")
ax.set_ylabel("Value (PKR)")
ax.set_title("Investment Growth Over Time")

st.pyplot(fig)

# Show table
st.subheader("Detailed Breakdown")
st.dataframe(df)

st.markdown("---")
st.markdown("Built for experimenting with investment scenarios 🚀")