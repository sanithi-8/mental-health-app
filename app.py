import streamlit as st
from datetime import datetime
import csv
import os
import pandas as pd

st.title("Virtual Mental Health Companion")

st.header("Daily Mood Check-in")

# Mood to activities mapping
mood_activities = {
    "Happy 😊": ["Keep up the great energy!", "Share your happiness with a friend.", "Do something creative."],
    "Sad 😞": ["Listen to your favorite music.", "Try a short walk outside.", "Write down three things you're grateful for."],
    "Anxious 😰": ["Practice deep breathing for 5 minutes.", "Try a mindfulness meditation.", "Write your worries down and set them aside."],
    "Angry 😡": ["Take a few deep breaths.", "Go for a brisk walk.", "Try some stretching or light exercise."],
    "Neutral 😐": ["Try a new hobby.", "Connect with a friend.", "Spend some time outdoors."]
}

mood = st.selectbox("How are you feeling today?", list(mood_activities.keys()))

journal_entry = st.text_area("Write your thoughts or feelings (optional)")

if st.button("Submit"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_row = [now, mood, journal_entry]

    file_exists = os.path.isfile('mood_journal.csv')
    with open('mood_journal.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Timestamp", "Mood", "Journal Entry"])
        writer.writerow(data_row)

    st.success("Thanks for checking in. Remember, you're not alone.")
    
    # Suggest mood-lifting activities
    activities = mood_activities.get(mood, [])
    if activities:
        st.markdown("### Here are some activities you might try:")
        for activity in activities:
            st.write(f"- {activity}")

st.markdown("---")
st.write("Here are some general tips for mental well-being:")
st.write("- Take deep breaths")
st.write("- Take a short walk")
st.write("- Reach out to a friend or professional if needed")

# Display past entries
st.markdown("---")
st.header("Your Past Mood & Journal Entries")

if os.path.isfile('mood_journal.csv'):
    df = pd.read_csv('mood_journal.csv')
    df = df.sort_values(by="Timestamp", ascending=False)
    for idx, row in df.iterrows():
        st.markdown(f"**{row['Timestamp']}** - Mood: *{row['Mood']}*")
        if pd.notna(row['Journal Entry']) and row['Journal Entry'].strip() != "":
            st.write(row['Journal Entry'])
        st.markdown("---")
else:
    st.write("No past entries found.")
