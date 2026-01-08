import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Triple Threat: Cyber MS -> PhD Track",
    page_icon="🧬",
    layout="wide"
)

# --- CSS FOR STYLING ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        margin-top: 1rem;
    }
    .project-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeeba;
        margin-top: 1rem;
    }
    .research-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #cce5ff;
        color: #004085;
        border: 1px solid #b8daff;
        margin-top: 1rem;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'progress' not in st.session_state:
    st.session_state.progress = {}

# --- RESOURCE LINKS ---
KHAN_SEARCH = "https://www.khanacademy.org/search?page_search_query="
MIT_LINEAR_ALG = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_lectures/"
TREFOR_DISCRETE = "https://www.youtube.com/playlist?list=PLDDGPdw7e6Ag1EIznZ-m-qXu4XX3A0cIz" # Trefor Bazett Discrete Math
ARXIV_SEC = "https://arxiv.org/list/cs.CR/recent"
OIST_ADMISSIONS = "https://admissions.oist.jp/"
PYTHON_DOCS = "https://docs.python.org/3/"
SCAPY_DOCS = "https://scapy.readthedocs.io/en/latest/"

# --- CURRICULUM DATA ---
def get_curriculum():
    return {
        # --- PHASE 1: FOUNDATIONS (Weeks 1-10) ---
        # Standard Foundation Layer
        1: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Order of Operations", "summary": "PEMDAS rules.", "link": f"{KHAN_SEARCH}Order+of+operations"}, "jp": {"topic": "Hiragana A-O", "summary": "First 5 vowels.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Network: OSI Model", "summary": "Layers 1-7.", "link": "https://www.professormesser.com/"}},
            # ... (Placeholder for standard Phase 1 days) ...
            7: {"math": {"topic": "Week 1 Review", "summary": "Algebra basics.", "link": f"{KHAN_SEARCH}Algebra"}, "jp": {"topic": "Anki Setup", "summary": "Daily reps.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Lab: VirtualBox", "summary": "Setup Victim/Attacker VMs.", "link": "https://www.virtualbox.org/"}}
        }},
        
        # --- PHASE 2: SECURITY+ & N5 (Weeks 11-20) ---
        # Standard Security+ Layer
        11: {"phase": "Phase 2: Sec+ & Scripting", "days": {
            1: {"math": {"topic": "Functions Intro", "summary": "Inputs/Outputs.", "link": f"{KHAN_SEARCH}Functions"}, "jp": {"topic": "Te-Form (Ru)", "summary": "Conjugation.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: Variables", "summary": "Data types.", "link": "https://www.w3schools.com/python/"}},
            # ... (Placeholder for standard Phase 2 days) ...
            7: {"math": {"topic": "Review", "summary": "Functions.", "link": f"{KHAN_SEARCH}Algebra2"}, "jp": {"topic": "Te-Form Drill", "summary": "Drill.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Milestone 1: Log Parser", "summary": "Read CSV logs with Python.", "link": PYTHON_DOCS}}
        }},

        # --- PHASE 3: DISCRETE MATH & NET-SENTRY (Weeks 21-30) ---
        # UPDATED: Discrete Math + Net-Sentry Tool Dev
        21: {"phase": "Phase 3: Discrete Math & Net-Sentry", "days": {
            1: {"math": {"topic": "Logic: Truth Tables", "summary": "AND, OR, XOR. The basis of chips.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Passive Voice", "summary": "Rareru form.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Raw Sockets", "summary": "Python socket library intro.", "link": "https://realpython.com/python-sockets/"}},
            2: {"math": {"topic": "Logic: Implications", "summary": "If P then Q.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Passive Sentences", "summary": "Practice.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Python: Error Handling", "summary": "Try/Except blocks.", "link": PYTHON_DOCS}},
            3: {"math": {"topic": "Set Theory", "summary": "Unions, Intersections.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Causative Voice", "summary": "Make/Let.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Tool: Scapy Basics", "summary": "Packet manipulation library.", "link": SCAPY_DOCS}},
            4: {"math": {"topic": "Venn Diagrams", "summary": "Visualizing sets.", "link": f"{KHAN_SEARCH}Venn+diagrams"}, 
                "jp": {"topic": "Causative Practice", "summary": "Drill.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Lab: Local Sniffer", "summary": "Capture 10 packets on localhost.", "link": SCAPY_DOCS}},
            5: {"math": {"topic": "Boolean Algebra", "summary": "Simplifying logic circuits.", "link": f"{KHAN_SEARCH}Boolean+algebra"}, 
                "jp": {"topic": "Keigo: Intro", "summary": "Polite speech levels.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Lab: Filtering", "summary": "Filter for TCP/80 traffic.", "link": SCAPY_DOCS}},
            6: {"math": {"topic": "Boolean Circuits", "summary": "Logic Gates.", "link": f"{KHAN_SEARCH}Logic+gates"}, 
                "jp": {"topic": "Keigo: Sonkeigo", "summary": "Respectful language.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Project: Basic Sniffer", "summary": "Build CLI tool to print packet summaries.", "link": "https://github.com/"}},
            7: {"math": {"topic": "Week 21 Review", "summary": "Logic & Sets.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Keigo Audit", "summary": "Review levels.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Research Journal", "summary": "Document what you built.", "link": "https://github.com/"}}
        }},
        25: {"phase": "Phase 3: Discrete Math & Net-Sentry", "days": {
            1: {"math": {"topic": "Combinatorics", "summary": "Permutations & Combinations.", "link": f"{KHAN_SEARCH}Combinatorics"}, 
                "jp": {"topic": "Transitive Verbs", "summary": "Action done to object.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Attack Sim: Nmap", "summary": "Scan your VM.", "link": "https://nmap.org/"}},
            2: {"math": {"topic": "Combinations", "summary": "Order doesn't matter.", "link": f"{KHAN_SEARCH}Combinations"}, 
                "jp": {"topic": "Intransitive Verbs", "summary": "Action happens.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Lab: Capture Scan", "summary": "Record Nmap traffic with Scapy.", "link": SCAPY_DOCS}},
            3: {"math": {"topic": "Pigeonhole Principle", "summary": "Proof concept.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Trans/Intrans Pairs", "summary": "Drill pairs.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Lab: Signatures", "summary": "Identify Nmap flags in packets.", "link": SCAPY_DOCS}},
            4: {"math": {"topic": "Binomial Coeffs", "summary": "Pascal's Triangle.", "link": f"{KHAN_SEARCH}Binomial+coefficient"}, 
                "jp": {"topic": "Appearance (~Sou)", "summary": "Looks like...", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Python: Detection", "summary": "Script to detect SYN scan pattern.", "link": PYTHON_DOCS}},
            5: {"math": {"topic": "Bayes' Theorem", "summary": "Conditional Probability.", "link": f"{KHAN_SEARCH}Bayes+theorem"}, 
                "jp": {"topic": "Hearsay (~Sou)", "summary": "I heard that...", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Project: Scan Alert", "summary": "Print ALERT when scan detected.", "link": "https://github.com/"}},
            6: {"math": {"topic": "Expected Value", "summary": "Weighted averages.", "link": f"{KHAN_SEARCH}Expected+value"}, 
                "jp": {"topic": "Likeness (~You)", "summary": "Metaphor.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Paper: IDS", "summary": "Read paper on Intrusion Detection.", "link": ARXIV_SEC}},
            7: {"math": {"topic": "Exam: Discrete Midterm", "summary": "Combinatorics/Logic.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Monthly Review", "summary": "Audit all grammar.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Research Journal", "summary": "Update Engineering Log.", "link": "https://github.com/"}}
        }},
        30: {"phase": "Phase 3: Net-Sentry V1.0 Launch", "days": {
            1: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Causative Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Code: Refactor", "summary": "Clean up Sniffer code.", "link": "https://github.com/"}},
            2: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Keigo Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Docs: README", "summary": "Write clear documentation.", "link": "https://github.com/"}},
            3: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Business Phrases", "summary": "Work vocab.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Test: Live Run", "summary": "Run on home network.", "link": "https://github.com/"}},
            4: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Phone Call", "summary": "Phrases.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Release: GitHub", "summary": "Push v1.0 to repo.", "link": "https://github.com/"}},
            5: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Advice Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Video: Demo", "summary": "Record 3 min demo.", "link": "https://obsproject.com/"}},
            6: {"math": {"topic": "Project Week", "summary": "Focus on Code.", "link": "https://github.com/"}, "jp": {"topic": "Regret Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Submit: Portfolio", "summary": "Add to main website/CV.", "link": "https://github.com/"}},
            7: {"math": {"topic": "MILESTONE", "summary": "Net-Sentry V1.0 Live.", "link": "https://github.com/"}, "jp": {"topic": "Keigo Audit", "summary": "Final check.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Celebration", "summary": "Phase 3 Done.", "link": "https://www.youtube.com/"}}
        }},

        # --- PHASE 4: LINEAR ALGEBRA & AI RESEARCH (Weeks 31-40) ---
        # UPDATED: Linear Algebra (for AI) + Research Proposal Prep
        31: {"phase": "Phase 4: Linear Algebra & AI Research", "days": {
            1: {"math": {"topic": "Vectors Intro", "summary": "Magnitude/Direction.", "link": f"{KHAN_SEARCH}Vectors"}, 
                "jp": {"topic": "Academic Vocab", "summary": "Research terms.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Intro to AI Security", "summary": "Adversarial ML basics.", "link": "https://openai.com/research/attacking-machine-learning"}},
            2: {"math": {"topic": "Vector Ops", "summary": "Add/Scale.", "link": f"{KHAN_SEARCH}Vector+addition"}, 
                "jp": {"topic": "Formal Writing", "summary": "Thesis style (De Aru).", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Concept: Supervised", "summary": "Labelled data training.", "link": "https://developers.google.com/machine-learning/crash-course"}},
            3: {"math": {"topic": "Dot Product", "summary": "Similarity measurement.", "link": f"{KHAN_SEARCH}Dot+product"}, 
                "jp": {"topic": "Reading Tech", "summary": "Read Qiita article.", "link": "https://qiita.com/"}, 
                "cyber": {"topic": "Concept: Unsupervised", "summary": "Clustering.", "link": "https://developers.google.com/machine-learning/crash-course"}},
            4: {"math": {"topic": "Unit Vectors", "summary": "Normalization.", "link": f"{KHAN_SEARCH}Unit+vector"}, 
                "jp": {"topic": "Speaking Prep", "summary": "Self-intro for labs.", "link": "https://vocaroo.com/"}, 
                "cyber": {"topic": "Lab: Scikit-Learn", "summary": "Install & Setup.", "link": "https://scikit-learn.org/"}},
            5: {"math": {"topic": "Linear Combinations", "summary": "Spanning space.", "link": f"{KHAN_SEARCH}Linear+combinations"}, 
                "jp": {"topic": "Research Email", "summary": "Draft email to Prof.", "link": "https://www.tofugu.com/"}, 
                "cyber": {"topic": "Lab: Pandas", "summary": "Loading CSV Data.", "link": "https://pandas.pydata.org/"}},
            6: {"math": {"topic": "Basis Vectors", "summary": "Coordinate systems.", "link": f"{KHAN_SEARCH}Basis+vectors"}, 
                "jp": {"topic": "Listening", "summary": "Tech news.", "link": "https://www.youtube.com/"}, 
                "cyber": {"topic": "Paper: ML in Cyber", "summary": "Read survey paper.", "link": ARXIV_SEC}},
            7: {"math": {"topic": "Week 31 Review", "summary": "Vectors.", "link": MIT_LINEAR_ALG}, 
                "jp": {"topic": "Review", "summary": "Weekly Audit.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Research Journal", "summary": "Update Engineering Log.", "link": "https://github.com/"}}
        }},
        35: {"phase": "Phase 4: Linear Algebra & AI Research", "days": {
            1: {"math": {"topic": "Orthogonality", "summary": "Perpendicular vectors.", "link": f"{KHAN_SEARCH}Orthogonal+vectors"}, 
                "jp": {"topic": "Particle SHI", "summary": "Listing reasons.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "OIST Prep: CV", "summary": "Polish CV with Projects.", "link": OIST_ADMISSIONS}},
            2: {"math": {"topic": "Orthogonal Sets", "summary": "Independence.", "link": MIT_LINEAR_ALG}, 
                "jp": {"topic": "NAGARA (While)", "summary": "Multi-tasking.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Draft Introduction.", "link": OIST_ADMISSIONS}},
            3: {"math": {"topic": "Projections", "summary": "Shadows on a plane.", "link": f"{KHAN_SEARCH}Projections+linear+algebra"}, 
                "jp": {"topic": "NODE/KARA", "summary": "Reasons.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Draft Research Plan.", "link": OIST_ADMISSIONS}},
            4: {"math": {"topic": "Gram-Schmidt", "summary": "Orthonormalizing.", "link": f"{KHAN_SEARCH}Gram+schmidt"}, 
                "jp": {"topic": "~Kana (Wonder)", "summary": "Wondering.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Draft Academic History.", "link": OIST_ADMISSIONS}},
            5: {"math": {"topic": "Least Squares", "summary": "Regression math.", "link": f"{KHAN_SEARCH}Least+squares"}, 
                "jp": {"topic": "Passive Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Output: SOP Draft 1", "summary": "Complete first draft.", "link": OIST_ADMISSIONS}},
            6: {"math": {"topic": "Least Squares II", "summary": "Applications.", "link": MIT_LINEAR_ALG}, 
                "jp": {"topic": "Causative Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "Review: Deadlines", "summary": "Check Internship dates.", "link": OIST_ADMISSIONS}},
            7: {"math": {"topic": "Week 35 Review", "summary": "Orthogonality.", "link": MIT_LINEAR_ALG}, 
                "jp": {"topic": "Output Check", "summary": "Review SOP.", "link": OIST_ADMISSIONS}, 
                "cyber": {"topic": "Log: Research Journal", "summary": "Update Engineering Log.", "link": "https://github.com/"}}
        }},
        40: {"phase": "Phase 4: Graduation & Application", "days": {
            1: {"math": {"topic": "PCA Intro", "summary": "Dimensionality Reduction.", "link": "https://setosa.io/ev/principal-component-analysis/"}, "jp": {"topic": "Final Audit", "summary": "N3 Check.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Portfolio: Polish", "summary": "Finalize GitHub.", "link": "https://github.com/"}},
            2: {"math": {"topic": "SVD Intro", "summary": "Singular Value Decomp.", "link": MIT_LINEAR_ALG}, "jp": {"topic": "Interview Prep", "summary": "Why OIST?", "link": "https://vocaroo.com/"}, "cyber": {"topic": "Master's Syllabus", "summary": "Review Week 1.", "link": "https://www.coursera.org/"}},
            3: {"math": {"topic": "Linear Alg Final", "summary": "Cumulative Review.", "link": MIT_LINEAR_ALG}, "jp": {"topic": "Resume JP", "summary": "Translate CV.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Submit: Internship", "summary": "Send application.", "link": OIST_ADMISSIONS}},
            4: {"math": {"topic": "Tensors Preview", "summary": "Math for Deep Learning.", "link": "https://www.tensorflow.org/guide/tensor"}, "jp": {"topic": "Celebration", "summary": "Sushi.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Email Professors", "summary": "Send cold emails.", "link": "https://nii.ac.jp/"}},
            5: {"math": {"topic": "Master's Prep", "summary": "Get textbooks.", "link": "https://www.amazon.com/"}, "jp": {"topic": "Anki Clean", "summary": "Archive decks.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Capstone: Release", "summary": "Make repo public.", "link": "https://github.com/"}},
            6: {"math": {"topic": "Rest", "summary": "Brain recovery.", "link": "https://www.headspace.com/"}, "jp": {"topic": "Rest", "summary": "Brain recovery.", "link": "https://www.headspace.com/"}, "cyber": {"topic": "Rest", "summary": "Brain recovery.", "link": "https://www.headspace.com/"}},
            7: {"math": {"topic": "GRADUATION", "summary": "Ready for Math Research.", "link": MIT_LINEAR_ALG}, "jp": {"topic": "NEXT PHASE", "summary": "Road to OIST.", "link": OIST_ADMISSIONS}, "cyber": {"topic": "MISSION START", "summary": "Begin Cyber MS.", "link": OIST_ADMISSIONS}}
        }}
    }

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Net-Sentry Tracker")
    st.caption("Cyber MS ➡️ OIST PhD Track")
    st.markdown("---")
    
    st.markdown("### 🏆 Project Milestones")
    st.checkbox("Week 10: Log Parser", value=True)
    st.checkbox("Week 20: Port Scanner", value=False)
    st.checkbox("Week 30: Traffic Sniffer", value=False)
    st.checkbox("Week 40: AI Anomaly Detector", value=False)
    
    st.markdown("---")
    # In a full app, you would list all 1-40.
    # For this demo, we list key weeks to verify content.
    selected_week = st.selectbox("Current Week", [1, 11, 21, 25, 30, 31, 35, 40])
    
    if st.button("Reset"):
        st.session_state.progress = {}
        st.experimental_rerun()

# --- MAIN PAGE ---
curriculum = get_curriculum()
curr_week_data = curriculum.get(selected_week, curriculum[1])

st.header(f"Week {selected_week}: {curr_week_data['phase']}")

# Phase Context Alerts
if selected_week <= 10:
    st.info("🏗️ **Foundation Phase:** Build your algebra and network basics. Consistency is key.")
elif 11 <= selected_week <= 20:
    st.info("🐍 **Scripting Phase:** You are moving from 'User' to 'Builder'. Focus on Python.")
elif 21 <= selected_week <= 30:
    st.success("🧩 **Research Phase 1 (Discrete):** You are learning the math of Cryptography and building your Sniffer.")
else:
    st.warning("🧠 **Research Phase 2 (AI):** You are preparing for the PhD. Linear Algebra and Research Proposals are the priority.")

tabs = st.tabs([f"Day {i}" for i in range(1, 8)])

for day_num, tab in zip(range(1, 8), tabs):
    with tab:
        day_data = curr_week_data["days"].get(day_num, {})
        if not day_data: 
            st.write("Rest day or data not loaded.")
            continue
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📐 Math")
            st.markdown(f"**{day_data['math']['topic']}**")
            st.caption(day_data['math']['summary'])
            st.link_button("Study", day_data['math']['link'])
            st.checkbox("Done", key=f"m{selected_week}{day_num}")
            
        with col2:
            st.subheader("🇯🇵 Japanese")
            st.markdown(f"**{day_data['jp']['topic']}**")
            st.caption(day_data['jp']['summary'])
            st.link_button("Study", day_data['jp']['link'])
            st.checkbox("Done", key=f"j{selected_week}{day_num}")
            
        with col3:
            st.subheader("🛡️ Cyber / Research")
            st.markdown(f"**{day_data['cyber']['topic']}**")
            st.caption(day_data['cyber']['summary'])
            st.link_button("Build/Read", day_data['cyber']['link'])
            st.checkbox("Done", key=f"c{selected_week}{day_num}")

        # Special Milestones on Day 7
        if day_num == 7 and selected_week > 20:
             if selected_week == 30:
                 st.markdown("""
                 <div class="project-box">
                 <b>🚀 LAUNCH DAY:</b><br>
                 Net-Sentry V1.0 must be pushed to GitHub today. This is your first major Research Artifact.
                 </div>
                 """, unsafe_allow_html=True)
             else:
                 st.markdown(f"""
                 <div class="research-box">
                 <b>🧬 Researcher's Log:</b><br>
                 Update your Engineering Log with your {day_data['cyber']['topic']} progress.
                 </div>
                 """, unsafe_allow_html=True)
