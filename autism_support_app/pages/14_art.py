import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Short rain animation
rain(emoji="🎨", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page configuration
st.set_page_config(page_title="Art Therapy", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title
st.title("🎨 Art Therapy")
rain(emoji="🖌️", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/EVW2XGJ2Kng?si=HvHeVs6pfWYlcup1",
    "https://youtu.be/Px5wLQqEbwU?si=5TnLVCts5MQ5AFCd",
    "https://youtu.be/w8BYwgUqFm0?si=eu7fFCXwbxTJbKzI",
    "https://youtu.be/w-U9gqWDD0Y?si=ehDG82dtjLG6TtHH",
    "https://youtu.be/ijlBcYVu_7Y?si=4Bwk4x_OQ8DyS6Vf"
]

# ✅ English Content
if language == "English":
    st.subheader(f"Welcome {username}! Let’s Explore Art Therapy 🎨")
    st.markdown("#### 💡 *“Art speaks where words are unable to explain.”*")

    st.markdown("### 🌱 What is Art Therapy?")
    st.markdown("""
    Art Therapy uses **drawing, painting, coloring, and craft** to help children express feelings, build focus, and boost creativity.  
    It's a **fun, stress-free way to develop emotional strength**.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **focus and concentration**  
    - Enhances **creativity and imagination**  
    - Reduces stress and anxiety  
    - Helps **express emotions non-verbally**  
    - Improves **fine motor skills and hand-eye coordination**  
    """)

    st.markdown("### 🎨 Fun Art Activities:")
    st.markdown("""
    - 🖍️ **Coloring Books:** Simple shapes and favorite characters  
    - 🖌️ **Finger Painting:** Explore colors and textures  
    - ✂️ **Paper Collage:** Cut and paste colored papers  
    - 🎭 **Mask Making:** Create happy/sad masks and discuss feelings  
    - 🏠 **Home Objects Art:** Paint old bottles, stones, or pots  
    - 🌈 **Rainbow Drawing:** Use bright colors for positive vibes  
    - 👣 **Footprint Art:** Paint on paper using feet and hands  
    - 🖼️ **Family Portrait:** Draw family members together  
    - 🎨 **Mood Art:** Draw what happiness, sadness, or anger looks like  
    - 📦 **DIY Craft:** Use waste materials to make toys  
    """)

    st.markdown("### ❤️ Parent Tips:")
    st.markdown("""
    ✅ **No judgment!** Let the child express freely  
    ✅ Offer **different colors and textures** to explore  
    ✅ Avoid correcting drawings – it’s about expression, not perfection  
    ✅ Praise effort, not the final picture  
    ✅ Encourage talking about what they drew  
    ✅ Create a **calm art corner at home**  
    ✅ Join them! Art is a great bonding activity  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Art is more than drawing—it’s therapy. Every stroke builds confidence and emotional strength. 🖌️")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! Art Therapy பற்றி அறிந்துகொள்வோம் 🎨")
    st.markdown("#### 💡 *“சொற்கள் சொல்ல முடியாததை கலை பேசுகிறது.”*")

    st.markdown("### 🌱 Art Therapy என்றால் என்ன?")
    st.markdown("""
    ஓவியம், வரைவது, நிறமிடுதல், மற்றும் கைவினை வேலைகள் மூலம் **உணர்ச்சிகளை வெளிப்படுத்தவும், கவனம் அதிகரிக்கவும், படைப்பாற்றலை மேம்படுத்தவும் உதவும் சிகிச்சை** இது.  
    இது **மகிழ்ச்சியான, அழுத்தமற்ற சிகிச்சை** ஆகும்.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - கவனம் மற்றும் ஒருமைப்பாடு அதிகரிக்கும்  
    - படைப்பாற்றல் மற்றும் கற்பனை வளர்ச்சி  
    - மன அழுத்தம் குறையும்  
    - உணர்வுகளை வார்த்தைகளில்லாமல் வெளிப்படுத்த உதவும்  
    - கை-கண் ஒருங்கிணைப்பு மேம்படும்  
    """)

    st.markdown("### 🎨 செய்யக்கூடிய செயல்கள்:")
    st.markdown("""
    - 🖍️ **நிறமிடுதல்:** எளிய படங்களில் நிறமிடுதல்  
    - 🖌️ **விரல் ஓவியம்:** வண்ணங்களுடன் விளையாடுதல்  
    - ✂️ **காகிதக் கலை:** காகிதத்தை வெட்டி ஒட்டுதல்  
    - 🎭 **முகமூடி தயாரித்தல்:** மகிழ்ச்சி/சோக முகமூடிகள்  
    - 🏠 **வீட்டுப் பொருள்களை அலங்கரித்தல்:** பாட்டில், கல், பானை  
    - 🌈 **வானவில் வரைதல்:** பிரகாசமான வண்ணங்கள் பயன்படுத்துதல்  
    - 👣 **கால்/கை தடம் கலை:** காகிதத்தில் தடம் போட்டல்  
    - 🖼️ **குடும்பப் படம்:** குடும்ப உறுப்பினர்களை வரையுங்கள்  
    - 🎨 **உணர்ச்சி ஓவியம்:** மகிழ்ச்சி/சோகம் ஆகியவற்றை வரையுங்கள்  
    - 📦 **கைவினை வேலைகள்:** பழைய பொருட்களால் விளையாட்டு பொருட்கள்  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ குற்றம் சொல்ல வேண்டாம் – சுதந்திரமாக வெளிப்படுத்த விடுங்கள்  
    ✅ நிறங்கள் மற்றும் வெவ்வேறு பொருட்களை வழங்குங்கள்  
    ✅ ஓவியத்தை திருத்த வேண்டாம் – இது ஒரு கலை சிகிச்சை  
    ✅ இறுதி முடிவை விட முயற்சியை பாராட்டுங்கள்  
    ✅ குழந்தை வரைவதை பற்றி பேச ஊக்குவிக்கவும்  
    ✅ வீட்டில் அமைதியான ஓவிய இடம் ஏற்படுத்துங்கள்  
    ✅ சேர்ந்து வரையுங்கள் – இது ஒரு நல்ல பந்த உறவு செயலாகும்  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("கலை என்பது ஓவியம் மட்டுமல்ல, அது சிகிச்சை. ஒவ்வொரு கோடும் உங்கள் குழந்தையின் தன்னம்பிக்கையை வளர்க்கிறது. 🖌️")
