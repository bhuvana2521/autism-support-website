import streamlit as st
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🧩",
    font_size=30,
    falling_speed=5,
    animation_length=3
)
# ✅ This protects the page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Set page configuration
st.set_page_config(page_title="DIR/Floortime Therapy", layout="centered")

# ✅ Language selector added
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language

username = st.session_state.get("logged_user", "User")
# ✅ Define video links **before language check**
english_links = [
    "https://youtu.be/ZfJBhjchOUU?si=pTxw_ZvpyvXRYMmc",
    "https://youtu.be/zxlPt1N8KgA?si=i-mt09i03gl68znX",
    "https://youtu.be/rQg9CSTqMQ0?si=MQWl5iEiz7cryer5",
    "https://youtu.be/lbRA2FSMirk?si=TaX2bhawNTjzAzTE",
    "https://youtu.be/gNAS9PskgYI?si=1NJQHyyNfvdjkhDr",
    "https://youtu.be/kl6C3E-RRTE?si=aZe2CZkoiKi9lXZg",
    "https://youtu.be/xzPeMh4M4Ic?si=8_c4ZiwYIYm5gESr",
    "https://youtu.be/MYqRuzBjkis?si=sOIvQlNTE8Acg_H_"
]

# Title and animation
st.title("🧸 DIR/Floortime Therapy")
rain(emoji="🧩", font_size=24, falling_speed=5, animation_length=3)

# Content based on language
if language == "English":
    st.subheader(f"Welcome {username}! Let's Explore DIR/Floortime Therapy 💬")

    st.markdown("### 🌱 What is DIR/Floortime?")
    st.markdown("""
    **DIR/Floortime** (Developmental, Individual-differences, Relationship-based) is a playful and emotional learning approach that helps children grow in their own way. It encourages **love, connection, and joyful interaction**.

    **It’s not about fixing your child. It’s about understanding and connecting.** 💖
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Builds emotional bonding and trust with the child
    - Helps improve attention span and communication
    - Supports social and emotional development
    - Encourages creative thinking through play
    - Flexible and can be done at home by parents!
    """)

    st.markdown("### 🏡 Home Activity Ideas:")
    st.markdown("""
    - 👶 Face-to-face pretend games (doctor-patient, kitchen play)
    - 🎨 Drawing side-by-side and talking about the art
    - 🧸 Role play using soft toys with emotions
    - 💃 Dancing together with your child's favorite music
    - 📚 Reading books and pointing to expressions
    - 🪀 Mirror game (imitate each other's actions)
    """)

    st.markdown("### ❤️ Parent Tips:")
    st.markdown("""
    - Let your child lead the play – follow their interest!
    - Always respond with love and curiosity, not correction
    - Celebrate small moments – even a smile or eye contact is progress
    - Consistency is more important than duration – even 20 minutes a day matters!
    - Your presence is the most powerful tool. 🫶
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    english_links = [
        "https://youtu.be/ZfJBhjchOUU?si=pTxw_ZvpyvXRYMmc",
        "https://youtu.be/zxlPt1N8KgA?si=i-mt09i03gl68znX",
        "https://youtu.be/rQg9CSTqMQ0?si=MQWl5iEiz7cryer5",
        "https://youtu.be/lbRA2FSMirk?si=TaX2bhawNTjzAzTE",
        "https://youtu.be/gNAS9PskgYI?si=1NJQHyyNfvdjkhDr",
        "https://youtu.be/kl6C3E-RRTE?si=aZe2CZkoiKi9lXZg",
        "https://youtu.be/xzPeMh4M4Ic?si=8_c4ZiwYIYm5gESr",
        "https://youtu.be/MYqRuzBjkis?si=sOIvQlNTE8Acg_H_"
    ]
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("You are doing amazing. Every playful moment you spend helps your child grow in love and confidence. Trust the process, and trust your heart. 💗")

# Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! DIR/Floortime சிகிச்சையைப் பற்றி அறிந்துகொள்வோம் 💬")

    st.markdown("### 🌱 DIR/Floortime என்றால் என்ன?")
    st.markdown("""
    **DIR/Floortime** என்பது வளர்ச்சி, தனிப்பட்ட வித்தியாசங்கள் மற்றும் உறவுகள் அடிப்படையிலான சிகிச்சை ஆகும். இது குழந்தையுடன் **அன்பு மற்றும் உணர்வுகள்** அடிப்படையிலான விளையாட்டு வழியாக நடக்கிறது.

    **குழந்தையை மாற்ற அல்ல, புரிந்துகொள்ள தான் இந்த சிகிச்சை.** 💖
    """)

    st.markdown("### 🌟 இதனால் கிடைக்கும் நன்மைகள்:")
    st.markdown("""
    - குழந்தை மற்றும் பெற்றோருக்கிடையிலான நெருக்கம் அதிகரிக்கும்
    - கவனம், தொடர்பு திறன் மேம்படும்
    - சமூக மற்றும் உணர்ச்சி வளர்ச்சிக்கு உதவும்
    - படைப்பாற்றலை ஊக்குவிக்கும்
    - வீட்டிலேயே பெற்றோர் செய்யக்கூடிய சிகிச்சை
    """)

    st.markdown("### 🏡 வீட்டில் செய்யக்கூடிய செயல்கள்:")
    st.markdown("""
    - 👶 கற்பனை விளையாட்டு (டாக்டர்-பேசியன்ட், சமையலறை விளையாட்டு)
    - 🎨 ஓவியம் வரைந்து அதைப் பற்றி பேசுதல்
    - 🧸 பாவைகள் மூலம் உணர்வுகளை வெளிப்படுத்துதல்
    - 💃 இசையுடன் கூடித் துள்ளல்
    - 📚 புத்தகம் வாசித்து முகபாவனைகளை காட்டுதல்
    - 🪀 மிரர் விளையாட்டு (அடிப்படையில் நடனம் போல)
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    - குழந்தையின் ஆசையை பின்பற்றி விளையாடுங்கள்
    - சுட்டிக்காட்டுவது அல்ல, அன்போடு பதிலளியுங்கள்
    - சிறிய முன்னேற்றங்களை கொண்டாடுங்கள்
    - தினசரி 20 நிமிடம் கூட போதுமானது!
    - உங்கள் அன்பும் நேரமும் பெரிய மருந்து! 🫶
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in english_links:
        st.video(link)


    st.markdown("### 🌈 பெற்றோருக்கான ஒரு எழுச்சி செய்தி:")
    st.info("நீங்கள் சிறந்த பெற்றோர். உங்கள் அன்பும், உங்கள் நேரமும் உங்கள் குழந்தையை வளர்க்கும் மிகப்பெரிய சக்தி. நம்பிக்கையுடன் தொடருங்கள். 💗")
