import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Animation
rain(emoji="🗣️", font_size=30, falling_speed=5, animation_length=3)

# ✅ Protect Page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Page Config
st.set_page_config(page_title="Speech and Language Therapy", layout="centered")

# ✅ Video Links
english_links = [
    "https://youtu.be/DOtGK0odCYg?si=ny_xIfAnc4mRdxNo",
    "https://youtu.be/4apZ5qf62kY?si=27KE5oC9jgiSR8Bp",
    "https://youtu.be/y_66HnrDPIQ?si=xMddFPjcFP5uVU8m",
    "https://youtu.be/V9YDDpo9LWg?si=PJHuIgCeQ5zmqT06",
    "https://youtu.be/3mYIDJM1hQM?si=dprIsqeXTDxs61ts"
]

tamil_links = [
    "https://youtu.be/FIeJevnNI-E?si=AMkSxYxOwTbDPfdU",
    "https://youtu.be/-gqQ05pMszw?si=fScL4rpj8D54y2We",
    "https://youtu.be/qzEWquwK3fc?si=hEvYymS3FO6Hd1V3",
    "https://youtu.be/UIh33mLI1fY?si=6GN2v2cUO0ua6TDW",
    "https://youtu.be/sIe6K_KV0ts?si=20A0I2P0Vi7j8fIp",
    "https://youtu.be/Szk0uNC-jfc?si=Sz7m04kTybO-chdG",
    "https://youtu.be/7aCWV16nIeQ?si=AdQc9RbnDRfjjjHc"
]

# ✅ Language Selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# Page Title
st.title("🗣️ Speech and Language Therapy")
rain(emoji="💬", font_size=24, falling_speed=5, animation_length=3)

# ✅ Content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Explore Speech Therapy 💬")

    st.markdown("#### 💡 *“Every word your child says is a step toward confidence.”*")

    st.markdown("### 🌱 What is Speech and Language Therapy?")
    st.markdown("""
    **Speech Therapy** helps children improve their ability to **understand and use language**.  
    It focuses on **speaking, listening, and communicating effectively** using different techniques and exercises.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **pronunciation and clarity**
    - Develops **understanding of words and sentences**
    - Enhances **social communication skills**
    - Builds **confidence in expressing thoughts**
    - Supports **academic and daily communication**
    """)

    st.markdown("### 🏡 Home Strategies:")
    st.markdown("""
    - 📖 Read simple storybooks daily
    - 🗣️ Encourage your child to **name objects around them**
    - 🎶 Sing nursery rhymes with actions
    - 📱 Use picture cards to improve vocabulary
    - 👄 Practice **lip and tongue exercises** (like blowing bubbles)
    """)

    st.markdown("### 🧩 Fun Activities for Speech at Home:")
    st.markdown("""
    - 🎤 **Mirror Talk:** Stand with your child in front of a mirror and repeat words together
    - 🧸 **Toy Naming Game:** Pick toys and name them out loud
    - 🗣️ **Sound Imitation Game:** Make animal sounds and ask your child to repeat
    - 📚 **Story Time Q&A:** After reading, ask simple questions like “Who is this?”
    - 🎶 **Song with Gestures:** Sing and act out rhymes
    - 🍎 **Snack Talk:** Name each food item before eating
    """)

    st.markdown("### ❤️ Parent Tips:")
    st.markdown("""
    - Speak slowly and clearly with your child
    - Use gestures along with words to help understanding
    - Avoid correcting too often – encourage and praise instead
    - Give time for your child to respond
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Every small word your child speaks is a victory. Celebrate progress, not perfection. 💖")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! Speech Therapy பற்றிப் பார்ப்போம் 💬")

    st.markdown("#### 💡 *“குழந்தையின் ஒவ்வொரு சொலும் ஒரு நம்பிக்கை.”*")

    st.markdown("### 🌱 Speech Therapy என்றால் என்ன?")
    st.markdown("""
    **Speech Therapy** என்பது குழந்தைகளின் **பேச்சுத்திறன் மற்றும் தொடர்புத்திறனை மேம்படுத்தும் சிகிச்சை** ஆகும்.  
    இதில் **வாக்கியம் பேசுதல், கேட்பது, புரிந்து கொள்ளுதல்** போன்ற பயிற்சிகள் இடம்பெறும்.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - **உச்சரிப்பு மற்றும் தெளிவுத்திறன் மேம்பாடு**
    - **சொற்களையும் வாக்கியங்களையும் புரிந்து கொள்ளும் திறன்**
    - **சமூக தொடர்பு திறன் அதிகரிப்பு**
    - **நம்பிக்கையுடன் பேசும் திறன் வளர்ச்சி**
    - **கல்வி மற்றும் தினசரி தொடர்பில் முன்னேற்றம்**
    """)

    st.markdown("### 🏡 வீட்டில் செய்யக்கூடிய முறைகள்:")
    st.markdown("""
    - 📖 தினசரி கதைகள் வாசிக்கவும்
    - 🗣️ வீட்டில் இருக்கும் பொருட்களின் பெயர்களைச் சொல்லச் செய்யுங்கள்
    - 🎶 பாடல்களையும் ஆட்டங்களையும் ஒன்றாக செய்யுங்கள்
    - 📱 பட அட்டைகள் மூலம் சொற்களை கற்றுக்கொடுங்கள்
    - 👄 உதடு மற்றும் நாக்கு பயிற்சிகள் செய்யுங்கள் (பப்ள் ஊதுதல் போன்றவை)
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய விளையாட்டுகள்:")
    st.markdown("""
    - 🎤 **மிரர் பேச்சு:** கண்ணாடி முன்னால் நின்று சொற்களைச் சொல்லுங்கள்
    - 🧸 **பொம்மைப் பெயரிடும் விளையாட்டு:** பொம்மைகளின் பெயரைச் சொல்லச் செய்யுங்கள்
    - 🗣️ **ஒலி பின்பற்றல்:** விலங்கு ஒலிகளைச் செய்து குழந்தை பின்பற்றச் செய்யுங்கள்
    - 📚 **கதை கேள்வி:** கதை முடிந்த பிறகு “இவர் யார்?” போன்ற கேள்விகளை கேளுங்கள்
    - 🎶 **இசையுடன் சைகை:** பாடல்களைச் சைகையுடன் பாடுங்கள்
    - 🍎 **சிற்றுண்டி உரையாடல்:** உணவு சாப்பிடும் முன் பெயர்களைச் சொல்லுங்கள்
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    - மெதுவாகவும் தெளிவாகவும் பேசுங்கள்
    - சொற்களுடன் சைகைகளையும் பயன்படுத்துங்கள்
    - குறைவாக திருத்துங்கள் – பாராட்டுங்கள்
    - பதிலளிக்க நேரம் கொடுங்கள்
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in tamil_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("குழந்தையின் ஒவ்வொரு சிறிய சொலும் ஒரு பெரிய முன்னேற்றம். கொண்டாடுங்கள்! 💖")
