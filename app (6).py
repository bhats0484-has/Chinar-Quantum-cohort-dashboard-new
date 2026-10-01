import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Chinar Quantum AI", page_icon="⚡", layout="wide")
st.title("⚡ Chinar Quantum AI")
st.markdown("### Data Source: Future AI Innovators (19 Participants)")

@st.cache_data
def load_data():
    return pd.read_csv("/content/my_chunar_data.csv")

df = load_data()

st.subheader("📊 Global Overview: 19 Participants")
col1, col2, col3 = st.columns(3)
col1.metric("Total Participants", len(df))
col2.metric("Average Quantum Score", f"{df['Quantum_Score'].mean():.2f}")
col3.metric("Average Lexicon Density", f"{df['Lexicon_Density'].mean():.2f}")

st.divider()
selected_participant = st.selectbox("Select a participant:", df['Participant_Name'].tolist())
p_row = df[df['Participant_Name'] == selected_participant].iloc[0]

p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
    st.markdown("### 🧠 Neural Map")
    st.metric("Quantum Score", p_row.get("Quantum_Score", 80))
with p_col2:
    st.markdown("### ⚙️ Sentiment Map")
    st.info(f"Sentiment: {p_row.get('Sentiment_Category', 'Positive')}")
with p_col3:
    st.markdown("### 🤖 AI Profile")
    st.write(p_row.get('Feedback_Summary', 'No feedback'))

st.divider()
st.subheader("📈 Visual Analysis")
st.bar_chart(df.set_index('Participant_Name')['Quantum_Score'])
