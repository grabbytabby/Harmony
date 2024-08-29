import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

# Set page config for page navigation
st.set_page_config(page_title="McM's HarmonyChain Dashboard", layout="wide", initial_sidebar_state="expanded")

# Initialize session state
if 'hmt_balance' not in st.session_state:
    st.session_state.hmt_balance = 1000
if 'mining_power' not in st.session_state:
    st.session_state.mining_power = 10

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main Dashboard", "User Segments", "Crypto & Hip-Hop Database"])

# Header
st.title("McM's HarmonyChain Dashboard")
st.markdown("### Empowering artists and producers through blockchain technology. [McM]")

if page == "Main Dashboard":
    # Sidebar
    st.sidebar.header("User Info")
    user_name = st.sidebar.text_input("Username", "HarmonyUser")
    st.sidebar.write(f"HMT Balance: {st.session_state.hmt_balance}")
    st.sidebar.write(f"Mining Power: {st.session_state.mining_power}")

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Music Streaming")
        genres = ["Pop", "Rock", "Jazz", "Classical", "Electronic"]
        selected_genre = st.selectbox("Select a genre", genres)
        
        if st.button("Stream Music"):
            st.write(f"Streaming {selected_genre} music...")
            st.session_state.hmt_balance += 5
            st.sidebar.write(f"Earned 5 HMT for streaming!")

    with col2:
        st.subheader("Mining Activity")
        if st.button("Mine HMT"):
            mined_amount = np.random.randint(1, 10) * st.session_state.mining_power / 10
            st.session_state.hmt_balance += mined_amount
            st.write(f"Mined {mined_amount:.2f} HMT!")

    st.subheader("Token Price Chart")
    # Generate some fake historical price data
    dates = pd.date_range(end=datetime.now(), periods=30).tolist()
    prices = np.random.randint(90, 110, size=30) / 100  # Random prices between 0.90 and 1.10
    df = pd.DataFrame({'Date': dates, 'Price': prices})

    # Create the line chart using Altair
    chart = alt.Chart(df).mark_line().encode(
        x='Date:T',
        y='Price:Q',
        tooltip=['Date:T', 'Price:Q']
    ).properties(
        title='HMT Token Price (Last 30 Days)'
    )

    st.altair_chart(chart, use_container_width=True)

    # Price Containers
    st.subheader("Current Prices")
    price_col1, price_col2, price_col3 = st.columns(3)

    with price_col1:
        st.metric("Bitcoin", "$100,000")

    with price_col2:
        st.metric("Ethereum", "$10,000")

    with price_col3:
        st.metric("Beatcoin", "$1,000")

    st.subheader("Platform Statistics")
    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("Total Users", "10,532", "+123")

    with col4:
        st.metric("Active Miners", "3,217", "-59")

    with col5:
        st.metric("Songs Streamed Today", "1,532,891", "+12%")

    st.subheader("Governance")
    proposal = st.text_input("Submit a proposal")
    if st.button("Submit"):
        st.write("Proposal submitted successfully!")

    st.subheader("Developer Section")
    st.code("""
    # Sample API call
    import requests

    api_url = "https://api.harmonychain.io/v1"
    response = requests.get(f"{api_url}/user/{user_id}")
    user_data = response.json()
    """, language="python")

    # Footer
    st.markdown("---")
    st.write("© 2023 McM's HarmonyChain. All rights reserved.")

elif page == "User Segments":
    # Header for User Segments
    st.title("User Segments")
    st.markdown("Explore different roles within McM's HarmonyChain ecosystem.")

    # Containers for Artist/Business, Artist and Producer, and Miners
    seg_col1, seg_col2, seg_col3 = st.columns(3)

    with seg_col1:
        st.subheader("Artist / Business")
        st.write("Connect with fans, sell music directly, and manage your business operations.")

    with seg_col2:
        st.subheader("Artist and Producer / Business Producer")
        st.write("Access advanced tools for collaboration and production. Monetize your creative work efficiently.")

    with seg_col3:
        st.subheader("Miners")
        st.write("Contribute to the network's security and earn HMT tokens through mining operations.")

    st.markdown("---")
    st.write("Select the segment that best represents your role within McM's HarmonyChain to get started.")

    # Footer
    st.markdown("---")
    st.write("© 2023 McM's HarmonyChain. All rights reserved.")

elif page == "Crypto & Hip-Hop Database":
    # Header for Relational Database Management System
    st.title("Crypto & Hip-Hop Database Management System")
    st.markdown("Manage and explore data related to cryptocurrencies and top hip-hop tracks.")

    # Simulated Database for Cryptocurrencies
    st.subheader("Cryptocurrencies Data")
    crypto_data = {
        "Name": ["Bitcoin", "Ethereum", "Beatcoin", "Ripple", "Litecoin", "Cardano", "Polkadot", "Solana", "Chainlink", "Dogecoin"],
        "Symbol": ["BTC", "ETH", "BTCN", "XRP", "LTC", "ADA", "DOT", "SOL", "LINK", "DOGE"],
        "Market Cap ($B)": [900, 400, 100, 40, 20, 15, 10, 8, 7, 6],
        "Price ($)": [100000, 10000, 1000, 0.9, 200, 1.5, 8, 120, 7, 0.1]
    }
    crypto_df = pd.DataFrame(crypto_data)
    st.dataframe(crypto_df)

    # Simulated Database for Top 10 Hip-Hop Songs
    st.subheader("Top 10 Hip-Hop Songs from Billboard")
    hip_hop_data = {
        "Rank": list(range(1, 11)),
        "Song Title": ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F", "Song G", "Song H", "Song I", "Song J"],
        "Artist": ["Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5", "Artist 6", "Artist 7", "Artist 8", "Artist 9", "Artist 10"],
        "Weeks on Chart": [12, 8, 15, 22, 5, 7, 19, 10, 6, 13]
    }
    hip_hop_df = pd.DataFrame(hip_hop_data)
    st.dataframe(hip_hop_df)

    st.markdown("---")
    st.write("Manage your crypto investments and explore the latest in hip-hop. Stay updated with the trends in both worlds.")

    # Footer
    st.markdown("---")
    st.write("© 2023 McM's HarmonyChain. All rights reserved.")
