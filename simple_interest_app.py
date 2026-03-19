import streamlit as st

# Set page configuration
st.set_page_config(page_title="Simple Interest Calculator", layout="centered")

# Add title and description
st.title("💰 Simple Interest Calculator")
st.write("Calculate simple interest by entering the principal amount, rate of interest, and time period.")

# Create divider
st.divider()

# Create input section in columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    principal = st.number_input(
        "Principal Amount (P)",
        min_value=0.0,
        step=100.0,
        value=1000.0,
        help="Enter the principal amount in currency"
    )

with col2:
    rate = st.number_input(
        "Rate of Interest (R) %",
        min_value=0.0,
        step=0.5,
        value=5.0,
        help="Enter the annual rate of interest"
    )

with col3:
    time = st.number_input(
        "Time (T) in Years",
        min_value=0.0,
        step=0.5,
        value=2.0,
        help="Enter the time period in years"
    )

st.divider()

# Add Calculate button
if st.button("Calculate", use_container_width=True, type="primary"):
    # Calculate Simple Interest using the formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    
    # Display success message
    st.success("✅ Calculation Complete!")
    
    # Display results in a clean format using metrics
    result_col1, result_col2 = st.columns(2)
    
    with result_col1:
        st.metric(
            label="Simple Interest (SI)",
            value=f"₹{simple_interest:.2f}",
            delta=None
        )
    
    with result_col2:
        st.metric(
            label="Total Amount (P + SI)",
            value=f"₹{total_amount:.2f}",
            delta=None
        )
    
    # Show the formula and calculation breakdown
    st.info("📋 **Formula Used:** SI = (P × R × T) / 100")
    st.write(f"**Calculation:** ({principal} × {rate} × {time}) / 100 = **₹{simple_interest:.2f}**")
else:
    st.info("👇 Enter the values and click the 'Calculate' button to see the result")
