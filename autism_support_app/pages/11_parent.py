import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Short rain animation
rain(emoji="👨‍👩‍👦", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page config
st.set_page_config(page_title="Parent-Mediated Therapy", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title
st.title("👨‍👩‍👦 Parent-Mediated Therapy")
rain(emoji="💖", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/fDsEEGL9KEQ?si=0ahnQfMw6XE_dQDO",
    "https://youtu.be/WyqZMeGY8j4?si=vQu82sjog6BKI9tM",
    "https://youtu.be/un4pPSbCGJg?si=BzwIWmkofmmLSmWn",
    "https://youtu.be/JYPeOm5A8XQ?si=nrC4S_RdrvdSkLGO",
    "https://youtu.be/n3utxIP0j8g?si=ni9YYY2iVWiH3hwh",
    "https://youtu.be/BkJvtWNqe80?si=oEwT4_JVxFD3x7e1"
]

# ✅ English content
if language == "English":
    st.subheader(f"Welcome {username}! Empower Yourself with Parent-Mediated Therapy 💡")
    st.markdown("#### 💡 *“Parents are the first and best teachers a child can have.”*")

    st.markdown("### 🌱 What is Parent-Mediated Therapy?")
    st.markdown("""
    Parent-Mediated Therapy trains parents to deliver therapy strategies during everyday activities.  
    You become your child’s **coach, play partner, and biggest supporter**.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Strengthens **parent-child bonding**  
    - Provides **continuous learning at home**  
    - Reduces stress and behavioral challenges  
    - Empowers parents to **feel confident and in control**  
    - Cost-effective and highly personalized  
    """)

    st.markdown("### 🧩 Fun Activities Parents Can Do Daily:")
    st.markdown("""
    - 🎵 **Sing Together:** Use nursery rhymes with actions  
    - 🎲 **Play Turn-Taking Games:** Rolling a ball back and forth  
    - 📚 **Story Time with Expression:** Point to pictures, ask “What is this?”  
    - 🧸 **Role Play:** Pretend doctor, shopkeeper, teacher  
    - 🍎 **Snack Time Communication:** Ask child to request “more” or “juice”  
    - 🖼️ **Emotion Show:** Show happy, sad, angry faces and name them  
    - 🎨 **Art Together:** Coloring and naming objects  
    - 🧠 **Puzzle Challenge:** Solve simple puzzles while talking  
    - 🛍️ **Shopping Helper:** Let child hand over money or pick items  
    - 🏠 **Daily Chores Together:** Folding clothes, setting the table  
    - 🎤 **Speech Practice:** Repeat words in fun tone during play  
    - 🕺 **Dance Together:** Use favorite songs to improve movement and bonding  
    """)

    st.markdown("### ❤️ Parent Tips for Success:")
    st.markdown("""
    ✅ **Set Realistic Goals:** Focus on small, achievable steps  
    ✅ **Use Everyday Moments:** Meal time, bath time, play time  
    ✅ **Model Behavior:** Show the action you want them to learn  
    ✅ **Keep it Fun:** Make therapy playful and stress-free  
    ✅ **Follow the Child’s Lead:** Join their play, don’t force  
    ✅ **Consistency is Key:** Short, frequent sessions every day  
    ✅ **Stay Positive:** Praise every attempt, no matter how small  
    ✅ **Ask for Guidance:** Regularly check with therapists for new strategies  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("You are your child’s hero. Every small effort you make shapes a lifetime of progress. 💖")

# ✅ Tamil content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! பெற்றோர் வழிநடத்தும் சிகிச்சையை அறிந்துகொள்வோம் 💡")
    st.markdown("#### 💡 *“பெற்றோர் தான் குழந்தையின் முதல் சிறந்த ஆசிரியர்.”*")

    st.markdown("### 🌱 Parent-Mediated Therapy என்றால் என்ன?")
    st.markdown("""
    இந்த சிகிச்சை, பெற்றோர்கள் **தினசரி செயல்களில் சிகிச்சை முறைகளைப் பயன்படுத்த கற்றுக்கொடுக்கிறது**.  
    நீங்கள் உங்கள் குழந்தையின் **பயிற்சி ஆசிரியரும், விளையாட்டு தோழனும், ஊக்குவிப்பவரும்** ஆவீர்கள்.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - பெற்றோர்-குழந்தை நெருக்கம் அதிகரிக்கும்  
    - வீட்டிலேயே தொடர்ச்சியான கற்றல்  
    - அழுத்தம் மற்றும் நடத்தை சிக்கல்கள் குறையும்  
    - பெற்றோருக்கு நம்பிக்கை மற்றும் கட்டுப்பாடு  
    - குறைந்த செலவு, தனிப்பட்ட பயிற்சி  
    """)

    st.markdown("### 🧩 பெற்றோர் செய்யக்கூடிய தினசரி விளையாட்டுகள்:")
    st.markdown("""
    - 🎵 **பாடல்கள் பாடுங்கள்:** அசைவுகளுடன் கூடிய பாடல்கள்  
    - 🎲 **மாறிமாறி விளையாடுங்கள்:** பந்து உருட்டுதல்  
    - 📚 **கதை நேரம்:** படங்களை காட்டி “இது என்ன?” என்று கேளுங்கள்  
    - 🧸 **நடிப்பு விளையாட்டு:** டாக்டர், கடை, ஆசிரியர்  
    - 🍎 **சிற்றுண்டி நேரம்:** “மேலும்” அல்லது “ஜூஸ்” என்று கேட்க ஊக்குவிக்கவும்  
    - 🖼️ **உணர்ச்சி விளையாட்டு:** மகிழ்ச்சி, துக்கம், கோபம் முகபாவனைகள் காட்டுங்கள்  
    - 🎨 **ஓவியம்:** வண்ணங்களைப் பற்றி பேசுங்கள்  
    - 🧠 **பஸில்:** சுலபமான புதிர் விளையாட்டுகள்  
    - 🛍️ **ஷாப்பிங் உதவி:** குழந்தையை பொருட்கள் எடுக்கச் சொல்லுங்கள்  
    - 🏠 **வீட்டு வேலைகள்:** துணி மடித்தல், மேஜை அமைத்தல்  
    - 🎤 **சொற்கள் பயிற்சி:** விளையாட்டு நேரத்தில் வார்த்தைகளை மீண்டும் சொல்லுங்கள்  
    - 🕺 **டான்ஸ் செய்யுங்கள்:** பிடித்த பாடல்களில் நடனம்  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **சிறிய இலக்குகள் அமைக்கவும்**  
    ✅ **அன்றாட நேரங்களை பயன்படுத்தவும்**  
    ✅ **மாதிரி காட்டுங்கள்**  
    ✅ **விளையாட்டாக செய்யுங்கள்**  
    ✅ **குழந்தையின் விருப்பத்திற்கு ஏற்ப செயல்படுங்கள்**  
    ✅ **தொடர்ச்சியாக செய்யுங்கள்**  
    ✅ **ஒவ்வொரு முயற்சியையும் பாராட்டுங்கள்**  
    ✅ **சிகிச்சை நிபுணர்களிடம் ஆலோசனை பெறுங்கள்**  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("நீங்கள் உங்கள் குழந்தையின் ஹீரோ. உங்கள் ஒவ்வொரு சிறிய முயற்சியும் பெரும் வெற்றியை உருவாக்கும். 💖")
