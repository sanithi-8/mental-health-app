import streamlit as st
from datetime import datetime
import csv
import os

st.title("Virtual Mental Health Companion")

st.header("Daily Mood Check-in")

mood = st.selectbox("How are you feeling today?", ["Happy 😊", "Sad 😞", "Anxious 😰", "Angry 😡", "Neutral 😐"])

journal_entry = st.text_area("Write your thoughts or feelings (optional)")

if st.button("Submit"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_row = [now, mood, journal_entry]

    file_exists = os.path.isfile('mood_journal.csv')
    with open('mood_journal.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Timestamp", "Mood", "Journal Entry"])  # Write header if file not exist
        writer.writerow(data_row)

    st.success("Thanks for checking in. Remember, you're not alone.")

st.markdown("---")
st.write("Here are some tips for mental well-being:")
st.write("- Take deep breaths")
st.write("- Take a short walk")
st.write("- Reach out to a friend or professional if needed")
