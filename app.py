# ================================================
# QR Code Generator (Run ONCE manually, not in Streamlit)
# ================================================
# To generate QR codes, uncomment and run this section ONCE:
"""
import qrcode

BASE_URL = "https://your-app-name.streamlit.app/"

offices = ["cairo", "alex", "delta"]

for office in offices:
    url = f"{BASE_URL}?office={office}"
    img = qrcode.make(url)
    img.save(f"{office}_qr.png")

print("QR Codes generated successfully")
"""
# ================================================

import streamlit as st

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="Office Drinks",
    page_icon="☕",
    layout="centered"
)

# --------------------------------
# Static Drinks Data (No Database)
# --------------------------------
OFFICE_DRINKS = {
    "cairo": [
        {"name": "Coffee", "icon": "☕"},
        {"name": "Tea", "icon": "🍵"},
        {"name": "Juice", "icon": "🧃"},
        {"name": "Water", "icon": "💧"},
    ],
    "alex": [
        {"name": "Coffee", "icon": "☕"},
        {"name": "Water", "icon": "💧"},
    ],
    "delta": [
        {"name": "Tea", "icon": "🍵"},
        {"name": "Water", "icon": "💧"},
    ],
}

# --------------------------------
# Get Office from QR (URL)
# --------------------------------
params = st.query_params
office = params.get("office", "").lower()

# --------------------------------
# Header
# --------------------------------
st.title("☕ Available Drinks")

# --------------------------------
# Validation
# --------------------------------
if office not in OFFICE_DRINKS:
    st.error("❌ Invalid QR Code")
    st.stop()

# --------------------------------
# Office Name
# --------------------------------
st.subheader(f"📍 Office: {office.capitalize()}")

# --------------------------------
# Refresh Button & Print Note
# --------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🔄 Refresh"):
        st.rerun()

with col2:
    st.markdown("🖨️ **Print:** Use your browser print")

st.divider()

# --------------------------------
# Sort Drinks Alphabetically
# --------------------------------
drinks = sorted(OFFICE_DRINKS[office], key=lambda x: x["name"])

# --------------------------------
# Display Drinks
# --------------------------------
for drink in drinks:
    st.markdown(
        f"""
        <div style="
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 12px;
            background-color: #f4f4f4;
            font-size: 20px;
        ">
            {drink["icon"]} <strong>{drink["name"]}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# --------------------------------
# Footer
# --------------------------------
st.caption("Internal use only • Office Drinks Menu")
