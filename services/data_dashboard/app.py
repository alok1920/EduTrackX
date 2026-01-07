import streamlit as st
import requests
import pandas as pd

FASTAPI_URL = "http://127.0.0.1:8000/students"

st.set_page_config(page_title="EduTrackX Dashboard", layout="centered")

st.title("📊 EduTrackX – Student Dashboard")

# 1️⃣ Fetch data from FastAPI
try:
    response = requests.get(FASTAPI_URL)
    response.raise_for_status()
    students = response.json()
except Exception as e:
    st.error(f"Unable to connect to FastAPI: {e}")
    st.stop()

# 2️⃣ If no data
if not students:
    st.warning("No students found.")
    st.stop()

# 3️⃣ Convert to DataFrame
df = pd.DataFrame(students)

# 4️⃣ Search by name
st.subheader("🔍 Search Student")
search_name = st.text_input("Enter student name")

if search_name:
    df = df[df["name"].str.contains(search_name, case=False)]

# 5️⃣ Show table
st.subheader("📋 Student Records")
st.dataframe(df, use_container_width=True)

# 6️⃣ Gender distribution
st.subheader("📊 Gender Distribution")

gender_counts = df["gender"].value_counts()

st.bar_chart(gender_counts)
