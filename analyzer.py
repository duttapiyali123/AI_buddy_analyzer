import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Study Analyzer", page_icon="📊")

st.title("📊 Study Analyzer")
st.write("Upload your marks and get simple insights!")

st.caption("Helps students understand their strengths and weaknesses")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Your Data:")
    st.write(df)

    if "Subject" in df.columns and "Marks" in df.columns:

        # Find weak & strong
        weak = df.loc[df["Marks"].idxmin()]
        strong = df.loc[df["Marks"].idxmax()]

        st.subheader("📊 Insights:")

        st.warning(f"⚠️ Focus more on: {weak['Subject']} ({weak['Marks']} marks)")
        st.success(f"✅ Strong in: {strong['Subject']} ({strong['Marks']} marks)")

        st.info("📈 Suggestion: Spend more time on weak subjects and revise regularly!")

    else:
        st.error("CSV must contain 'Subject' and 'Marks' columns.")
