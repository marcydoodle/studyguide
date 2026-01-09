import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="CCSU CyberSecurity Mastery Tracker", layout="wide")

# --- DATABASE: PHASE 3 (Calculus & Optimization) ---
# [span_3](start_span)Sourced from Units 1-8 and Course Challenge[span_3](end_span)
phase_3_tasks = {
    33: ["Limits Intro & Properties", "Limits at Infinity", "Continuity & IVT", "Asymptotes & Graphs", "Review: Limits", "Unit 1 Test"],
    34: ["Derivative Definition", "Power/Sum/Difference Rules", "Product & Quotient Rules", "Trig Derivatives", "Chain Rule Intro", "Unit 2 Test"],
    35: ["Advanced Chain Rule", "Implicit Differentiation", "Inverse Trig Derivatives", "Logarithmic Differentiation", "Review: Composite Functions", "Unit 3 Test"],
    36: ["Related Rates", "Linear Approximation", "L'Hopital's Rule", "Contextual Apps Practice", "Optimization Modeling", "Unit 4 Test"],
    37: ["Mean Value Theorem", "Extreme Value Theorem", "Increasing/Decreasing Intervals", "Concavity & 2nd Deriv. Test", "Sketching Curves", "Unit 5 Test"],
    38: ["Integration Intro & Riemann Sums", "Fundamental Theorem of Calculus", "U-Substitution", "Integration of Trig/Logs", "Review: Area Under Curve", "Unit 6 Test"],
    39: ["Intro to Differential Equations", "Separation of Variables", "Slope Fields", "Exponential Models", "Review: Diff-Eq", "Unit 7 Test"],
    40: ["Area Between Curves", "Volume: Disk/Washer Method", "Volume: Cross-sections", "Applications of Integration", "Integration Review", "Unit 8 Test"],
    41: ["AP/FRQ Practice Set 1", "AP/FRQ Practice Set 2", "Timed Integration Drills", "Optimization Review", "Calculus Mock Exam", "Review Weak Areas"],
    42: ["Final Mastery Review", "Practice Course Challenge", "Practice Course Challenge", "Calculus AB Course Challenge", "Error Correction", "Achieve 100% Mastery"]
}

# --- DATABASE: PHASE 4 (Linear Algebra & AI) ---
# [span_4](start_span)Sourced from Linear Algebra and Multivariable Partial Derivatives[span_4](end_span)
phase_4_tasks = {
    43: ["Vectors & Linear Combinations", "Span and Basis", "Linear Transformations", "Matrix-Vector Products", "Unit 1 Practice", "Unit 1 Test"],
    44: ["Matrix Multiplication", "Inverse Matrices & Determinants", "Systems as Matrix Equations", "Null Space & Column Space", "Unit 2 Practice", "Unit 2 Test"],
    45: ["Eigenvalues & Eigenvectors", "Change of Basis", "Diagonalization", "Orthogonality", "Linear Algebra Review", "Unit 3 Test"],
    46: ["Matrix Rank Mastery", "Practice Course Challenge", "Practice Course Challenge", "Linear Algebra Course Challenge", "Review Matrix Logic", "Achieve 100% Mastery"],
    47: ["Partial Derivatives Intro", "The Gradient Vector", "Directional Derivatives", "Chain Rule (Multivariable)", "Divergence & Curl", "Partial Deriv. Test"],
    48: ["Optimization (Multivariable)", "Lagrange Multipliers", "Hessian Matrix", "Gradient Descent Logic", "Optimization Drills", "Optimization Test"],
    49: ["Cyber AI: Adversarial AI", "Cyber AI: Prompt Injection", "Securing ML Models", "Certification Practice", "Certification Practice", "Certification Prep Day"],
    50: ["Retake: Stats Challenge", "Retake: Stats Challenge", "Stats Weak Spot Review", "Certification Practice", "Certification Practice", "Stats 100% Mastery"],
    51: ["Retake: Linear Alg Challenge", "Linear Alg Review", "Final CTF Challenge (THM)", "Final CTF Challenge (THM)", "Final CTF Challenge (THM)", "Final CTF Victory"],
    52: ["Final Portfolio Cleanup", "Project Documentation Review", "Project Documentation Review", "Review CCSU Application", "Review CCSU Application", "SUBMIT APPLICATION"]
}

# --- RESOURCE LINKS ---
URLS = {
    "math_calc": "https://www.khanacademy.org/math/ap-calculus-ab",
    "math_linalg": "https://www.khanacademy.org/math/linear-algebra",
    "math_multi": "https://www.khanacademy.org/math/multivariable-calculus",
    "thm_soc1": "https://tryhackme.com/path/outline/soclevel1",
    "thm_soc2": "https://tryhackme.com/path/outline/soclevel2",
    "fcc_ml": "https://www.freecodecamp.org/learn/machine-learning-with-python/"
}

# --- APP LAYOUT ---
st.title("🛡️ CCSU Master's Prep Dashboard")

if 'daily_progress' not in st.session_state:
    st.session_state.daily_progress = {f"wk{w}_day{d}": False for w in range(1, 53) for d in range(1, 7)}

st.sidebar.header("Navigation")
phase_choice = st.sidebar.selectbox("Select Study Phase", ["Phase 3: Calculus", "Phase 4: Linear Algebra & AI"])

# Progress Tracking
completed = sum(st.session_state.daily_progress.values())
st.sidebar.metric("Total Course Progress", f"{completed}/{52*6}")
st.sidebar.progress(min(completed / (52*6), 1.0))

# --- WEEKLY VIEW LOGIC ---
current_phase_tasks = phase_3_tasks if "Phase 3" in phase_choice else phase_4_tasks
weeks = range(33, 43) if "Phase 3" in phase_choice else range(43, 53)

for week in weeks:
    with st.expander(f"📅 WEEK {week}", expanded=(week == min(weeks))):
        # Links selection
        if week <= 42:
            m_url = URLS["math_calc"]
            s_url = URLS["thm_soc1"] if week <= 39 else URLS["thm_soc2"]
        else:
            m_url = URLS["math_linalg"] if week <= 46 else URLS["math_multi"]
            s_url = "https://tryhackme.com/room/introtoaiincyber"

        l_col, r_col = st.columns(2)
        l_col.link_button(f"🔢 Math Week {week}", m_url, use_container_width=True)
        r_col.link_button("🛡️ TryHackMe Lab", s_url, use_container_width=True)

        st.markdown("---")
        tasks = current_phase_tasks.get(week, ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6"])
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        
        for i, task_text in enumerate(tasks):
            key = f"wk{week}_day{i+1}"
            st.session_state.daily_progress[key] = st.checkbox(
                f"**{days[i]}:** {task_text}", 
                value=st.session_state.daily_progress[key], 
                key=f"check_{key}"
            )
