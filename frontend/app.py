
import streamlit as st
import requests
import time

st.set_page_config(page_title="Fraud AI Pro", layout="wide")
API_URL = st.sidebar.text_input("API URL", "http://localhost:8080")

st.title("💳 Fraud Detection AI Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Check")
    amount = st.number_input("Transaction Amount", 0.0, 1000000.0, 1000.0)
    if st.button("Check Fraud"):
        try:
            res = requests.get(f"{API_URL}/predict?amount={amount}", timeout=5)
            data = res.json()
            if data.get("fraud"):
                st.error(f"⚠️ FRAUD DETECTED (model={data.get('model')})")
            else:
                st.success(f"✅ Safe Transaction (model={data.get('model')})")
        except Exception as e:
            st.error(f"API error: {e}")

with col2:
    st.subheader("📊 Metrics")
    if st.button("Refresh Metrics"):
        try:
            m = requests.get(f"{API_URL}/metrics", timeout=5).json()
            st.metric("Requests", m.get("requests", 0))
            if m.get("avg_latency_ms") is not None:
                st.metric("Avg Latency (ms)", round(m["avg_latency_ms"], 2))
        except Exception as e:
            st.warning("Metrics unavailable")

st.markdown("---")
st.caption("Blue-Green Deployment Demo | Streamlit + FastAPI + ONNX + Docker + Nginx")
