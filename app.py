import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# Refresh every 30 seconds
st_autorefresh(interval=30000, key="refresh")

API_URL = "https://www.namiwalks.org/api/events/2030"

st.set_page_config(
    page_title="NAMIWalks Miami Thermometer",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background-color: #003B5C;
    }

    .big-number {
        font-size: 64px;
        font-weight: bold;
        color: white;
        text-align: center;
    }

    .goal-text {
        font-size: 32px;
        color: white;
        text-align: center;
    }

    h1 {
        text-align: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

try:
    response = requests.get(API_URL)
    data = response.json()

    raised = data.get("sumDonations", 0)
    goal = data.get("fundraisingGoal", 425000)

    percent = raised / goal if goal else 0

    st.markdown(
        "<h1>NAMI Miami-Dade Walk Progress</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">${raised:,.0f}</div>',
        unsafe_allow_html=True
    )

    st.progress(percent)

    st.markdown(
        f'<div class="goal-text">{percent:.1%} of ${goal:,.0f} goal</div>',
        unsafe_allow_html=True
    )

except Exception as e:
    st.error(f"Error loading fundraiser data: {e}")
