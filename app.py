import streamlit as st

st.title("Mental Health Empowerment App")

st.write("Welcome! This app is here to help you track your mood and find quick tips for mental well-being.")

mood = st.selectbox("How are you feeling today?", ["Happy 😊", "Sad 😞", "Anxious 😰", "Angry 😡", "Neutral 😐"])

if st.button("Submit"):
    st.success(f"Thank you for sharing that you are feeling {mood} today. Remember, you're not alone!")

st.markdown("---")
st.write("Here are some tips for mental well-being:")
st.write("- Take deep breaths")
st.write("- Take a short walk")
st.write("- Reach out to a friend or professional if needed")
