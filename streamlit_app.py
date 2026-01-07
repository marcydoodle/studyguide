import streamlit as st
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Triple Threat Mastery (Weeks 1-20)",
    page_icon="🎓",
    layout="wide"
)

# --- CSS FOR STYLING ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'progress' not in st.session_state:
    st.session_state.progress = {}

# --- CURRICULUM DATA (WEEKS 1-20) ---
def get_curriculum():
    return {
        # --- PHASE 1: FOUNDATIONS (Weeks 1-10) ---
        1: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Order of Operations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:intro-variables/v/order-of-operations"},
                "jp": {"topic": "Hiragana A-O", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "Intro to Networking", "link": "https://www.youtube.com/watch?v=9WkCgEyxk70"}},
            2: {"math": {"topic": "Combining Like Terms", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:combining-like-terms/v/combining-like-terms"},
                "jp": {"topic": "Hiragana KA-KO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "The OSI Model", "link": "https://www.youtube.com/watch?v=Ilk71j9kSgs"}},
            3: {"math": {"topic": "1-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/why-we-do-the-same-thing-to-both-sides-of-equation"},
                "jp": {"topic": "Hiragana SA-SO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "TCP/IP Model", "link": "https://www.freecodecamp.org/news/osi-model-networking-layers/"}},
            4: {"math": {"topic": "2-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/two-step-equations"},
                "jp": {"topic": "Hiragana TA-TO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "Binary & Hex", "link": "https://www.youtube.com/watch?v=LpuPe81bc2w"}},
            5: {"math": {"topic": "Multi-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/multi-step-equations-1"},
                "jp": {"topic": "Hiragana NA-NO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "IPv4 Addressing", "link": "https://www.youtube.com/watch?v=vcAr9OSHJYA"}},
            6: {"math": {"topic": "Stats: Mean, Median, Mode", "link": "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode"},
                "jp": {"topic": "Writing Practice", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "Classful Subnetting", "link": "https://www.youtube.com/watch?v=ecC3qvIz9fQ"}},
            7: {"math": {"topic": "Week 1 Review", "link": "https://www.khanacademy.org/math/algebra"},
                "jp": {"topic": "Anki Setup", "link": "https://apps.ankiweb.net/"},
                "cyber": {"topic": "Lab: Install VirtualBox", "link": "https://www.virtualbox.org/wiki/Downloads"}}
        }},
        2: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Slope Formula", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope/v/slope-of-a-line"},
                "jp": {"topic": "Hiragana HA-HO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "
