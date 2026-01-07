import streamlit as st
import pandas as pd
import json

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Triple Threat Mastery",
    page_icon="🎓",
    layout="wide"
)

# --- SESSION STATE INITIALIZATION ---
# This keeps track of your checked boxes
if 'progress' not in st.session_state:
    st.session_state.progress = {}

# --- CURRICULUM DATA ---
# In a real scenario, you might load this from the CSVs we generated.
# I have populated Week 1 fully to demonstrate.
def get_curriculum():
    return {
        1: {
            "phase": "Phase 1: Foundations",
            "days": {
                1: {
                    "math": {"topic": "Order of Operations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:intro-variables/v/order-of-operations"},
                    "jp": {"topic": "Hiragana A-O", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "Intro to Networking", "link": "https://www.youtube.com/watch?v=9WkCgEyxk70"}
                },
                2: {
                    "math": {"topic": "Combining Like Terms", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:combining-like-terms/v/combining-like-terms"},
                    "jp": {"topic": "Hiragana KA-KO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "The OSI Model", "link": "https://www.youtube.com/watch?v=Ilk71j9kSgs"}
                },
                3: {
                    "math": {"topic": "1-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/why-we-do-the-same-thing-to-both-sides-of-equation"},
                    "jp": {"topic": "Hiragana SA-SO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "TCP/IP Model", "link": "https://www.freecodecamp.org/news/osi-model-networking-layers/"}
                },
                4: {
                    "math": {"topic": "2-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/two-step-equations"},
                    "jp": {"topic": "Hiragana TA-TO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "Binary & Hex", "link": "https://www.youtube.com/watch?v=LpuPe81bc2w"}
                },
                5: {
                    "math": {"topic": "Multi-Step Equations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/multi-step-equations-1"},
                    "jp": {"topic": "Hiragana NA-NO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "IPv4 Addressing", "link": "https://www.youtube.com/watch?v=vcAr9OSHJYA"}
                },
                6: {
                    "math": {"topic": "Stats: Mean, Median, Mode", "link": "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode"},
                    "jp": {"topic": "Writing Practice", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                    "cyber": {"topic": "Classful Subnetting", "link": "https://www.youtube.com/watch?v=ecC3qvIz9fQ"}
                },
                7: {
                    "math": {"topic": "Week 1 Review", "link": "https://www.khanacademy.org/math/algebra"},
                    "jp": {"topic": "Anki Setup", "link": "https://apps.ankiweb.net/"},
                    "cyber": {"topic": "Lab: Install VirtualBox", "link": "https://www.virtualbox.org/wiki/Downloads"}
                },
            }
        }
    }

# --- HELPER FUNCTIONS ---
def generate_placeholder_data(start_week, end_week, phase_name):
    """Generates placeholder structure for weeks not yet hardcoded"""
    data = {}
    for w in range(start_week, end_week + 1):
        data[w] = {
            "phase": phase_name,
            "days": {
                d: {
                    "math": {"topic": f"Week {w} Math Topic", "link": "https://www.khanacademy.org/"},
                    "jp": {"topic": f"Week {w} Japanese Topic", "link": "http://www.guidetojapanese.org/"},
                    "cyber": {"topic": f"Week {w} Cyber Topic", "link": "https://www.youtube.com/"}
                } for d in range(1, 8)
            }
        }
    return data

# Load Data
full_curriculum = get_curriculum()
# Add placeholders for the rest of the year so the app functions fully
full_curriculum.update(generate_placeholder_data(2, 10, "Phase 1: Foundations"))
full_curriculum.update(generate_placeholder_data(11, 20, "Phase 2: Security+ & N5"))
full_curriculum.update(generate_placeholder_data(21, 30, "Phase 3: Calculus I & Pentest+"))
full_curriculum.update(generate_placeholder_data(31, 40, "Phase 4: Calc II & CySA+"))


# --- SIDEBAR ---
with st.sidebar:
    st.title("📊 Mastery Tracker")
    st.markdown("---")
    
    # Calculate Stats
    total_tasks = 40 * 7 * 3 # 40 weeks, 7 days, 3 subjects
    completed_count = sum(st.session_state.progress.values())
    percent_complete = (completed_count / total_tasks)
    
    st.metric("Total Progress", f"{percent_complete:.1%}")
    st.progress(percent_complete)
    
    st.markdown("### Navigation")
    selected_week = st.selectbox("Select Current Week", list(range(1, 41)))
    
    # Reset Button
    if st.button("Reset All Progress", type="primary"):
        st.session_state.progress = {}
        st.rerun()

    st.info("💡 **Tip:** Bookmarks this page. Your progress is saved in this browser session (don't clear cache!).")

# --- MAIN PAGE ---
curr_week_data = full_curriculum[selected_week]
st.header(f"Week {selected_week}: {curr_week_data['phase']}")
st.markdown("Check off tasks as you complete them to track your 'Triple Threat' journey.")

# Create tabs for days
tabs = st.tabs([f"Day {i}" for i in range(1, 8)])

for day_num, tab in zip(range(1, 8), tabs):
    with tab:
        day_data = curr_week_data["days"][day_num]
        
        col1, col2, col3 = st.columns(3)
        
        # --- MATH COLUMN ---
        with col1:
            st.subheader("📐 Math")
            topic = day_data['math']['topic']
            link = day_data['math']['link']
            
            key = f"w{selected_week}_d{day_num}_math"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done:
                st.session_state.progress[key] = True
            else:
                st.session_state.progress[key] = False
                
            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        # --- JAPANESE COLUMN ---
        with col2:
            st.subheader("🇯🇵 Japanese")
            topic = day_data['jp']['topic']
            link = day_data['jp']['link']
            
            key = f"w{selected_week}_d{day_num}_jp"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done:
                st.session_state.progress[key] = True
            else:
                st.session_state.progress[key] = False

            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        # --- CYBER COLUMN ---
        with col3:
            st.subheader("🛡️ Cyber")
            topic = day_data['cyber']['topic']
            link = day_data['cyber']['link']
            
            key = f"w{selected_week}_d{day_num}_cyber"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done:
                st.session_state.progress[key] = True
            else:
                st.session_state.progress[key] = False

            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        st.markdown("---")
        
        # Motivation logic based on daily completion
        day_keys = [f"w{selected_week}_d{day_num}_{subj}" for subj in ["math", "jp", "cyber"]]
        if all(st.session_state.progress.get(k, False) for k in day_keys):
            st.success(f"🎉 Day {day_num} Complete! Great work.")
