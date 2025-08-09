import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Short rain animation (limited)
rain(emoji="🎵", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page configuration
st.set_page_config(page_title="Music Therapy", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title
st.title("🎵 Music Therapy")
rain(emoji="🎶", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/PHBEzLf-qrw?si=YS4vi6_YhmpUieFI",
    "https://youtu.be/PvyK3euKV2U?si=FFhPsORiZd-F_EB-",
    "https://youtu.be/rDClsLM_NDY?si=_ER5rQUlghrW33Ew",
    "https://youtu.be/PgFfercKfsA?si=Riphp_cGlYOSYbvL",
    "https://youtu.be/Fps2bqFV5nM?si=p2OhrWidQW-CirkZ",
    "https://youtu.be/8ByBu3qFBgc?si=Qg6zOu7b0inKqmXX"
]

# ✅ English Content
if language == "English":
    st.subheader(f"Welcome {username}! Let’s Explore Music Therapy 🎶")
    st.markdown("#### 💡 *“Where words fail, music speaks.” – Hans Christian Andersen*")

    st.markdown("### 🌱 What is Music Therapy?")
    st.markdown("""
    Music Therapy uses sound, rhythm, and melody to improve communication, emotional regulation, and social interaction in children.  
    It’s **fun, relaxing, and powerful for speech and sensory development**.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **speech and language skills**  
    - Helps in **emotional regulation**  
    - Boosts **social interaction and confidence**  
    - Reduces anxiety and stress  
    - Encourages **creativity and self-expression**  
    """)

    st.markdown("### 🎶 Fun Music Therapy Activities:")
    st.markdown("""
    - 🥁 **Rhythm Game:** Clap hands or tap on table in patterns  
    - 🎤 **Sing Along:** Simple nursery rhymes or favorite songs  
    - 🧸 **Music with Toys:** Use rattles or bells during play  
    - 🎸 **Instrument Exploration:** Drums, xylophone, or keyboard  
    - 🎧 **Listening Time:** Play calming music before bedtime  
    - 🎼 **Name Song Game:** Sing child’s name in a tune  
    - 🕺 **Dance & Freeze:** Dance when music plays, freeze when it stops  
    - 🌍 **Sound Hunt:** Identify sounds from surroundings  
    - 🎵 **DIY Instruments:** Make shakers from rice-filled bottles  
    - 🎶 **Echo Singing:** Parent sings a line, child repeats  
    """)

    st.markdown("### ❤️ Parent Tips:")
    st.markdown("""
    ✅ Play music daily for **at least 10 minutes**  
    ✅ Use **simple repetitive songs** for language building  
    ✅ Combine **movement with music** for better engagement  
    ✅ Encourage child to **create their own sounds**  
    ✅ Never force singing—focus on enjoyment  
    ✅ Use **soft background music** during stressful times  
    ✅ Join in! Your voice is the best instrument  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Music is a universal language of love. Every song you sing with your child builds confidence and happiness. 🎵")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! Music Therapy பற்றி அறிந்துகொள்வோம் 🎶")
    st.markdown("#### 💡 *“சொற்கள் தோல்வியடைந்த இடத்தில் இசை பேசும்.”*")

    st.markdown("### 🌱 Music Therapy என்றால் என்ன?")
    st.markdown("""
    இசை, தாளம், மற்றும் ராகத்தைப் பயன்படுத்தி **மொழித் திறன், உணர்ச்சி கட்டுப்பாடு, மற்றும் சமூக பழக்கங்களை மேம்படுத்தும் சிகிச்சை** இது.  
    இது **மகிழ்ச்சியானதும், அமைதியானதும், குழந்தையின் பேச்சு மற்றும் உணர்ச்சி வளர்ச்சிக்கு உதவும்**.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - பேச்சு மற்றும் மொழித் திறன் மேம்படும்  
    - உணர்ச்சி கட்டுப்பாடு வலுப்படும்  
    - சமூக தொடர்பு அதிகரிக்கும்  
    - மன அழுத்தம் குறையும்  
    - படைப்பாற்றல் மற்றும் தன்னம்பிக்கை வளரும்  
    """)

    st.markdown("### 🎶 செய்யக்கூடிய செயல்கள்:")
    st.markdown("""
    - 🥁 **தாள விளையாட்டு:** கைகள் தட்டுதல் அல்லது மேசையைத் தட்டுதல்  
    - 🎤 **பாடல்கள் பாடுதல்:** குழந்தையின் விருப்பமான பாடல்கள்  
    - 🧸 **விளையாட்டு பொம்மைகளுடன் இசை:** ராட்டில், மணி போன்றவை  
    - 🎸 **சாதன ஆராய்ச்சி:** டிரம்ஸ், கீபோர்ட், ஜைலோபோன்  
    - 🎧 **அமைதியான இசை:** படுக்கும் முன் மென்மையான இசை  
    - 🎼 **பெயர் பாடல்:** குழந்தையின் பெயரை ஒரு ராகத்தில் பாடுங்கள்  
    - 🕺 **நடனம் & நிறுத்தம்:** இசை நிறுத்தும் போது குழந்தை நிற்க வேண்டும்  
    - 🌍 **ஒலி தேடல்:** வீட்டில் உள்ள ஒலிகளை அடையாளம் காணுங்கள்  
    - 🎵 **சுயமாக இசை உருவாக்குதல்:** பாட்டிலில் அரிசி வைத்து சத்தம் செய்யுங்கள்  
    - 🎶 **பாடல் எதிரொலி:** பெற்றோர் பாடும் வரியை குழந்தை மீண்டும் பாடுதல்  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ தினமும் **10 நிமிடம் இசை** ஒலிக்கவும்  
    ✅ எளிய மற்றும் மீண்டும் மீண்டும் வரும் பாடல்களைப் பயன்படுத்துங்கள்  
    ✅ **இசையுடன் உடல் அசைவுகளை** சேர்க்கவும்  
    ✅ குழந்தையைத் தன் சத்தங்களை உருவாக்க ஊக்குவிக்கவும்  
    ✅ கட்டாயப்படுத்த வேண்டாம் – மகிழ்ச்சியை முன்னிலைப்படுத்துங்கள்  
    ✅ மன அழுத்தம் குறைக்க மென்மையான இசை போடுங்கள்  
    ✅ நீங்கள் பாடுங்கள்! உங்கள் குரல் மிகச் சிறந்த இசைக்கருவி  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("இசை என்பது அன்பின் மொழி. நீங்கள் பாடும் ஒவ்வொரு பாடலும் உங்கள் குழந்தைக்கு தன்னம்பிக்கையையும் மகிழ்ச்சியையும் தரும். 🎵")
