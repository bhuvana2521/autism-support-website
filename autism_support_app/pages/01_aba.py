import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Rain Animation (short)
rain(emoji="🧠", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login Protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page Configuration
st.set_page_config(page_title="ABA Therapy", layout="centered", page_icon="🧠")

# ✅ Language Selection
language = st.radio("Select Language | மொழியைத் தேர்வுசெய்க", ["English", "Tamil"], horizontal=True)

# ✅ Title and Motivational Quote
if language == "English":
    st.title("🧠 Applied Behavior Analysis (ABA) Therapy")
    st.markdown("💬 *“Every small step is progress. Celebrate your child’s wins!”*")
else:
    st.title("🧠 செயல்முறை நடத்தை பகுப்பாய்வு (ABA) சிகிச்சை")
    st.markdown("💬 *“ஒவ்வொரு சிறிய முன்னேற்றமும் ஒரு வெற்றிதான். அதை கொண்டாடுங்கள்!”*")

st.divider()

# ✅ What is ABA Therapy
if language == "English":
    with st.expander("📘 What is ABA Therapy?"):
        st.write("""
Applied Behavior Analysis (ABA) helps children learn positive behaviors and reduce unwanted behaviors through structured techniques.

- Focus on **reward-based learning**
- Break skills into **simple steps**
- Encourage **communication & social interaction**
- Used **at home, school, or therapy centers**
        """)
else:
    with st.expander("📘 ABA சிகிச்சை என்றால் என்ன?"):
        st.write("""
ABA என்பது **நேர்மறை நடத்தைகளை கற்றுக்கொடுக்கவும், எதிர்மறை நடத்தைகளை குறைக்கவும்** உதவும் ஒரு சிகிச்சை முறை.

- வெகுமதி அடிப்படையிலான கற்றல்
- சிக்கலான திறன்களை **சிறிய படிகளாக** பிரித்தல்
- **தொடர்பு மற்றும் சமூக உறவுகளை** ஊக்குவித்தல்
- வீட்டிலும் பள்ளியிலும் பயன்படுத்தப்படுகிறது
        """)

# ✅ Key Principles
st.subheader("🔑 " + ("Key ABA Principles" if language == "English" else "முக்கிய ABA கொள்கைகள்"))
principles = [
    ("✅ Positive Reinforcement", "✅ நேர்மறை ஊக்குவிப்பு"),
    ("✅ Step-by-Step Learning", "✅ படிப்படியாக கற்றல்"),
    ("✅ Consistency & Routine", "✅ தொடர்ச்சியும் ஒழுங்கும்"),
    ("✅ Behavior Tracking & Notes", "✅ நடத்தை கண்காணிப்பு மற்றும் குறிப்புகள்"),
    ("✅ Parent Involvement is Key", "✅ பெற்றோர் பங்கேற்பு முக்கியம்")
]
for en, ta in principles:
    st.markdown(en if language == "English" else ta)

st.divider()

# ✅ Activities Section
st.subheader("📝 " + ("Try These ABA Activities" if language == "English" else "இந்த ABA செயல்பாடுகளை முயற்சிக்கவும்"))

activities = [
    ("👏 Imitation Game (Clap hands, wave)", "👏 நடிப்பு விளையாட்டு (கைத்தட்டல், கைகாட்டுதல்)"),
    ("🍎 Naming Common Objects", "🍎 பொருட்களின் பெயரை சொல்லுதல்"),
    ("🔷 Sorting Shapes and Colors", "🔷 வடிவங்களையும் நிறங்களையும் வரிசைப்படுத்துதல்"),
    ("🗣️ Practicing One-step Commands", "🗣️ ஒரே கட்டளை பயிற்சி"),
    ("👀 Eye Contact Training", "👀 கண் தொடர்பு பயிற்சி"),
    ("🎶 Singing Action Songs", "🎶 செயல் பாடல்கள் பாடுதல்"),
    ("🧩 Puzzle Matching", "🧩 புதிர் பொருத்துதல்"),
    ("🚗 Toy Play Turn Taking", "🚗 பொம்மையுடன் மாறி விளையாடுதல்"),
    ("📚 Point and Name Pictures in a Book", "📚 புத்தகத்தில் படங்களை காட்டி பெயரிடுதல்"),
    ("🥄 Feeding Practice Using Spoons", "🥄 ஸ்பூன் பயன்படுத்தி உணவளித்தல்")
]

for en, ta in activities:
    st.checkbox(en if language == "English" else ta)

# ✅ Extra Suggestion for Parents
st.subheader("❤️ " + ("Parental Tips & Advice" if language == "English" else "பெற்றோருக்கான குறிப்புகள் மற்றும் அறிவுரை"))
if language == "English":
    st.markdown("""
✅ **Be consistent** – Repeat activities daily at the same time  
✅ Use **praise and small rewards** (claps, stickers, favorite snacks)  
✅ Keep **sessions short (5-10 mins)** but frequent  
✅ Avoid scolding – use **gentle correction and redirection**  
✅ Track progress in a notebook – celebrate improvements  
✅ Turn learning into **playful games**  
✅ Stay patient – progress takes time, every small step matters  
    """)
else:
    st.markdown("""
✅ **தொடர்ச்சியாக பயிற்சி செய்யுங்கள்** – தினமும் ஒரே நேரத்தில் செய்க  
✅ சிறிய **வெகுமதிகளை வழங்குங்கள்** (கைத்தட்டல், ஸ்டிக்கர்கள், சிறு ஸ்நாக்ஸ்)  
✅ **குறுகிய நேரம் (5-10 நிமிடங்கள்)** பயிற்சி, ஆனால் அடிக்கடி  
✅ கோபப்பட வேண்டாம் – மென்மையான திருத்தம் பயன்படுத்துங்கள்  
✅ முன்னேற்றத்தை **குறிப்பேட்டில் பதிவு செய்யுங்கள்**  
✅ கற்றலை **விளையாட்டாக மாற்றுங்கள்**  
✅ பொறுமையாக இருங்கள் – சிறிய முன்னேற்றமும் முக்கியம்  
    """)

st.divider()

# ✅ Video Section
if language == "English":
    st.subheader("🎥 Watch ABA in Action (English)")
    english_videos = [
        "https://youtu.be/eQ0W86jCN74?si=G3OOkF2kZHaoOFHX",
        "https://youtu.be/-CpsFm6USIE?si=fvr70MGNmHSBb5H2",
        "https://youtu.be/BMDm-q4EGN0?si=RR6D0G6eud7j6MQv",
        "https://youtu.be/YnI7kag0ALE?si=dqcZvdbXxXPDxqzj",
        "https://youtu.be/eLwrqbCXs3w?si=rbbNt4smC3suk5kj"
    ]
    for link in english_videos:
        st.video(link)
else:
    st.subheader("🎥 ABA பயிற்சி காணொளி (Tamil)")
    tamil_videos = [
        "https://youtu.be/_JlIuUKoDwI?si=nL59F_4s3o4fXMNR",
        "https://youtu.be/uIoLqPoT5TI?si=ZPtRWsyuOcME7J_z"
    ]
    for link in tamil_videos:
        st.video(link)

# ✅ Footer
st.markdown("---")
if language == "English":
    st.markdown("🌟 *You are your child’s best teacher. Keep going with love and patience!*")
else:
    st.markdown("🌟 *உங்கள் குழந்தைக்கு சிறந்த ஆசிரியர் நீங்கள் தான். அன்புடனும் பொறுமையுடனும் தொடருங்கள்!*")
