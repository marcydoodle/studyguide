import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="CCSU CyberSecurity Mastery Tracker", layout="wide")

# --- PHASE 1 TASK DATABASE ---
# Sourced from user plan data for weeks 1-16
phase_1_tasks = {
    1: ["Algebra Foundations: Variables/Expressions", "Combining Like Terms", "Linear Equations Intro", "Multi-step Equations", "Parentheses & Solutions", "Unit Test Day"],
    2: ["Slope Intro & Intercept Form", "Graphing from Slope-Intercept", "Point-Slope & Standard Form", "Parallel & Perpendicular Lines", "Catch up on Graphing", "Unit Test Day"],
    3: ["Systems Intro & Graphing", "Substitution Method", "Elimination Method", "Graphing Inequalities", "Systems of Inequalities Word Problems", "Unit Test Day"],
    4: ["Functions, Domain, and Range", "Function Notation & Piecewise", "Arithmetic & Geometric Sequences", "Modeling with Sequences", "Review of Functions", "Unit Test Day"],
    5: ["Exponent Properties Review", "Radicals & Fractional Exponents", "Polynomials & Distributive Property", "Factoring Quadratics Intro", "Factoring Special Products", "Unit Test Day"],
    6: ["Vertex Form & Completing Square", "The Quadratic Formula", "Rational/Irrational Properties", "Catch-up: Complex Factoring", "Algebra 1 Units 11-12 Review", "Unit Test Day"],
    7: ["Alg 1: Unit 13 Focus", "Alg 1: Unit 13 Practice", "Alg 1: Unit 14 Focus", "Alg 1: Unit 14 Practice", "Project: Start Crypto Toolkit", "Unit Test Day"],
    8: ["Alg 1: Unit 15 Focus", "Alg 1: Unit 15 Practice", "Alg 1: Unit 16 Focus", "Alg 1: Unit 16 Practice", "Final Alg 1 Review", "Unit Test Day"],
    9: ["Mastery: Weak Spot Review", "Mastery: Practice Test", "Mastery: Practice Test", "Algebra 1 Course Challenge", "Error Review", "Achieve 100% Mastery"],
    10: ["Polynomial Arithmetic Intro", "Imaginary Numbers & Complex Plane", "Operations with Complex Numbers", "Factoring Higher-Degree Poly", "Remainder Theorem", "Unit Test Day"],
    11: ["Long & Synthetic Division", "End Behavior & Zeros", "Solving Radical Equations", "Intro to 'e' & Continuous Growth", "Review Polynomial Behavior", "Unit Test Day"],
    12: ["Logs & Exponents Relationship", "Log Properties (Product/Quotient)", "Change of Base Rule", "Solving Exponential Eq with Logs", "Logarithmic Graphs", "Mastery Day: 100% Logs"],
    13: ["Shifting & Scaling Functions", "Modeling with Advanced Equations", "Unit Circle & Radians", "Sine, Cosine, & Tangent Graphs", "Inverse Trig Functions", "Unit Test Day"],
    14: ["Asymptotes & End Behavior", "Multiplying/Dividing Rationals", "Adding/Subtracting Rationals", "THM: Linux Hardening", "Review Rational Functions", "Unit Test Day"],
    15: ["Circles and Ellipses", "Hyperbolas and Parabolas", "Basic Matrix Operations", "THM: Windows Hardening", "Review Units 11-12", "Unit Test Day"],
    16: ["Review Algebra 2 Materials", "Course Challenge Prep", "Course Challenge Prep", "Algebra 2 Course Challenge", "Targeted Review", "Achieve 100% Mastery"]
}

# --- RESOURCE LINKS ---
URLS = {
    "math_alg1": "https://www.khanacademy.org/math/algebra",
    "math_alg2": "https://www.khanacademy.org/math/algebra2",
    "thm_sec_eng": "https://tryhackme.com/path/outline/security-engineer-training",
    "fcc_sci": "https://www.freecodecamp.org/learn/scientific-computing-with-python/"
}

# --- APP LAYOUT ---
st.title("🛡️ CCSU Master's Prep Dashboard")

# Initialize Progress State
if 'daily_progress' not in st.session_state:
    st.session_state.daily_progress = {f"wk{w}_day{d}": False for w in range(1, 53) for d in range(1, 7)}

# Sidebar Navigation
st.sidebar.header("Navigation")
phase_choice = st.sidebar.selectbox("Select Study Phase", ["Phase 1: Algebra & Security", "Phase 2-4 (Coming Soon)"])

# Progress Tracking
completed = sum(st.session_state.daily_progress.values())
total_phase1_tasks = 16 * 6
st.sidebar.metric("Phase 1 Progress", f"{completed}/{total_phase1_tasks}")
st.sidebar.progress(min(completed / total_phase1_tasks, 1.0))

# --- DYNAMIC WEEKLY VIEW ---
if "Phase 1" in phase_choice:
    for week in range(1, 17):
        with st.expander(f"📅 WEEK {week}", expanded=(week == 1)):
            # Quick Links
            m_url = URLS["math_alg1"] if week <= 9 else URLS["math_alg2"]
            l_col, r_col = st.columns(2)
            l_col.link_button(f"🔢 Khan Academy Week {week}", m_url, use_container_width=True)
            r_col.link_button("🛡️ TryHackMe Path", URLS["thm_sec_eng"], use_container_width=True)

            # Specific Daily Tasks from the Dictionary
            st.markdown("---")
            tasks = phase_1_tasks.get(week, ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6"])
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            
            for i, task_text in enumerate(tasks):
                key = f"wk{week}_day{i+1}"
                st.session_state.daily_progress[key] = st.checkbox(
                    f"**{days[i]}:** {task_text}", 
                    value=st.session_state.daily_progress[key], 
                    key=f"check_{key}"
                )

# GitHub Documentation Section
st.divider()
st.header("🖼️ Current Project: Modular Crypto Toolkit")
[span_0](start_span)st.write("Start building this in **Week 7** to demonstrate your understanding of Binary Ops and Modular Arithmetic[span_0](end_span).")

with st.expander("View Week 7 Project Requirements"):
    st.markdown("""
    - **[span_1](start_span)RSA Key Generator:** Use Prime Number and Modular Inverse math[span_1](end_span).
    - **[span_2](start_span)XOR Encryptor:** Demonstrate logic gates via bitwise operators[span_2](end_span).
    - **[span_3](start_span)README:** Document 'The Math', 'The Threat', and 'The Engineering'[span_3](end_span).
    """)
