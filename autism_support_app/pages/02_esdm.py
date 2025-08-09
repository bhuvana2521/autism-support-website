import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Rain Animation (short)
rain(emoji="👶", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login Protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page Setup
st.set_page_config(page_title="Early Start Denver Model (ESDM)", layout="centered")

# ✅ Language Selector
if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.radio("Select Language | மொழியைத் தேர்வுசெய்க", ["English", "Tamil"],
                    index=0 if st.session_state.language == "English" else 1)

st.session_state.language = language
username = st.session_state.get("logged_user", "User")

# ✅ Title
st.title("🌟 Early Start Denver Model (ESDM)")

# ✅ Intro + Motivation
if language == "English":
    st.markdown("""
### 👶 What is ESDM?
The Early Start Denver Model (ESDM) is an evidence-based **play-focused early intervention program** for children with autism (12–48 months).

💡 It combines **behavioral principles (ABA)** with **relationship-based developmental strategies**.

🧠 Helps improve **language, social, and cognitive skills** through natural play and joyful interaction.

---

### ✨ Why Try ESDM?
- Builds strong parent-child bonding
- Encourages communication and social skills
- Improves attention, imitation, and interaction

---

> _"Start where the child is, and guide them with love and play."_
    """)
else:
    st.markdown("""
### 👶 ESDM என்றால் என்ன?
Early Start Denver Model (ESDM) என்பது **விளையாட்டு அடிப்படையிலான** சிகிச்சை முறை. இது 12–48 மாத வயதுடைய ஆட்டிசம் குழந்தைகளுக்கான **ஆரம்ப தலையீடு** ஆகும்.

💡 இது **நடத்தை ஆய்வு (ABA)** மற்றும் **உறவுச் சார்ந்த வளர்ச்சி முறைகளை** இணைக்கிறது.

🧠 **மொழி, சமூக மற்றும் அறிவாற்றல் திறன்களை** மகிழ்ச்சியான விளையாட்டின் மூலம் மேம்படுத்துகிறது.

---

### ✨ ஏன் ESDM முக்கியம்?
- பெற்றோர்-குழந்தை உறவை வலுப்படுத்துகிறது
- தொடர்பு மற்றும் சமூக திறனை மேம்படுத்துகிறது
- கவனம், பின்பற்றுதல் மற்றும் விளையாட்டு ஈடுபாட்டை அதிகரிக்கிறது

---

> _"குழந்தையின் நிலையை புரிந்து கொண்டு அன்புடன் வழிகாட்டு."_  
    """)

st.divider()

# ✅ ESDM Activities Section
st.subheader("🏡 " + ("Try These Fun ESDM Activities" if language == "English" else "இந்த சுவாரஸ்யமான ESDM செயல்பாடுகளை முயற்சிக்கவும்"))

activities = [
    ("🎵 Singing rhymes with actions", "🎵 செயல்களுடன் கூடிய பாடல்கள் பாடுதல்"),
    ("🧸 Peek-a-boo and hiding games", "🧸 பூச்சாண்டி மற்றும் மறைவு விளையாட்டுகள்"),
    ("📚 Show & name pictures in books", "📚 புத்தகங்களில் படங்களை காட்டி பெயரிடுதல்"),
    ("🖐️ Pointing and gesturing during play", "🖐️ விளையாட்டின்போது விரல் காட்டுதல் மற்றும் சைகை செய்வது"),
    ("🚗 Toy car rolling back and forth", "🚗 பொம்மை கார் முன்னும் பின்னும் உருட்டுதல்"),
    ("🔊 Sound imitation (animal sounds, claps)", "🔊 ஒலி பின்பற்றுதல் (விலங்கு சத்தம், கைத்தட்டல்)"),
    ("🎨 Drawing together with crayons", "🎨 கிராயான்களுடன் ஓவியம் வரைதல்"),
    ("👀 Eye-contact games while playing", "👀 விளையாடும்போது கண் தொடர்பு விளையாட்டு"),
    ("🍎 Naming fruits and favorite snacks", "🍎 பழங்களையும் பிடித்த ஸ்நாக்ஸ்களையும் பெயரிடுதல்"),
    ("🤝 Turn-taking in simple games", "🤝 எளிய விளையாட்டுகளில் மாறிமாறி விளையாடுதல்")
]

for eng, tam in activities:
    st.checkbox(eng if language == "English" else tam)

st.divider()

# ✅ Parental Tips
st.subheader("❤️ " + ("Parental Tips & Advice" if language == "English" else "பெற்றோருக்கான அறிவுரைகள்"))

if language == "English":
    st.markdown("""
✅ Engage in **playful learning** – learning should feel like a game  
✅ Use **praise and small rewards** for participation  
✅ **Follow the child’s lead** – join their play, don’t force your agenda  
✅ Create **short but frequent sessions** (5–10 mins, multiple times a day)  
✅ Speak **slowly and clearly**, repeat key words  
✅ Include **siblings or family** for more natural interaction  
✅ Celebrate every attempt – even eye contact is a big win  
    """)
else:
    st.markdown("""
✅ **விளையாட்டின் மூலம் கற்றல்** – கற்றல் ஒரு விளையாட்டாக இருக்க வேண்டும்  
✅ **வெகுமதிகளை வழங்குங்கள்** – கைத்தட்டல், சிறிய பரிசு  
✅ **குழந்தையின் விருப்பத்திற்கேற்ப செயல்படுங்கள்** – வற்புறுத்த வேண்டாம்  
✅ **குறுகிய நேரம் ஆனால் அடிக்கடி** (5–10 நிமிடம், தினமும் பலமுறை)  
✅ மெதுவாகவும் தெளிவாகவும் பேசுங்கள்  
✅ **சகோதரர் அல்லது குடும்பத்தினரை** சேர்க்கவும்  
✅ **சிறிய முயற்சிகளையும் பாராட்டுங்கள்** – கண் தொடர்பு கூட ஒரு முன்னேற்றம்  
    """)

st.divider()

# ✅ YouTube Videos
st.subheader("🎥 " + ("Watch ESDM in Action" if language == "English" else "ESDM காணொளிகள்"))

video_links = [
    "https://youtu.be/4hu0ZUr_tqM?si=A81tJovdUkKsEU87",
    "https://youtu.be/dNkd3N6a7cw?si=FoNWOjcGsU6AkND3",
    "https://youtu.be/7lo36qNVrX8?si=5R5Y1yi9QE7Wn0Pr",
    "https://youtu.be/5iUk6vIOmGw?si=-mB2oJ9gjmOfn0G8",
    "https://youtu.be/_AUF8U1xMt8?si=xQIBBjnE00kla2AA",
    "https://youtu.be/S8ee_myXz-U?si=Wj6nTJPpfOg3feND",
    "https://youtu.be/zvKk1CvfzJM?si=N9zJCuU-Lbgaa-bn"
]

for link in video_links:
    st.video(link)

# ✅ End Note
st.markdown("---")
if language == "English":
    st.success("🌈 Every playful moment you share helps your child grow. Keep going!")
else:
    st.success("🌈 ஒவ்வொரு விளையாட்டு தருணமும் உங்கள் குழந்தையின் வளர்ச்சிக்கு உதவும். தொடருங்கள்!")
