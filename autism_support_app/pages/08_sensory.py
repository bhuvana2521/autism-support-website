import streamlit as st
from streamlit_extras.let_it_rain import rain

# Short rain effect
rain(emoji="🌈", font_size=30, falling_speed=5, animation_length=3)

# ✅ Protect Page
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# Page Config
st.set_page_config(page_title="Sensory Integration Therapy", layout="centered")

# ✅ Language Selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# Page Title
st.title("🌈 Sensory Integration Therapy")
rain(emoji="✨", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video Links
video_links = [
    "https://youtu.be/T9j6rQ4rtQY?si=tIJ6k61ZDRlDfxMr",
    "https://youtu.be/YUdsgQGHSR8?si=3pA887xgXuEmSbma",
    "https://youtu.be/kZuu0kInwp8?si=WOmZaTeINJdkwjKV",
    "https://youtu.be/p3QDy_JsvVg?si=yZwpej__gsjalrZl"
]

# ✅ Content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Explore Sensory Integration Therapy 💬")

    st.markdown("#### 💡 *“Calm mind and happy senses create joyful learning.”*")

    st.markdown("### 🌱 What is Sensory Integration Therapy?")
    st.markdown("""
    **Sensory Integration Therapy** helps children process sensory information like **touch, sound, movement, and balance**.  
    It supports children with **sensory processing difficulties**, reducing anxiety and improving focus through structured play.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **body awareness and coordination**
    - Reduces **sensory overload and meltdowns**
    - Helps with **attention and calmness**
    - Encourages **exploration and confidence**
    - Promotes **emotional regulation**
    """)

    st.markdown("### 🧩 Fun Sensory Activities at Home:")
    st.markdown("""
    ✅ **Tactile Activities:**  
    - Play with sand, rice, or beans in a sensory bin  
    - Finger painting with bright colors  
    - Playing with slime or playdough  
    - Texture hunt (find soft, rough, smooth objects)  

    ✅ **Vestibular (Movement) Activities:**  
    - Swinging in a hammock or playground swing  
    - Rolling on a yoga ball  
    - Spinning on a chair (short, safe turns)  
    - Jumping on a trampoline  

    ✅ **Proprioceptive (Body Pressure) Activities:**  
    - Carrying small weighted bags  
    - Crawling under a blanket fort  
    - Push wall or pillow fights for resistance  
    - Animal walks (bear walk, crab walk, frog jumps)  

    ✅ **Auditory Activities:**  
    - Listening to calming music  
    - Playing soft instruments (xylophone, tambourine)  
    - Nature sounds game – “Guess the sound”  

    ✅ **Visual Activities:**  
    - Watching colorful bubbles rise  
    - Sorting toys by color and size  
    - Light box play with translucent toys  

    ✅ **Oral Sensory:**  
    - Chewing crunchy snacks  
    - Drinking thick shakes with a straw  
    - Blowing bubbles for oral motor control  
    """)

    st.markdown("### ❤️ Parent Tips for Sensory Integration:")
    st.markdown("""
    ✅ **Observe your child’s preferences** – Do they seek or avoid certain sensations?  
    ✅ **Create a calm corner** – A safe space with soft lights and favorite toys  
    ✅ **Start slow** – Introduce one sensory activity at a time  
    ✅ **Follow the child’s lead** – Never force an activity they dislike  
    ✅ **Consistency is key** – Short daily sessions work best  
    ✅ **Use sensory breaks** – Before stressful activities like homework  
    ✅ **Balance stimulation** – Too much can overwhelm; too little can bore  
    ✅ **Pair with music and rhythm** – Helps regulate mood  
    ✅ **Celebrate small wins** – Even touching a new texture is progress  
    ✅ **Communicate with therapist** – Adjust activities as needed  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Every sensory experience is a step toward confidence. Be patient, loving, and keep exploring with your child! 💖")

# ✅ Tamil Content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! உணர்வு ஒருங்கிணைப்பு சிகிச்சையைப் பற்றி அறிந்துகொள்வோம் 💬")

    st.markdown("#### 💡 *“சாந்தமான உணர்வுகள் மகிழ்ச்சியான கற்றலை உருவாக்கும்.”*")

    st.markdown("### 🌱 Sensory Integration என்றால் என்ன?")
    st.markdown("""
    **Sensory Integration Therapy** என்பது **தொட்டு உணர்வு, ஒலி, இயக்கம், சமநிலை** போன்ற உணர்வுகளைச் சரியாக புரிந்துகொள்ள உதவும் சிகிச்சை.  
    இது குழந்தைகளின் **பதற்றம் குறைந்து கவனம் அதிகரிக்க** விளையாட்டின் மூலம் உதவுகிறது.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - உடல் ஒருங்கிணைப்பு மேம்பாடு  
    - உணர்வு அடக்கம் மற்றும் கோபம் குறைவு  
    - கவனமும் அமைதியும் அதிகரிக்கும்  
    - ஆர்வமும் நம்பிக்கையும் வளர்ச்சி  
    - உணர்ச்சி கட்டுப்பாடு மேம்பாடு  
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய உணர்வு விளையாட்டுகள்:")
    st.markdown("""
    ✅ **தொட்டு உணர்வு:**  
    - மணல், அரிசி, பயறு கொண்ட பாக்ஸ் விளையாட்டு  
    - விரல் ஓவியம்  
    - ஸ்லைம் அல்லது களிமண் விளையாட்டு  
    - வேறு வேறு பொருட்களின் மேல் தொட்டு உணர்தல்  

    ✅ **இயக்கம்:**  
    - ஊஞ்சல் விளையாட்டு  
    - யோகா பந்து மீது உருளுதல்  
    - மெதுவாக சுழலும் நாற்காலி  
    - டிராம்போலின் குதிப்பு  

    ✅ **உடல் அழுத்தம்:**  
    - சிறிய எடை பைகள் எடுத்துச் செல்லுதல்  
    - போர்வை அடியில் துழாவல்  
    - சுவர் தள்ளுதல்  
    - விலங்கு நடை – கரடி நடை, நண்டு நடை  

    ✅ **ஒலி:**  
    - மென்மையான இசை கேட்குதல்  
    - சிறிய இசைக்கருவிகள் வாசித்தல்  
    - இயற்கை ஒலியை அடையாளம் காண்பது  

    ✅ **காட்சி:**  
    - பப்ள்ஸ் விளையாட்டு  
    - நிறம், அளவுப்படி பொருட்களை வகைப்படுத்துதல்  
    - ஒளி பெட்டியில் விளையாடுதல்  

    ✅ **வாய்புணர்வு:**  
    - முறுக்கான ஸ்நாக்ஸ் சாப்பிடுதல்  
    - கெட்டியான ஜூஸ் ஸ்ட்ரா மூலம் குடித்தல்  
    - பப்ள்ஸ் ஊதுதல்  
    """)

    st.markdown("### ❤️ பெற்றோர்களுக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **குழந்தையின் விருப்பத்தை கவனியுங்கள்**  
    ✅ **அமைதியான மூலை அமைக்குங்கள்**  
    ✅ **மெதுவாக ஆரம்பியுங்கள்**  
    ✅ **குழந்தையின் ஆசையை பின்பற்றுங்கள்**  
    ✅ **தினசரி குறுகிய அமர்வுகள்**  
    ✅ **பிரேக் நேரங்களில் உணர்வு விளையாட்டுகள்**  
    ✅ **மிகுதியான உந்துதல் கொடுக்காதீர்கள்**  
    ✅ **இசை மற்றும் ரிதம் சேர்த்து விளையாடுங்கள்**  
    ✅ **சிறிய முன்னேற்றங்களையும் கொண்டாடுங்கள்**  
    ✅ **நிபுணருடன் ஆலோசித்து செயல் படுங்கள்**  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("ஒவ்வொரு உணர்வு அனுபவமும் நம்பிக்கைக்கு வழிகாட்டும். அன்போடு பொறுமையாக செயல்படுங்கள்! 💖")
