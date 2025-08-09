import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Short rain animation
rain(emoji="🎲", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page config
st.set_page_config(page_title="Play Therapy", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title
st.title("🎲 Play Therapy")
rain(emoji="🧸", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/l-Jqj3WrrRU?si=vjXrGgB3W5vSVf5F",
    "https://youtu.be/QsPaFzivhc4?si=xPmslYkO8HWHZhEU",
    "https://youtu.be/0yHsPjlYLXs?si=7OkwZUeL69m787pC",
    "https://youtu.be/XQGT3Ux8t4w?si=ngoDHcthCivrrBWG",
    "https://youtu.be/RSF7Qr1tPHw?si=AoZQVmQiBqPfGey0"
]

# ✅ English content
if language == "English":
    st.subheader(f"Welcome {username}! Let’s Explore Play Therapy 🧸")
    st.markdown("#### 💡 *“Play is the highest form of research.” – Albert Einstein*")

    st.markdown("### 🌱 What is Play Therapy?")
    st.markdown("""
    Play Therapy uses **play as a tool for emotional and social development**.  
    It helps children express feelings, build communication skills, and develop problem-solving abilities through fun and structured activities.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Encourages **emotional expression** through play  
    - Builds **social and communication skills**  
    - Improves problem-solving and creativity  
    - Reduces stress and anxiety in children  
    - Strengthens **parent-child bonding**  
    """)

    st.markdown("### 🧩 Fun Play Therapy Activities:")
    st.markdown("""
    - 🧸 **Role-Play Games:** Doctor-patient, teacher-student, shopkeeper  
    - 🎨 **Creative Art:** Painting, coloring, clay modeling  
    - 🧩 **Puzzle Time:** Build problem-solving through jigsaw puzzles  
    - 🏠 **House Play:** Pretend cooking, cleaning, arranging furniture  
    - 🎭 **Emotion Show:** Act out feelings like happy, sad, angry  
    - 🎤 **Storytelling with Toys:** Use puppets to narrate a story  
    - 🎲 **Board Games:** Snakes & Ladders, Ludo – teach patience and rules  
    - 🌳 **Outdoor Play:** Running, sliding, hide and seek for motor skills  
    - 🎵 **Music & Dance:** Free dance and singing sessions to boost mood  
    - 🪁 **Imitation Play:** Copy each other’s actions like mirror game  
    - 🚗 **Toy Car Racing:** Take turns and encourage communication  
    - 🏗️ **Building Blocks:** Build towers and describe them together  
    """)

    st.markdown("### ❤️ Parent Tips for Effective Play Therapy:")
    st.markdown("""
    ✅ **Let the Child Lead:** Join their play instead of controlling it  
    ✅ **Create a Safe Space:** No criticism or judgment during play  
    ✅ **Observe & Learn:** Understand child’s feelings through play behavior  
    ✅ **Model Positive Behavior:** Use toys to teach sharing, kindness  
    ✅ **Keep Sessions Short & Fun:** 20-30 minutes is enough  
    ✅ **Use Play for Communication:** Ask open-ended questions like “What is the doll feeling?”  
    ✅ **Avoid Screens:** Focus on hands-on and interactive games  
    ✅ **Be Consistent:** Make play a daily routine  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Play is not just fun – it’s therapy, bonding, and learning rolled into one. Every game you play helps your child grow emotionally. 💖")

# ✅ Tamil content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! Play Therapy பற்றி அறிந்துகொள்வோம் 🧸")
    st.markdown("#### 💡 *“விளையாட்டு என்பது கற்றலின் உயர்ந்த வடிவம்.” – ஆல்பர்ட் ஐன்ஸ்டீன்*")

    st.markdown("### 🌱 Play Therapy என்றால் என்ன?")
    st.markdown("""
    இந்த சிகிச்சை **விளையாட்டை ஒரு கருவியாகப் பயன்படுத்தி உணர்ச்சி மற்றும் சமூக வளர்ச்சியை ஊக்குவிக்கிறது**.  
    குழந்தைகள் உணர்ச்சிகளை வெளிப்படுத்த, பேச கற்றுக்கொள்ள, மற்றும் பிரச்சினைகளைத் தீர்க்க **விளையாட்டு வழியாக கற்றுக்கொள்வார்கள்**.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - உணர்வுகளை வெளிப்படுத்த உதவும்  
    - சமூக மற்றும் தொடர்பு திறன்கள் மேம்படும்  
    - பிரச்சினை தீர்க்கும் திறன் வளர்க்கும்  
    - மன அழுத்தம் குறையும்  
    - பெற்றோர்-குழந்தை பிணைப்பு வலுப்படும்  
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய விளையாட்டுகள்:")
    st.markdown("""
    - 🧸 **நடிப்பு விளையாட்டு:** டாக்டர், ஆசிரியர், கடை  
    - 🎨 **ஓவியம் & கலை:** வரைவது, நிறமிடுவது, களிமண் வேலை  
    - 🧩 **பஸில் விளையாட்டு:** சிறிய பஸில்களை சேர்த்தல்  
    - 🏠 **வீட்டு விளையாட்டு:** சமையல், சுத்தம், அலங்காரம்  
    - 🎭 **உணர்ச்சி நாடகம்:** மகிழ்ச்சி, சோகம், கோபம் போலி நடிப்பு  
    - 🎤 **கதை நேரம்:** பொம்மைகளைப் பயன்படுத்தி கதைகள் சொல்லுங்கள்  
    - 🎲 **போர்டு விளையாட்டு:** சுறா & ஏணி, லுடோ  
    - 🌳 **வெளியங்காண விளையாட்டு:** ஓடுதல், ஒளிந்துபார்  
    - 🎵 **இசை மற்றும் நடனம்:** பாடல்கள் பாடி, நடனம் செய்யுங்கள்  
    - 🪁 **மிரர் விளையாட்டு:** ஒருவரை ஒருவர் பின்பற்றி செய்யும் விளையாட்டு  
    - 🚗 **கார் பந்தயம்:** மாறி மாறி விளையாடுங்கள்  
    - 🏗️ **கட்டிட விளையாட்டு:** பிளாஸ்டிக் கட்டுகளால் கோபுரம் கட்டுங்கள்  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **குழந்தை வழிநடத்தும் விளையாட்டு செய்யுங்கள்**  
    ✅ **பாதுகாப்பான சூழல் உருவாக்குங்கள்**  
    ✅ **குழந்தையை கவனியுங்கள்**  
    ✅ **நல்ல பழக்கங்களை மாதிரி காட்டுங்கள்**  
    ✅ **சிறிய நேரத்திலேயே செய்யுங்கள்** (20-30 நிமிடம் போதுமானது)  
    ✅ **விளையாட்டின் மூலம் உரையாடுங்கள்**  
    ✅ **மொபைல் & டிவி தவிர்க்கவும்**  
    ✅ **தொடர்ச்சியாக செய்யுங்கள்**  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("விளையாட்டு என்பது பொழுதுபோக்கு மட்டும் அல்ல – அது சிகிச்சை, கற்றல், மற்றும் அன்பு. தினமும் சிறிது நேரம் விளையாடுங்கள். 💖")
