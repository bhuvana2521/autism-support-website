import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Short rain animation
rain(emoji="🗨️", font_size=30, falling_speed=5, animation_length=3)

# ✅ Login check
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page config
st.set_page_config(page_title="AAC & Communication Tools", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title
st.title("🗨️ AAC & Communication Tools")
rain(emoji="💬", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/eCB5jQeRxR8?si=j74EmrrKkraDaJPO",
    "https://youtu.be/1zhQ9vHo1gc?si=n8QYytOuGHTeWcfS",
    "https://youtu.be/oLRDXPCbMKg?si=CgZpbOD9txIJ4cPE",
    "https://youtu.be/qpLm7OlSOQg?si=rga6T6dbGWagu-ly",
    "https://youtu.be/iV3Ltn2PvGU?si=WGgcIQeexlZwRxVp"
]

# ✅ English content
if language == "English":
    st.subheader(f"Welcome {username}! Let’s Explore AAC & Communication Tools 💬")
    st.markdown("#### 💡 *“Communication is connection, no matter the method.”*")

    st.markdown("### 🌱 What is AAC?")
    st.markdown("""
    **AAC (Augmentative and Alternative Communication)** tools help children communicate when speech is difficult.  
    These include **picture boards, communication apps, sign language, and speech devices**.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Gives a voice to children with speech challenges  
    - Reduces frustration and behavior issues  
    - Improves **social interaction and confidence**  
    - Encourages **language development**  
    - Can be **used at home, school, and therapy sessions**  
    """)

    st.markdown("### 🧩 Fun AAC Activities at Home:")
    st.markdown("""
    - 📷 **Picture Choice Game:** Ask child to point at picture for “I want water”  
    - 🧃 **Snack Request Game:** Use AAC board to request food or drink  
    - 🛒 **Shopping List AAC:** Use pictures to pick items in store  
    - 🏠 **Daily Routine AAC:** Show pictures for “bath”, “play”, “eat”  
    - 🎵 **Music Choice:** Let child pick songs using AAC app  
    - 📚 **Storytelling with AAC:** Ask child to choose “happy” or “sad” picture for story ending  
    - 🖼️ **Emotion Cards:** Show how they feel – happy, sad, tired  
    - 🎲 **Game Commands:** “Roll dice”, “My turn”, “Your turn” using AAC  
    - 🎨 **Art Time:** Use AAC to choose color or object  
    """)

    st.markdown("### ❤️ Parent Tips for AAC Success:")
    st.markdown("""
    ✅ **Always Keep AAC Available:** Don’t remove AAC device or board  
    ✅ **Model AAC Use:** Use the board/app when speaking to child  
    ✅ **Start Simple:** Teach “yes”, “no”, “more”, “help” first  
    ✅ **Respond Immediately:** When child uses AAC, respond with excitement  
    ✅ **Practice in Real Life:** Meals, playtime, shopping – use AAC everywhere  
    ✅ **Avoid Pressure:** Let child explore AAC freely  
    ✅ **Celebrate Every Attempt:** Even pointing to one picture is progress  
    ✅ **Combine Speech & AAC:** Say the word as you show the picture  
    ✅ **Personalize AAC:** Add favorite items like toys, snacks, family photos  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("AAC is not replacing speech – it’s a bridge to communication and independence. Your support matters. 💖")

# ✅ Tamil content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! AAC & தொடர்பு கருவிகளைப் பற்றி அறிந்துகொள்வோம் 💬")
    st.markdown("#### 💡 *“தொடர்பு என்பது எந்த முறையிலானாலும் ஒரு இணைப்பு.”*")

    st.markdown("### 🌱 AAC என்றால் என்ன?")
    st.markdown("""
    **AAC (Augmentative and Alternative Communication)** என்பது குழந்தைகள் பேச முடியாதபோது **பட அட்டைகள், கையெழுத்து மொழி, ஆப்ஸ், சாதனங்கள்** மூலம் தொடர்பு கொள்ள உதவும்.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - குழந்தைக்கு பேசுவதற்கான வாய்ப்பு கிடைக்கும்  
    - விரக்தி மற்றும் கோபம் குறையும்  
    - சமூக உறவு மற்றும் நம்பிக்கை அதிகரிக்கும்  
    - மொழி வளர்ச்சிக்கு உதவும்  
    - வீடு, பள்ளி, சிகிச்சை – எங்கும் பயன்படுத்தலாம்  
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய AAC விளையாட்டுகள்:")
    st.markdown("""
    - 📷 **பட தேர்வு:** “எனக்கு தண்ணீர் வேண்டும்” என்று காட்டச் சொல்லுங்கள்  
    - 🧃 **சிற்றுண்டி கோரிக்கை:** AAC மூலம் உணவை கேட்க சொல்லுங்கள்  
    - 🛒 **ஷாப்பிங் விளையாட்டு:** படங்களை காட்டி பொருட்களை தேர்வு செய்ய  
    - 🏠 **நாள் நடைமுறை:** “குளியல்”, “விளையாட்டு”, “சாப்பாடு” பட அட்டைகள் காட்டுங்கள்  
    - 🎵 **இசை தேர்வு:** AAC மூலம் பாடலை தேர்வு செய்ய  
    - 📚 **கதை விளையாட்டு:** “மகிழ்ச்சி”, “துக்கம்” படத்தை தேர்வு செய்ய சொல்லுங்கள்  
    - 🖼️ **உணர்ச்சி அட்டைகள்:** “மகிழ்ச்சி”, “சோர்வு”, “கோபம்” ஆகியவற்றை காட்டச் சொல்லுங்கள்  
    - 🎲 **விளையாட்டு உத்தரவு:** “என் டர்ன்”, “உங்கள் டர்ன்” AAC மூலம் சொல்லுங்கள்  
    - 🎨 **கலை நேரம்:** விருப்பமான நிறங்களை AAC மூலம் தேர்வு செய்ய  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **AAC எப்போதும் அருகில் இருக்க வேண்டும்**  
    ✅ **நீங்களே மாதிரி காட்டுங்கள்**  
    ✅ **எளிய வார்த்தைகளில் தொடங்குங்கள்** (ஆம், இல்லை, மேலும்)  
    ✅ **குழந்தை AAC பயன்படுத்தினால் உடனே பாராட்டு**  
    ✅ **வாழ்க்கைச் சூழலில் பயிற்சி கொடுங்கள்**  
    ✅ **அழுத்தம் விட வேண்டாம்**  
    ✅ **ஒவ்வொரு முயற்சியையும் கொண்டாடுங்கள்**  
    ✅ **வாய்மொழியுடன் AAC இணைக்குங்கள்**  
    ✅ **குழந்தையின் விருப்பங்களைச் சேர்க்குங்கள்** (பொம்மை, சாப்பாடு)  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("AAC என்பது பேசுவதற்கு பதிலாக அல்ல – அது தொடர்பு மற்றும் சுதந்திரத்திற்கான பாலம். உங்கள் ஆதரவு முக்கியம். 💖")
