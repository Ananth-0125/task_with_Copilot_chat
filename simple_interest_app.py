import streamlit as st

st.set_page_config(page_title="Simple Interest Calculator", layout="centered")

st.title("💰 Simple Interest Calculator")
st.write("Easily calculate simple interest using principal, rate, and time.")

st.divider()

with st.form("interest_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        principal = st.number_input(
            "Principal (₹)",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

    with col2:
        rate = st.number_input(
            "Rate (%)",
            min_value=0.0,
            value=5.0,
            step=0.5
        )

    with col3:
        time = st.number_input(
            "Time (Years)",
            min_value=0.0,
            value=2.0,
            step=0.5
        )

    submit = st.form_submit_button("Calculate")

st.divider()

if submit:
    if principal == 0 or rate == 0 or time == 0:
        st.warning("⚠️ Please enter values greater than 0")
    else:
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest

        st.success("✅ Calculation Complete!")

        st.subheader("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Simple Interest", f"₹{simple_interest:.2f}")

        with col2:
            st.metric("Total Amount", f"₹{total_amount:.2f}")

        st.info("📌 Formula: SI = (P × R × T) / 100")

        st.write(
            f"Calculation: ({principal} × {rate} × {time}) / 100 = ₹{simple_interest:.2f}"
        )

else:
    st.info("👇 Fill the values and click Calculate")
