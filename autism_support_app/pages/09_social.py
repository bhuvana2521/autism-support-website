import streamlit as st
from streamlit_extras.let_it_rain import rain

# ✅ Page animation (short duration)
rain(emoji="🤝", font_size=30, falling_speed=5, animation_length=3)

# ✅ Protect page (requires login)
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please log in to access this page.")
    st.stop()

# ✅ Page configuration
st.set_page_config(page_title="Social Skills Training", layout="centered")

# ✅ Language selector
language = st.radio("🌐 Choose Language", ["English", "தமிழ்"], index=0)
st.session_state["language"] = language
username = st.session_state.get("logged_user", "User")

# ✅ Page title and rain
st.title("🤝 Social Skills Training")
rain(emoji="💬", font_size=24, falling_speed=5, animation_length=3)

# ✅ Video links
video_links = [
    "https://youtu.be/IcUR8NxLdG4?si=j77OYZtMjkdp10_Z",
    "https://youtu.be/cqoEwdRDd5I?si=vcMOmL1y8WeObSUd",
    "https://youtu.be/DEqhWMugltk?si=P72sN57Ls6tLXLwc",
    "https://youtu.be/1n3Vm-jUzrU?si=y66aFolrLJSbpQQj",
    "https://youtu.be/ruQL1QwGCoc?si=Zw7BU90xnVEIXKHt"
]

# ✅ English content
if language == "English":
    st.subheader(f"Welcome {username}! Let's Boost Social Skills Together 💬")
    st.markdown("#### 💡 *“Every small conversation builds confidence.”*")

    st.markdown("### 🌱 What is Social Skills Training?")
    st.markdown("""
    **Social Skills Training** helps children communicate, share, and interact effectively with others.  
    It teaches **conversation skills, emotional understanding, and teamwork** through fun and engaging activities.
    """)

    st.markdown("### 🌟 Key Benefits:")
    st.markdown("""
    - Improves **eye contact and greetings**
    - Builds **confidence in group settings**
    - Develops **empathy and understanding of feelings**
    - Encourages **turn-taking and sharing**
    - Helps **reduce social anxiety**
    """)

    st.markdown("### 🧩 Fun Social Activities at Home:")
    st.markdown("""
    - 🗨️ **Role Play Conversations:** Practice greeting, asking names, saying thank you  
    - 🎭 **Emotion Charades:** Act out feelings and guess them  
    - 🧸 **Sharing Game:** Take turns with favorite toys  
    - 📚 **Story Time:** Read a story and talk about how characters feel  
    - 🎲 **Board Games:** Practice waiting for turns and following rules  
    - 🖼️ **Picture Talk:** Show pictures and ask “What do you see? How do they feel?”  
    - 🛍️ **Pretend Shopping:** Practice saying “Hello”, “Please”, “Thank you”  
    - 🎤 **Sing-Along Songs:** Group singing for confidence  
    - 🧠 **Question Game:** “What’s your favorite food?” “What makes you happy?”  
    - 🧎 **Playdates:** Invite one child for short, structured play  
    - 🎬 **Watch & Discuss Cartoons:** Ask “Why did the character do that?”  
    - 🪞 **Mirror Play:** Practice facial expressions and gestures  
    """)

    st.markdown("### ❤️ Parent Tips for Social Development:")
    st.markdown("""
    ✅ **Model Social Behavior:** Greet others, say “thank you” in front of your child  
    ✅ **Give Positive Feedback:** Praise when they share or make eye contact  
    ✅ **Break Down Steps:** Teach one skill at a time (like greeting first)  
    ✅ **Use Visual Aids:** Social stories and picture cards work well  
    ✅ **Practice Daily:** Use every opportunity (shopping, playground, home)  
    ✅ **Create Calm Social Situations:** Avoid overwhelming group size initially  
    ✅ **Celebrate Effort:** Even a smile or wave is progress  
    ✅ **Use Favorite Interests:** If child loves cars, use that in social play  
    """)

    st.markdown("### 📺 Watch These Helpful Videos:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 A Note to Parents:")
    st.info("Every conversation your child attempts is a victory. Be patient, gentle, and keep encouraging. 💖")

