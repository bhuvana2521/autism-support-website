import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Rain Animation
rain(emoji="📚", font_size=30, falling_speed=5, animation_length=3)

# ✅ Protect Page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Page Config
st.set_page_config(page_title="TEACCH Therapy", layout="centered")

# ✅ Define Video Links (English)
english_links = [
    "https://youtu.be/MmZdQOZnkbs?si=JicvDKSMV5kEShj5",
    "https://youtu.be/JDixL6m3ppc?si=zqzRcJaMATMPco2m",
    "https://youtu.be/NzQKpcHpnGE?si=tlhOSLbx6Q3QSGzd",
    "https://youtu.be/LCh2R-4JLTE?si=JsR1c65JF9wCYjzx",
    "https://youtu.be/MEEr8GmzDcA?si=dIQj6YqNWFCjolA3",
    "https://youtu.be/vkymZzmg4jw?si=USCjqU_b-UzJN6kW"
]

# ✅ Language Selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# Title + Rain Effect
st.title("📅 TEACCH – Structured Teaching")
rain(emoji="📋", font_size=24, falling_speed=5, animation_length=3)

# ✅ Content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Learn About TEACCH 💬")

    st.markdown("#### 💡 *“Structure is the bridge to independence.”*")

    st.markdown("### 🌱 What is TEACCH?")
    st.markdown("""
    **TEACCH** stands for *Treatment and Education of Autistic and related Communication-Handicapped Children*.  
    It uses **structured teaching** methods like visual schedules, work systems, and clear routines to make learning predictable and reduce anxiety.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Builds **independence and confidence**
    - Reduces **stress and confusion** for the child
    - Improves **communication using visuals**
    - Supports **learning at home and school**
    - Encourages **predictable routines**
    """)

    st.markdown("### 🏡 Home Strategies:")
    st.markdown("""
    - 🖼 Use **visual schedules** (pictures of daily activities)
    - 🧩 Organize toys and materials in labeled boxes
    - 📋 Create **‘Work-Break-Work’ systems** for tasks
    - 🏡 Maintain consistent daily routines
    - ✅ Give clear, simple instructions with visual cues
    """)

    st.markdown("### 🧩 Fun Activities for TEACCH at Home:")
    st.markdown("""
    - 📦 **Sorting Activity:** Ask your child to sort toys by color or size into labeled boxes
    - 🖼 **Visual Schedule Matching:** Print activity cards and let the child arrange them in order
    - 🧃 **Snack Time Routine:** Use pictures to show steps (Take plate → Take snack → Sit → Eat)
    - 🎨 **Color Coding:** Assign colors to daily tasks (Red = Bath, Blue = Meal)
    - 📚 **Story Sequencing:** Give story cards and help arrange them in correct order
    - 🏠 **Room Labels:** Label items at home (Door, Chair, Table) and let your child match pictures
    """)

    st.markdown("### ❤️ Parent Tips:")
    st.markdown("""
    - Consistency is key – follow the schedule daily
    - Celebrate small successes with positive reinforcement
    - Reduce distractions during learning time
    - Use **visual reminders** instead of verbal repetition
    """)

    st.markdown("### 📅 Sample Daily Routine:")
    st.info("☀️ Morning – Breakfast → 🧩 Play → 📚 Learning → 🍎 Snack → 🎨 Art → 🛏 Nap")

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Every small step towards structure is a big step towards independence. You are doing amazing! 💖")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! TEACCH சிகிச்சையைப் பற்றி அறிந்துகொள்வோம் 💬")

    st.markdown("#### 💡 *“ஒழுங்கான நடைமுறைகள் சுயநிறைவை அதிகரிக்கும்.”*")

    st.markdown("### 🌱 TEACCH என்றால் என்ன?")
    st.markdown("""
    **TEACCH** என்பது Autism குழந்தைகளுக்கான **ஒழுங்கமைக்கப்பட்ட கற்றல் முறையாகும்**.  
    இதில் **படங்களுடன் கூடிய அட்டவணைகள், விளையாட்டு ஒழுங்கு, பணிச்செய்யும் முறை** போன்றவை பயன்படுத்தப்படுகிறது.
    """)

    st.markdown("### 🌟 இதனால் கிடைக்கும் நன்மைகள்:")
    st.markdown("""
    - குழந்தைக்கு **சுயநிறைவு மற்றும் நம்பிக்கை**
    - **கவலை குறைவு, தெளிவு அதிகம்**
    - **படங்களால் தொடர்பு மேம்பாடு**
    - **வீட்டிலும் பள்ளியிலும் கற்றல் சுலபம்**
    - **முன்னறிவிப்பு அட்டவணைகள் மூலம் நிம்மதி**
    """)

    st.markdown("### 🏡 வீட்டில் செய்யக்கூடிய முறைகள்:")
    st.markdown("""
    - 🖼 **பட அட்டவணைகள்** அமைக்கவும் (காலை, மதியம், மாலை)
    - 🧩 பொம்மைகள் மற்றும் பொருட்களை **லேபிள் போட்டு ஒழுங்கமைக்கவும்**
    - 📋 **‘பணி-இடைவேளை-பணி’** முறையைப் பின்பற்றவும்
    - 🏡 தினசரி **அதே அட்டவணையைப்** பின்பற்றவும்
    - ✅ **எளிய விளக்கங்களும் படங்களும்** பயன்படுத்தவும்
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய விளையாட்டுகள்:")
    st.markdown("""
    - 📦 **வகைப்படுத்தும் விளையாட்டு:** பொம்மைகளை நிறம் அல்லது அளவு அடிப்படையில் பிரித்து ஒழுங்கமைக்கச் சொல்லுங்கள்
    - 🖼 **பட அட்டவணை விளையாட்டு:** அட்டைகளை கொடுத்து, செயல்களின் வரிசையை அமைக்கச் செய்யுங்கள்
    - 🧃 **சிற்றுண்டி நடைமுறை:** (பிளேட் எடு → சிற்றுண்டி எடு → உட்கார் → சாப்பிடு) என்ற படங்களை பயன்படுத்துங்கள்
    - 🎨 **நிற குறியீடு:** தினசரி செயல்களுக்கு நிறங்களை கொடுங்கள் (சிகப்பு = குளியல், நீலம் = உணவு)
    - 📚 **கதை அட்டைகள்:** கதை அட்டைகளை கொடுத்து சரியான வரிசையில் அமைக்கச் செய்யுங்கள்
    - 🏠 **வீட்டுப் பொருட்கள் பெயரிடுதல்:** (கதவு, நாற்காலி, மேசை) போன்றவற்றை லேபிள் போடுங்கள்
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    - தினசரி ஒரே மாதிரி அட்டவணை பழக்கப்படுத்துங்கள்
    - சிறிய முன்னேற்றங்களை கொண்டாடுங்கள்
    - கற்றல் நேரத்தில் கவனச்சிதறலை தவிர்க்கவும்
    - **வாக்கியம் கூறுவதற்கு பதில் படங்கள் காட்டவும்**
    """)

    st.markdown("### 📅 ஒரு நாள் அட்டவணை உதாரணம்:")
    st.info("☀️ காலை – காலை உணவு → 🧩 விளையாட்டு → 📚 கற்றல் → 🍎 சிற்றுண்டி → 🎨 ஓவியம் → 🛏 ஓய்வு")

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஒரு எழுச்சி செய்தி:")
    st.info("ஒழுங்கமைக்கப்பட்ட ஒவ்வொரு படியும் உங்கள் குழந்தைக்கு சுயநிறைவை தரும். நீங்கள் சிறந்த பெற்றோர்! 💖")
