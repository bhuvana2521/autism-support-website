import streamlit as st
import os

# Set page title
st.set_page_config(page_title="Autism Support App", layout="centered")

# Load session data
username = st.session_state.get("logged_user", "User")
language = st.session_state.get("language", "English")

# Therapy page buttons with filename as key and label as value
therapy_pages = {
    "01_aba": "Applied Behavior Analysis (ABA)",
    "02_esdm": "Early Start Denver Model (ESDM)",
    "03_dir": "DIR/Floortime",
    "04_teacch": "TEACCH (Structured Teaching)",
    "05_speech": "Speech and Language Therapy",
    "06_ot": "Occupational Therapy (OT)",
    "07_pt": "Physical Therapy (PT)",
    "08_sensory": "Sensory Integration Therapy",
    "09_social": "Social Skills Training",
    "10_aac": "AAC & Communication Tools",
    "11_parent": "Parent-Mediated Therapy",
    "12_play": "Play Therapy",
    "13_music": "Music Therapy",
    "14_art": "Art Therapy"
}

# Pleasant Introduction (based on language)
if language == "English":
    st.markdown("### 🌿 Welcome to the Autism Support App")
    st.markdown(f"#### ✨ Welcome, **{username}** ✨")
    st.markdown("*A safe space made with love, care, and understanding.*\n")
    st.markdown("Here, you're not alone. Every child is unique — and every parent deserves support, hope, and peace of mind.")
    st.markdown("This app is created with the pure intention to **guide, comfort, and uplift** you in your journey.")
    st.markdown("\n🌸 Explore therapy options that suit your child")
    st.markdown("🌼 Track their progress, mood, and joyful moments")
    st.markdown("🌺 Learn, reflect, and grow — step by step, with love")
    st.markdown("\nTake a deep breath. You're doing the best you can.")
    st.markdown("---")
    st.markdown("### 👉 Select a Therapy Type to Learn More:")

elif language == "Tamil":
    st.markdown("### 🌿 ஆட்டிசம் ஆதரவு பயன்பாட்டிற்கு உங்களை அன்புடன் வரவேற்கிறோம்")
    st.markdown(f"#### ✨ வரவேற்கிறோம், **{username}** ✨")
    st.markdown("*இதயத்துடிப்போடு உருவாக்கப்பட்ட ஒரு நிம்மதியான பயணத்துக்கான துணை.*\n")
    st.markdown("இங்கு நீங்கள் தனியாக இல்லை. ஒவ்வொரு குழந்தையும் தனிப்பட்டவர். ஒவ்வொரு பெற்றோருக்கும் ஆதரவும் நம்பிக்கையும் தேவை.")
    st.markdown("இந்தப் பயன்பாடு உங்கள் பயணத்தில் **வழிகாட்ட, ஆறுதல் தர, உற்சாகமளிக்க** உருவாக்கப்பட்டுள்ளது.")
    st.markdown("\n🌸 உங்கள் குழந்தைக்கு ஏற்ற சிகிச்சைகளை ஆராயுங்கள்")
    st.markdown("🌼 அவர்களின் முன்னேற்றத்தையும், மனநிலையையும் பதிவு செய்யுங்கள்")
    st.markdown("🌺 காதலோடு, படிப்படியாக வளருங்கள்")
    st.markdown("\nஒரு ஆழ்ந்த மூச்சை விடுங்கள். நீங்கள் சிறந்த முறையில் முயற்சி செய்கிறீர்கள்.")
    st.markdown("---")
    st.markdown("### 👉 மேலும் அறிய சிகிச்சை வகையைத் தேர்ந்தெடுக்கவும்:")

# Show buttons for therapy pages
for filename, label in therapy_pages.items():
    if st.button(label):
        # Set query param so user can navigate from sidebar
        st.experimental_set_query_params(page=filename)
        st.success(f"Now go to the sidebar and click **{label}** to view the page.")
