import streamlit as st
from streamlit_extras.let_it_rain import rain



# ✅ Protect Page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Page Config
st.set_page_config(page_title="Occupational Therapy", layout="centered")

# ✅ Video Links
english_links = [
    "https://youtu.be/OtohyMJTIy8?si=AvudDW2m1MUPvEKc",
    "https://youtu.be/37qPEWQMQa4?si=KpJq5XtChRZBJGnE",
    "https://youtu.be/12k0XUCKzbk?si=mRHuOfNY6jQnXCza",
    "https://youtu.be/YgRizhh36lw?si=c9fROFvsMuHh4Upd",
    "https://youtu.be/tNPQOLkLmhs?si=W_k0fy9V2gQp8lTo"
]

tamil_links = [
    "https://youtu.be/EPyKBe8ZaMo?si=HiAs5CMmdUn91t1Z",
    "https://youtu.be/kAyAkKzhJUc?si=xNVFK6n9SdRfYcQg",
    "https://youtu.be/d0BeMfpF0rM?si=mTU179uy_KPVZrGm",
    "https://youtu.be/0ZCm-j319vA?si=Y7BohDhPDbybpbUw",
    "https://youtu.be/TdsDbmI3irc?si=QutzTPOpVf-6R2RA",
    "https://youtu.be/GQNnhzku4FM?si=yfrHS440r0J1IkQg"
]

# ✅ Language Selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# Page Title
st.title("🖐️ Occupational Therapy (OT)")
rain(emoji="🎨", font_size=24, falling_speed=5, animation_length=3)

# ✅ Content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Explore Occupational Therapy 💬")

    st.markdown("#### 💡 *“Every activity is a step toward independence.”*")

    st.markdown("### 🌱 What is Occupational Therapy?")
    st.markdown("""
    **Occupational Therapy (OT)** helps children develop **daily life skills** like dressing, eating, writing, and coordination.  
    It improves **fine motor skills, sensory processing, and independence** through structured activities.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **hand-eye coordination**
    - Enhances **fine and gross motor skills**
    - Helps with **sensory processing challenges**
    - Builds **self-care and independence**
    - Improves **focus and attention**
    """)

    st.markdown("### 🧩 Fun Activities for OT at Home:")
    st.markdown("""
    - 🎨 **Finger Painting:** Enhances creativity and sensory awareness
    - 🧩 **Puzzle Time:** Improves problem-solving and coordination
    - ✂️ **Cutting Shapes:** Practice with child-safe scissors
    - 🏗 **Block Building:** Develops balance and fine motor skills
    - 🍝 **Play with Dough:** Strengthens hand and finger muscles
    - 🖌️ **Color Inside Lines:** Improves attention and precision
    - 🥢 **Using Spoon & Chopsticks:** Improves grip and control
    - 👕 **Buttoning and Zipping:** Builds dressing independence
    - 📦 **Sorting Objects by Size/Color:** Develops visual-motor skills
    - 🧺 **Laundry Folding:** Promotes sequencing and hand coordination
    - 🏐 **Ball Catch & Throw Games:** Enhances gross motor skills
    - 🖐️ **Clothespin Games:** Improves finger strength and dexterity
    - 🧃 **Squeezing Sponge in Water:** Builds hand muscles and control
    - 🪁 **Paper Airplane Making:** Boosts creativity and motor planning
    """)

    st.markdown("### ❤️ Parent Tips for OT Success:")
    st.markdown("""
    ✅ **Make Therapy Fun** – Turn activities into games, not tasks  
    ✅ **Follow Child's Interest** – Use favorite colors, toys, or characters  
    ✅ **Start Simple** – Break tasks into **small, achievable steps**  
    ✅ **Give Choices** – Let them choose between 2 activities  
    ✅ **Model First** – Show how it’s done and encourage imitation  
    ✅ **Avoid Pressure** – Praise effort, not perfection  
    ✅ **Involve Daily Life** – Include child in chores like cooking, setting table  
    ✅ **Be Patient & Consistent** – Progress takes time  
    ✅ **Celebrate Small Wins** – Acknowledge every tiny improvement  
    ✅ **Use Positive Reinforcement** – Stickers, claps, and verbal praise  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in english_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Every small action your child achieves is a BIG success. Your love and patience make all the difference. 💖")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! Occupational Therapy பற்றி அறிந்துகொள்வோம் 💬")

    st.markdown("#### 💡 *“ஒவ்வொரு செயலும் சுயநிறைவை நோக்கி ஒரு படி.”*")

    st.markdown("### 🌱 Occupational Therapy என்றால் என்ன?")
    st.markdown("""
    **Occupational Therapy (OT)** என்பது குழந்தைகளின் **தினசரி வாழ்க்கைத் திறன்களை மேம்படுத்தும் சிகிச்சை** ஆகும்.  
    இதில் **உடல் இயக்கம், நுண்ணறிவு திறன், உணர்வுகளை சரிசெய்தல்** ஆகியவற்றை வளர்க்கும் பயிற்சிகள் இடம்பெறும்.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - **கைகள் மற்றும் கண் ஒருங்கிணைப்பு மேம்பாடு**
    - **நுண்ணிய மற்றும் பெரிய இயக்கத் திறன் வளர்ச்சி**
    - **உணர்வு சீரமைப்பு திறன் மேம்பாடு**
    - **சுய பராமரிப்பு மற்றும் சுயநிறைவு**
    - **கவனம் மற்றும் ஒருமைப்பாடு அதிகரிப்பு**
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய விளையாட்டுகள்:")
    st.markdown("""
    - 🎨 **விரல் ஓவியம்:** படைப்பாற்றல் மற்றும் உணர்வு விழிப்புணர்ச்சி மேம்பாடு  
    - 🧩 **புதிர் விளையாட்டு:** பிரச்சினை தீர்க்கும் திறன் மற்றும் கைகளை வலுப்படுத்தும்  
    - ✂️ **வடிவங்களை வெட்டுதல்:** பாதுகாப்பான கத்தரிக்கோல் கொண்டு வெட்டுங்கள்  
    - 🏗 **கட்டிட விளையாட்டு:** கட்டங்களை அடுக்கி சமநிலை மற்றும் ஒருங்கிணைப்பை வளர்க்கும்  
    - 🍝 **மாவு விளையாட்டு:** கைகளின் வலிமையை அதிகரிக்க வடிவங்களை உருவாக்குங்கள்  
    - 🖌️ **வரையருகில் நிறமிடுதல்:** கவனம் மற்றும் துல்லியத்தை மேம்படுத்தும்  
    - 🥢 **ஸ்பூன் மற்றும் குச்சி பயிற்சி:** பிடிப்பு மற்றும் கட்டுப்பாட்டை மேம்படுத்தும்  
    - 👕 **பட்டன் போடுதல், சிப்பை பூட்டுதல்:** சுய பராமரிப்பு திறனை வளர்க்கும்  
    - 📦 **பொருட்களை அளவின்படி அடுக்குதல்:** காட்சி திறனை மேம்படுத்தும்  
    - 🧺 **ஆடைகளை மடித்தல்:** வரிசை மற்றும் ஒழுங்கு கற்றுத்தரும்  
    - 🏐 **பந்து விளையாட்டு:** பெரிய இயக்க திறனை மேம்படுத்தும்  
    - 🖐️ **கிளிப்புகளைப் பயன்படுத்துதல்:** விரல் வலிமையை அதிகரிக்கும்  
    - 🧃 **ஸ்பொன்ஜ் சுருட்டுதல்:** கை வலிமை மற்றும் கட்டுப்பாட்டை அதிகரிக்கும்  
    - 🪁 **காகித விமானம் செய்யுதல்:** படைப்பாற்றல் மற்றும் திட்டமிடும் திறனை மேம்படுத்தும்  
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **விளையாட்டு போல பயிற்சி** – அழுத்தம் இல்லாமல் மகிழ்ச்சியாகச் செய்யுங்கள்  
    ✅ **குழந்தையின் விருப்பத்தை பின்பற்றுங்கள்** – அவருக்கு பிடித்த பொருட்களைப் பயன்படுத்துங்கள்  
    ✅ **சிறிய படிகளாக தொடங்குங்கள்** – வெற்றியளிக்கும் செயலில் தொடங்குங்கள்  
    ✅ **தேர்வுகளை கொடுங்கள்** – இரண்டு செயல்களில் ஒன்றைத் தேர்ந்தெடுக்கச் சொல்லுங்கள்  
    ✅ **முதலில் நீங்கள் செய்து காட்டுங்கள்** – அதன் பிறகு குழந்தை பின்பற்றட்டும்  
    ✅ **மிகைப்படுத்தாமல் பொறுமை காட்டுங்கள்**  
    ✅ **தினசரி வாழ்க்கைச் செயல்களில் ஈடுபடுத்துங்கள்** – சமையல், மேசை போடுதல் போன்றவை  
    ✅ **சிறிய முன்னேற்றங்களையும் கொண்டாடுங்கள்**  
    ✅ **நல்ல வார்த்தைகளால் ஊக்கப்படுத்துங்கள்** – பாராட்டு, கைத்தட்டல், ஸ்டிக்கர்கள்  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in tamil_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("குழந்தையின் ஒவ்வொரு சிறிய செயலும் பெரிய முன்னேற்றம். அன்பும் பொறுமையும் வெற்றிக்குக் காரணம்! 💖")
