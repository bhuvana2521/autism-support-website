import streamlit as st 
import json
import os
import time

# Initialize users in session state if not exists
if "users" not in st.session_state:
    st.session_state["users"] =  {}


# ----------------------------
# 🔧 Configuration
# ----------------------------
st.set_page_config(page_title="Autism Support App", layout="wide")
USER_DATA_FILE = "users.json"


# ----------------------------
# 📦 Helpers
# ----------------------------
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# ----------------------------
# 🧠 Session State Init
# ----------------------------
if "users" not in st.session_state:
    st.session_state.users = load_users()

if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_user" not in st.session_state:
    st.session_state.logged_user = None

if "language" not in st.session_state:
    st.session_state.language = "English"

# ----------------------------
# 🔐 Login Page
# ----------------------------
def login_page():
    # Custom CSS for bigger, stylish font
    st.markdown("""
        <style>
        /* Remove extra top padding from Streamlit */
        .block-container {
            padding-top: 1rem;
        }

        /* Title */
        .title-text {
            font-size: 42px !important;
            font-weight: bold !important;
            color: #1B4F72;
            text-align: center;
            margin-bottom: 25px;
        }

        /* Bigger labels */
        div[data-testid="stTextInput"] label,
        div[data-testid="stPasswordInput"] label,
        div[data-testid="stRadio"] label {
            font-size: 20px !important;
            font-weight: 600 !important;
        }

        /* Bigger input text */
        .stTextInput input, .stPasswordInput input {
            font-size: 18px !important;
            height: 45px !important;
        }

        /* Bigger radio options */
        div[data-testid="stRadio"] div[role="radiogroup"] label {
            font-size: 18px !important;
        }

        /* Buttons */
        .stButton>button {
            font-size: 20px !important;
            padding: 12px 24px !important;
            border-radius: 12px !important;
            background-color: #50C878 !important;
            color: white !important;
            font-weight: bold !important;
        }
        .stButton>button:hover {
            background-color: #3CB371 !important;
        }

        /* Form box */
        .form-box {
            background-color: #F0F4F8;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 6px 12px rgba(0,0,0,0.15);
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown(
    "<h1 style='text-align: center; font-size: 40px;'>Autism Support App</h1>",
    unsafe_allow_html=True
)


    

    login_input = st.text_input("Username or Email | பயனர்பெயர் அல்லது மின்னஞ்சல்").strip()
    password = st.text_input("Password | கடவுச்சொல்", type='password')
    selected_language = st.radio("Select Language | மொழியைத் தேர்வுசெய்க", ["English", "Tamil"])

    if st.button("Login"):
        users = st.session_state.users
        for username, details in users.items():
            if login_input == username or login_input == details.get("email"):
                if details["password"] == password:

                    st.session_state["logged_user"] = username
                    st.session_state["language"] = selected_language
                    st.session_state["logged_in"] = True
                    st.session_state.page = "welcome"
                    st.success(f"✅ Welcome, {username}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid password")
            else:
                st.error("❌ Invalid username/email")

    st.markdown("---")

    if st.button("New user? Register here | புதிய பயனர் பதிவு செய்யவுமா?"):
        st.session_state.page = "register"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------
# 📝 Registration Page
# ----------------------------
def register_page():
    # ✅ Emerald Green Button Styling
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #50C878; /* Emerald Green */
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #3CB371; /* Darker green on hover */
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📝 Register | பதிவு")

    language = st.radio("Select Language | மொழியைத் தேர்வுசெய்க", ["English", "Tamil"])

    if language == "English":
        st.subheader("Welcome to the Autism Support App!")
    else:
        st.subheader("ஆட்டிசம் ஆதரவு பயன்பாட்டிற்கு வரவேற்கிறோம்!")

    username = st.text_input("Username | பயனர்பெயர்", key='reg_username')
    password = st.text_input("Password | கடவுச்சொல்", type='password', key='reg_password')
    mobile = st.text_input("Mobile Number | கைபேசி எண்")
    email = st.text_input("Email ID")
    parent_type = st.selectbox("I am a | நான்", ["Mother", "Father"])
    child_age = st.number_input("Child's Age | குழந்தையின் வயது", min_value=1, max_value=20)
    condition = st.selectbox("Condition | நிலை", ["Autism", "Hyperactive", "Speech Delay"])
    therapy = st.selectbox("Therapy Type", [
        "Applied Behavior Analysis (ABA)",
        "Early Start Denver Model (ESDM)",
        "DIR/Floortime",
        "TEACCH (Structured Teaching)",
        "Speech and Language Therapy",
        "Occupational Therapy (OT)",
        "Physical Therapy (PT)",
        "Sensory Integration Therapy",
        "Social Skills Training",
        "AAC & Communication Tools",
        "Parent-Mediated Therapy",
        "Play Therapy",
        "Music Therapy",
        "Art Therapy"
    ])

    st.text_area("💖 Motivation:",
        "You're doing great! Every step matters for your child’s bright future." 
        if language == "English" else 
        "நீங்கள் சிறப்பாக செய்கிறீர்கள்! உங்கள் குழந்தையின் சிறப்பான எதிர்காலத்திற்கு ஒவ்வொரு அடியும் முக்கியம்.")

    if st.button("Submit | சமர்ப்பிக்கவும்"):
        users = st.session_state.users
        if username in users:
            st.warning("⚠️ Username already exists")
        else:
            users[username] = {
                'password': password,
                'mobile': mobile,
                'email': email,
                'parent_type': parent_type,
                'child_age': child_age,
                'condition': condition,
                'therapy': therapy,
                'language': language
            }
            save_users(users)
            st.success("🎉 Successfully Registered!")
            time.sleep(1.5)
            st.session_state.page = "login"
            st.rerun()


    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()


# ----------------------------
# 👋 Welcome Page with new sections
# ----------------------------
def welcome_page():
    username = st.session_state.get("logged_user", "User")

    # 🔘 Language selector
    language = st.radio("🌐 Select Language | மொழியைத் தேர்வுசெய்க", ["English", "Tamil"], key="dynamic_lang")
    st.session_state["language"] = language  # Update session

    # 🌟 Welcome Message
    if language == "English":
        st.title(f"🌟 Welcome, {username}!")
        st.markdown("""
        💬 *You’re doing an amazing job supporting your child. Every step counts!*  
        🌸 **"Small progress is still progress."**  
        💖 **"Your care makes all the difference."**
        """)
    else:
        st.title(f"🌟 வரவேற்கிறோம், {username}!")
        st.markdown("""
        💬 *உங்கள் குழந்தையை ஆதரிப்பதில் நீங்கள் சிறப்பாக செய்கிறீர்கள். ஒவ்வொரு படியும் முக்கியமானது!*  
        🌸 **"சிறிய முன்னேற்றமும் முன்னேற்றமே."**  
        💖 **"உங்கள் பராமரிப்பு எல்லாவற்றிலும் வித்தியாசத்தை ஏற்படுத்துகிறது."**
        """)

    st.markdown("---")

    # ✅ Basic Parental Advice
    st.header("💡 Basic Parental Tips" if language == "English" else "💡 பெற்றோர் ஆலோசனைகள்")
    st.write("""
    1. Maintain a **routine** for your child.
    2. Use **visual supports** like charts and pictures.
    3. Give **positive reinforcement** for good behavior.
    4. Stay calm during meltdowns.
    5. Take care of **yourself** too.
    """ if language == "English" else """
    1. உங்கள் குழந்தைக்கான **ஒரே நேரம் திட்டத்தை** பின்பற்றுங்கள்.
    2. **படங்கள் மற்றும் அட்டவணைகளை** பயன்படுத்துங்கள்.
    3. நல்ல நடத்தைக்கு **நல்ல பாராட்டு** அளிக்கவும்.
    4. கோபமான நேரங்களில் அமைதியாக இருங்கள்.
    5. உங்களையும் **பாதுகாத்துக்கொள்ளுங்கள்**.
    """)

    st.markdown("---")

    # ✅ Avoid Foods Section
    st.header("🚫 Foods to Avoid" if language == "English" else "🚫 தவிர்க்க வேண்டிய உணவுகள்")
    st.write("""
    - Processed foods (chips, snacks)
    - Sugary foods
    - Artificial colors & preservatives
    - High caffeine drinks
    - Sometimes gluten & casein (check with doctor)
    """ if language == "English" else """
    - பதப்படுத்தப்பட்ட உணவுகள் (சிப்ஸ், ஸ்நாக்ஸ்)
    - அதிக சர்க்கரை உள்ள உணவுகள்
    - செயற்கை நிறங்கள் மற்றும் பாதுகாப்புச் சத்துகள்
    - அதிக காஃபீன் உள்ள பானங்கள்
    - சில நேரங்களில் குளூட்டன் மற்றும் கேசீன் (மருத்துவரை கேளுங்கள்)
    """)

    st.info("💡 Always consult your doctor before making diet changes." if language == "English" else "💡 உணவு மாற்றங்களுக்கு முன் எப்போதும் மருத்துவரை அணுகவும்.")

    st.markdown("---")

    # ✅ Dynamic Video Section
    if language == "English":
        st.subheader("🎥 Helpful Autism Videos")
        video_links = [
            "https://youtu.be/p6Xd4cg40no",
            "https://youtu.be/DZXjJVrm1Jw",
            "https://youtu.be/JYPeOm5A8XQ",
            "https://youtu.be/MTW7H5UQ8Ts",
            "https://youtu.be/FCejya1WWC8",
            "https://youtu.be/0Pp8jcQ97pY"
        ]
    else:
        st.subheader("🎥 ஆட்டிசம் விழிப்புணர்வு வீடியோக்கள்")
        video_links = [
            "https://youtu.be/8d966Audhe0",
            "https://youtu.be/KS2VpfLPQQM",
            "https://youtu.be/UjN7OIdAU4s",
            "https://youtu.be/Ve0JOzpKc44",
            "https://youtu.be/ys10hN1yQws",
            "https://youtu.be/6aD47nMAjlA"
        ]

    # Show videos in 2 rows (3 per row)
    cols = st.columns(3)
    for idx, link in enumerate(video_links):
        with cols[idx % 3]:
            st.video(link)

    st.markdown("---")

    # ✅ Therapy Navigation
    st.subheader("📚 Select a Therapy to Learn More" if language == "English" else "📚 தெரபியைத் தேர்ந்தெடுக்கவும்")

    therapies = [
        ("Applied Behavior Analysis (ABA)", "01_aba"),
        ("Early Start Denver Model (ESDM)", "02_esdm"),
        ("DIR/Floortime", "03_dir"),
        ("TEACCH (Structured Teaching)", "04_teacch"),
        ("Speech and Language Therapy", "05_speech"),
        ("Occupational Therapy (OT)", "06_ot"),
        ("Physical Therapy (PT)", "07_pt"),
        ("Sensory Integration Therapy", "08_sensory"),
        ("Social Skills Training", "09_social"),
        ("AAC & Communication Tools", "10_aac"),
        ("Parent-Mediated Therapy", "11_parent"),
        ("Play Therapy", "12_play"),
        ("Music Therapy", "13_music"),
        ("Art Therapy", "14_art"),
    ]

    cols = st.columns(3)
    for idx, (label, file) in enumerate(therapies):
        with cols[idx % 3]:
            if st.button(label, key=f"therapy_{file}"):
                st.switch_page(f"pages/{file}.py")

# ----------------------------
# 🚀 Main App
# ----------------------------
def main():
    # Sidebar greeting if logged in
    if st.session_state.logged_user:
        st.sidebar.markdown(f"### 👋 Welcome, {st.session_state.logged_user}!")
        if st.sidebar.button("Logout"):
            st.session_state.logged_user = None
            st.session_state.page = "login"
            st.experimental_rerun()

    # Page navigation
    if st.session_state.page == "login":
        login_page()

    elif st.session_state.page == "register":
        register_page()

    elif st.session_state.page == "welcome":
        if st.session_state.logged_user:
            welcome_page()
        else:
            st.session_state.page = "login"
            st.experimental_rerun()


# -------------------------
# Entry Point
if __name__ == "__main__":
    main()



