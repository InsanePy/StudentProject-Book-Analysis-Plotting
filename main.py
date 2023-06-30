import glob
import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))
print(filepaths)
st.title("Diary Tone")
st.subheader("Positivity")

analyzer = SentimentIntensityAnalyzer()
dates = [name.strip(".txt").strip("diary\\") for name in filepaths]
print(dates)
positivity = []
negativity = []
for file in filepaths:
    with open(file, "r", encoding="utf8") as f:
        text = f.read()
    scores = analyzer.polarity_scores(text)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

figure_pos = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_pos)

st.subheader("Negativity")
figure_neg = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_neg)