# ✅ Tamil content
else:
    st.subheader(f"வரவேற்கிறோம் {username}! சமூகத் திறன்களை மேம்படுத்துவோம் 💬")
    st.markdown("#### 💡 *“ஒவ்வொரு உரையாடலும் நம்பிக்கையை உருவாக்கும்.”*")

    st.markdown("### 🌱 Social Skills Training என்றால் என்ன?")
    st.markdown("""
    **Social Skills Training** என்பது குழந்தைகள் **உரையாடல், பகிர்வு, மற்றும் தொடர்பு** திறன்களை கற்றுக்கொள்ள உதவுகிறது.  
    இது **உணர்வுகளை புரிதல், நட்பு வளர்ப்பு, மற்றும் குழு விளையாட்டுகளை** ஊக்குவிக்கிறது.
    """)

    st.markdown("### 🌟 நன்மைகள்:")
    st.markdown("""
    - **கண் பார்வை மற்றும் வணக்கம் மேம்படும்**
    - **குழு சூழலில் நம்பிக்கை அதிகரிக்கும்**
    - **மற்றவரின் உணர்வுகளை புரிந்துகொள்ள உதவும்**
    - **பகிர்வு மற்றும் மாறிமாறி விளையாடுதல் பழக்கம்**
    - **சமூக அச்சம் குறையும்**
    """)

    st.markdown("### 🧩 வீட்டில் செய்யக்கூடிய சமூக விளையாட்டுகள்:")
    st.markdown("""
    - 🗨️ **நடிப்பு உரையாடல்:** வணக்கம் சொல்லும் பழக்கம்  
    - 🎭 **உணர்ச்சி விளையாட்டு:** முகபாவனை காட்டி யூகிக்க  
    - 🧸 **பகிர்வு விளையாட்டு:** பொம்மைகளை மாறிமாறி பயன்படுத்த  
    - 📚 **கதை நேரம்:** கதாபாத்திரங்களின் உணர்வுகளை விவாதிக்க  
    - 🎲 **போர்டு விளையாட்டு:** விதிகளை பின்பற்ற கற்றுக்கொள்ள  
    - 🖼️ **படம் காட்டி கேள்வி:** “என்ன பார்கிறாய்? அவன் எப்படி உணர்கிறான்?”  
    - 🛍️ **கடை விளையாட்டு:** வணக்கம், நன்றி சொல்லும் பழக்கம்  
    - 🎤 **பாடல் பாடுதல்:** குழுவில் பாடுவதால் நம்பிக்கை அதிகரிக்கும்  
    - 🧠 **கேள்வி விளையாட்டு:** “உனக்கு பிடித்த உணவு என்ன?”  
    - 🧎 **சிறிய விளையாட்டு கூட்டம்:** ஒரு நண்பருடன் சிறிய விளையாட்டு  
    - 🎬 **கார்ட்டூன் பார்த்து பேசுதல்:** கதாபாத்திரம் ஏன் அவ்வாறு செய்தான்?  
    - 🪞 **மிரர் விளையாட்டு:** முகபாவனைகளைப் பயிற்சி செய்ய  
    """)

    st.markdown("### ❤️ பெற்றோருக்கான குறிப்புகள்:")
    st.markdown("""
    ✅ **மாதிரி காட்டுங்கள்:** நீங்கள் வணக்கம் சொல்லுங்கள், நன்றி சொல்லுங்கள்  
    ✅ **பாராட்டுங்கள்:** குழந்தை பகிர்ந்தால் உடனே பாராட்டு  
    ✅ **சிறிய படிகளாக கற்றுக்கொள்ளுங்கள்:** முதலில் வணக்கம், பிறகு உரையாடல்  
    ✅ **பட உதவிகள் பயன்படுத்துங்கள்:** சமூகக் கதைகள், பட அட்டைகள்  
    ✅ **தினசரி பயிற்சி:** கடை, விளையாட்டு பூங்கா போன்ற இடங்களில்  
    ✅ **அமைதியான சூழல் உருவாக்குங்கள்:** அதிகமான கூட்டம் தவிர்க்க  
    ✅ **சிறிய முன்னேற்றங்களையும் கொண்டாடுங்கள்**  
    ✅ **விருப்பமான விஷயங்களை சேர்க்குங்கள்:** கார் பிடித்தால் அதில் விளையாட்டு  
    """)

    st.markdown("### 📺 பயனுள்ள வீடியோக்கள்:")
    for link in video_links:
        st.video(link)

    st.markdown("### 🌈 பெற்றோருக்கான ஊக்கம்:")
    st.info("ஒவ்வொரு சிறிய உரையாடலும் பெரிய முன்னேற்றம். பொறுமையாகவும் அன்பாகவும் ஊக்குவியுங்கள். 💖")
