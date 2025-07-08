import streamlit as st
from datetime import datetime, timedelta
import csv
import os
import pandas as pd
import random

# Initialize dark mode state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# CSS for light and dark modes
light_css = """
body, .block-container {
    background-color: white;
    color: black;
}
textarea, select, input, button {
    background-color: #f0f0f0 !important;
    color: black !important;
    border-radius: 8px !important;
    border: 1px solid #cccccc !important;
}
.stButton>button {
    background-color: #6200ee !important;
    color: white !important;
    border-radius: 8px !important;
}
.journal-container {
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(102, 166, 255, 0.6);
}
.journal-textarea textarea {
    background: white !important;
    color: #333333 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    height: 150px !important;
    font-size: 16px !important;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
}
"""

dark_css = """
body, .block-container {
    background-color: #121212;
    color: #e0e0e0;
}
textarea, select, input, button {
    background-color: #333333 !important;
    color: #e0e0e0 !important;
    border-radius: 8px !important;
    border: 1px solid #555555 !important;
}
.stButton>button {
    background-color: #bb86fc !important;
    color: black !important;
    border-radius: 8px !important;
}
.journal-container {
    background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(27, 38, 56, 0.9);
}
.journal-textarea textarea {
    background: #222 !important;
    color: #ddd !important;
    border-radius: 10px !important;
    padding: 10px !important;
    height: 150px !important;
    font-size: 16px !important;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.7);
}
"""

def apply_theme():
    if st.session_state.dark_mode:
        st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)
    else:
        st.markdown(f"<style>{light_css}</style>", unsafe_allow_html=True)

apply_theme()

# Sidebar Navigation and theme toggle
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Resources"])

if st.sidebar.button("Toggle Dark Mode 🌙" if not st.session_state.dark_mode else "Toggle Light Mode ☀️"):
    toggle_dark_mode()
    st.experimental_rerun()

# Affirmations list
affirmations = [
    "You are enough just as you are.",
    "Every day is a new beginning.",
    "You are stronger than you think.",
    "Your feelings are valid.",
    "Take it one step at a time.",
    "You deserve kindness and respect.",
    "Believe in your ability to heal."
]
affirmation = random.choice(affirmations)

if page == "Home":
    st.title("Virtual Mental Health Companion")
    
    # Show Affirmation
    st.markdown(f"### 🌟 Daily Affirmation:\n> {affirmation}")
    
    # Check if user logged mood today for reminder
    checked_in_today = False
    if os.path.isfile('mood_journal.csv'):
        df_check = pd.read_csv('mood_journal.csv')
        if not df_check.empty:
            last_entry_date_str = df_check['Timestamp'].max()
            last_entry_date = datetime.strptime(last_entry_date_str, "%Y-%m-%d %H:%M:%S")
            if last_entry_date.date() == datetime.now().date():
                checked_in_today = True
    
    if not checked_in_today:
        st.warning("🔔 You haven't checked in your mood today. Take a moment for your mental health!")
    
    st.header("Daily Mood Check-in")

    mood_activities = {
        "Happy 😊": ["Keep up the great energy!", "Share your happiness with a friend.", "Do something creative."],
        "Sad 😞": ["Listen to your favorite music.", "Try a short walk outside.", "Write down three things you're grateful for."],
        "Anxious 😰": ["Practice deep breathing for 5 minutes.", "Try a mindfulness meditation.", "Write your worries down and set them aside."],
        "Angry 😡": ["Take a few deep breaths.", "Go for a brisk walk.", "Try some stretching or light exercise."],
        "Neutral 😐": ["Try a new hobby.", "Connect with a friend.", "Spend some time outdoors."]
    }

    mood = st.selectbox("How are you feeling today?", list(mood_activities.keys()))

    # Colorful journaling container
    st.markdown('<div class="journal-container">', unsafe_allow_html=True)
    journal_entry = st.text_area("Write your thoughts or feelings (optional):", key="journal_entry", help="Journaling helps with emotional release.", placeholder="Start typing your journal entry here...")
    st.markdown('</div>', unsafe_allow_html=True)

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

    st.markdown("---")
    st.header("Gratitude Tracker")

    st.markdown("Write down things you're grateful for:")
    gratitude_entry = st.text_input("Enter something you're grateful for today:", key="gratitude_entry")

    if st.button("Add Gratitude"):
        if gratitude_entry.strip() != "":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_row = [now, gratitude_entry]

            file_exists = os.path.isfile('gratitude.csv')
            with open('gratitude.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:
                    writer.writerow(["Timestamp", "Gratitude"])
                writer.writerow(data_row)
            st.success("Gratitude entry added!")

    st.markdown("### Your recent gratitude entries:")
    if os.path.isfile('gratitude.csv'):
        df_grat = pd.read_csv('gratitude.csv')
        df_grat = df_grat.sort_values(by="Timestamp", ascending=False)
        recent = df_grat.head(5)
        for idx, row in recent.iterrows():
            st.write(f"- {row['Timestamp']}: {row['Gratitude']}")
    else:
        st.write("No gratitude entries found.")

    # Gratitude streak calculation
    if os.path.isfile('gratitude.csv'):
        df_streak = pd.read_csv('gratitude.csv')
        df_streak['Date'] = pd.to_datetime(df_streak['Timestamp']).dt.date
        unique_dates = sorted(df_streak['Date'].unique(), reverse=True)

        streak = 0
        today = datetime.now().date()
        for i, d in enumerate(unique_dates):
            if d == today - timedelta(days=i):
                streak += 1
            else:
                break
        st.markdown(f"### Your current gratitude streak: {streak} day(s)")

elif page == "Resources":
    st.title("Mental Health Resources")

    st.markdown("""
    Here are some helpful resources and hotlines:

    - [National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org) – 988 or 1-800-273-8255  
    - [Crisis Text Line](https://www.crisistextline.org) – Text HOME to 741741  
    - [MentalHealth.gov](https://www.mentalhealth.gov) – Information and resources  
    - [BetterHelp](https://www.betterhelp.com) – Online therapy platform  
    - [Calm](https://www.calm.com) – Meditation and sleep app  
    - [Headspace](https://www.headspace.com) – Meditation and mindfulness  
    - [NAMI (National Alliance on Mental Illness)](https://www.nami.org) – Support and education  
    """)

    st.write("If you are in crisis or need immediate help, please contact a professional or call a hotline.")
