import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Animation
rain(emoji="🏃‍♂️", font_size=30, falling_speed=5, animation_length=3)

# ✅ Protect Page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Page Config
st.set_page_config(page_title="Physical Therapy (PT)", layout="centered")

# ✅ Video Links
english_links = [
    "https://youtu.be/mHUQoICOJAQ?si=wyHYW2Tsn8uoFGvR",
    "https://youtu.be/jMdROoUb0wA?si=zOXiRVUB6QOODiyO",
    "https://youtu.be/E6i2NTuRFn8?si=Ly2PWnh0eI7KTO8k",
    "https://youtu.be/sCAKjuFJpuA?si=VYzWAByZWHK-U5rS",
    "https://youtube.com/shorts/J8sAN02R6no?si=W0MIrXE218lhLLbS"
]

# ✅ Language Selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# Page Title
st.title("🏃‍♂️ Physical Therapy (PT)")
rain(emoji="💪", font_size=24, falling_speed=5, animation_length=3)

# ✅ Content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Explore Physical Therapy 💬")

    st.markdown("#### 💡 *“Strong body, strong confidence.”*")

    st.markdown("### 🌱 What is Physical Therapy?")
    st.markdown("""
    **Physical Therapy (PT)** helps improve **movement, balance, strength, and coordination** in children.  
    It focuses on **gross motor skills**, posture correction, and building muscle strength for daily activities.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **balance and coordination**
    - Strengthens **core and limb muscles**
    - Helps with **walking, running, and posture**
    - Reduces **risk of injuries**
    - Builds **confidence in movement**
    """)

    st.markdown("### 🧩 Fun Physical Therapy Activities at Home:")
    st.markdown("""
    - 🏃 **Running Games:** Short races or chasing games to improve stamina  
    - 🏋️ **Wall Push-Ups:** Great for upper body strength  
    - 🧗 **Climbing Soft Stairs:** Improves leg strength and coordination  
    - ⚽ **Kick the Ball:** Develops balance and leg control  
    - 🧍 **Balance Beam Walk:** Use a straight line on the floor for balance training  
    - 🪁 **Jumping Games:** Jump over cushions or ropes to build agility  
    - 🚴 **Tricycle or Cycle Riding:** Enhances leg strength and coordination  
    - 🧎 **Crawling Through Tunnels:** Improves core strength and motor planning  
    - 🧘 **Yoga Poses:** Tree pose, butterfly pose for flexibility and balance  
    - 🥏 **Throw and Catch Ball:** Hand-eye coordination improvement  
    - 🛞 **Rolling on Exercise Ball:** Builds core strength and balance  
    - 🐸 **Frog Jumps:** Increases leg power and stamina  
    - 🦀 **Crab Walk:** Improves core muscles and shoulder strength  
    - 🪢 **Tug of War:** Builds arm strength and teamwork  
    - 🧦 **Sock Slide Game:** Slide on socks across smooth floor for fun workout  
    """)

    st.markdown("### ❤️ Parent Tips for Physical Therapy Success:")
    st.markdown("""
    ✅ **Keep it Fun** – Turn therapy into playtime  
    ✅ **Use Safe Space** – Ensure a soft mat or carpet for safety  
    ✅ **Encourage, Don’t Force** – Never push too hard, make it enjoyable  
    ✅ **Start Small** – Begin with simple activities and progress slowly  
    ✅ **Consistency is Key** – Daily 15–20 mins is more effective than long sessions  
    ✅ **Involve Siblings** – Make it a family activity for motivation  
    ✅ **Praise Every Effort** – Cheer for trying, not just winning  
    ✅ **Set Routines** – Same time each day builds habit  
    ✅ **Avoid Comparisons** – Every child grows at their own pace  
    ✅ **Celebrate Progress** – Take photos, give rewards for milestones  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Movement is medicine! Every playful step builds confidence and strength. Be patient and keep cheering! 💖")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! உடல் பயிற்சி சிகிச்சையைப் பற்றி அறிந்துகொள்வோம் 💬")

    st.markdown("#### 💡 *“உடல் வலிமை மனவலிமைக்கு அடிப்படை.”*")

    st.markdown("### 🌱 Physical Therapy என்றால் என்ன?")
    st.markdown("""
    **Physical Therapy (PT)** என்பது **நடப்பு, ஓட்டம், சமநிலை, தசை வலிமை** ஆகியவற்றை மேம்படுத்த உதவும் சிகிச்சை.  
    இது **முழு உடல் இயக்கம்** மற்றும் **நிலை திருத்தம்** மூலம் குழந்தைகளின் உடல் வளர்ச்சியை ஊக்குவிக்கிறது.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - **சமநிலை மற்றும் ஒருங்கிணைப்பு மேம்பாடு**
    - **கைகள் மற்றும் கால்களின் தசை வலிமை அதிகரிப்பு**
    - **நடப்பது, ஓடுவது, நிற்பது எளிதாகும்**
    - **காயம் ஏற்படும் அபாயம் குறைவு**
    - **நம்பிக்கை அதிகரிப்பு**
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய உடல் பயிற்சி விளையாட்டுகள்:")
    st.markdown("""
    - 🏃 **ஓட்டப்பந்தயம்:** சிறிய தூர ஓட்டம்  
    - 🏋️ **சுவர் புஷ்-அப்ஸ்:** கைகளின் வலிமை அதிகரிக்கும்  
    - 🧗 **மெத்தை ஏறுதல்:** கால்கள் வலுப்பெறும்  
    - ⚽ **பந்தை அடித்து விளையாடுதல்:** கால்களின் ஒருங்கிணைப்பு  
    - 🧍 **ஒரே கோட்டில் நடப்பது:** சமநிலை பயிற்சி  
    - 🪁 **குதிப்பாட்டுகள்:** துள்ளல் விளையாட்டுகள்  
    - 🚴 **மூன்று சக்கர வண்டி பயணம்:** கால்கள் வலுப்படும்  
    - 🧎 **துழாவல் விளையாட்டு:** வயிற்று தசைகள் வலிமை பெறும்  
    - 🧘 **யோகா ஆசனங்கள்:** மர ஆசனம், பட்டாம்பூச்சி ஆசனம்  
    - 🥏 **பந்து பிடி விளையாட்டு:** கை-கண் ஒருங்கிணைப்பு  
    - 🛞 **பந்தின் மேல் உருண்டல்:** உடல் சமநிலை மேம்பாடு  
    - 🐸 **தவளை குதிப்பு:** கால்வலிமை அதிகரிக்கும்  
    - 🦀 **நண்டு நடை:** வயிற்று மற்றும் தோள் வலிமை  
    - 🪢 **கயிறு இழுக்கும் விளையாட்டு:** கைகள் வலிமை பெறும்  
    - 🧦 **சாக்ஸ் ஸ்லைட் விளையாட்டு:** பொழுதுபோக்கு மற்றும் உடற்பயிற்சி  
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **விளையாட்டு போல பயிற்சி செய்யுங்கள்**  
    ✅ **பாதுகாப்பான இடம் தேர்வு செய்யுங்கள்** – மெத்தை அல்லது கம்பளம் மீது செய்யுங்கள்  
    ✅ **அழுத்தம் கொடுக்காதீர்கள்** – மெதுவாக ஊக்கப்படுத்துங்கள்  
    ✅ **சிறிய செயல்களால் தொடங்குங்கள்**  
    ✅ **தினசரி 15 நிமிடம் செய்யுங்கள்**  
    ✅ **குடும்பத்தினரையும் சேர்த்துக்கொள்ளுங்கள்**  
    ✅ **ஒவ்வொரு முயற்சிக்கும் பாராட்டுங்கள்**  
    ✅ **நேரம் நிர்ணயியுங்கள்** – தினசரி ஒரே நேரத்தில் செய்யுங்கள்  
    ✅ **ஒப்பீடு செய்யாதீர்கள்** – ஒவ்வொரு குழந்தைக்கும் தனித்த முன்னேற்றம்  
    ✅ **சிறிய முன்னேற்றங்களையும் கொண்டாடுங்கள்**  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("ஒவ்வொரு இயக்கமும் ஆரோக்கியத்திற்கும் நம்பிக்கைக்கும் வழிகாட்டும். பொறுமையாக ஊக்கப்படுத்துங்கள்! 💖")
