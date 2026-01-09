import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="CCSU CyberSecurity Mastery Tracker", layout="wide")

# --- COMPLETE TASK DATABASE ---
# [span_9](start_span)Phase 1: Algebra (Weeks 1-16)[span_9](end_span)
phase_1_tasks = {
    1: ["Variables/Expressions", "Combining Like Terms", "Linear Equations Intro", "Multi-step Equations", "Parentheses & Solutions", "Unit Test Day"],
    2: ["Slope Intro & Intercept Form", "Graphing from Slope-Intercept", "Point-Slope & Standard Form", "Parallel & Perpendicular Lines", "Catch up on Graphing", "Unit Test Day"],
    3: ["Systems Intro & Graphing", "Substitution Method", "Elimination Method", "Graphing Inequalities", "Systems of Inequalities Word Problems", "Unit Test Day"],
    4: ["Functions, Domain, and Range", "Function Notation & Piecewise", "Arithmetic & Geometric Sequences", "Modeling with Sequences", "Review of Functions", "Unit Test Day"],
    5: ["Exponent Properties Review", "Radicals & Fractional Exponents", "Polynomials & Distributive Property", "Factoring Quadratics Intro", "Factoring Special Products", "Unit Test Day"],
    6: ["Vertex Form & Completing Square", "The Quadratic Formula", "Rational/Irrational Properties", "Catch-up: Complex Factoring", "Algebra 1 Units 11-12 Review", "Unit Test Day"],
    7: ["Alg 1: Unit 13 Focus", "Alg 1: Unit 13 Practice", "Alg 1: Unit 14 Focus", "Alg 1: Unit 14 Practice", "Project: Start Crypto Toolkit", "Unit Test Day"],
    8: ["Alg 1: Unit 15 Focus", "Alg 1: Unit 15 Practice", "Alg 1: Unit 16 Focus", "Alg 1: Unit 16 Practice", "Final Alg 1 Review", "Unit Test Day"],
    9: ["Mastery Review", "Practice Test", "Practice Test", "Algebra 1 Course Challenge", "Error Review", "100% Mastery"],
    10: ["Polynomial Arithmetic", "Complex Plane", "Operations with Complex Numbers", "Factoring High-Degree Poly", "Remainder Theorem", "Unit Test Day"],
    11: ["Polynomial Division", "End Behavior & Zeros", "Radical Equations", "Intro to 'e'", "Review Polynomials", "Unit Test Day"],
    12: ["Logs/Exponents", "Log Properties", "Change of Base Rule", "Solving Exp Equations", "Logarithmic Graphs", "Mastery: 100% Logs"],
    13: ["Shifting Functions", "Modeling Equations", "Unit Circle & Radians", "Trig Graphs", "Inverse Trig", "Unit Test Day"],
    14: ["Asymptotes", "Multiplying Rationals", "Adding Rationals", "THM: Linux Hardening", "Rational Review", "Unit Test Day"],
    15: ["Conics: Circles/Ellipses", "Hyperbolas/Parabolas", "Matrix Operations", "THM: Windows Hardening", "Review Units 11-12", "Unit Test Day"],
    16: ["Algebra 2 Review", "Practice Challenge", "Practice Challenge", "Algebra 2 Course Challenge", "Targeted Review", "100% Mastery"]
}

# [span_10](start_span)Phase 2: Statistics (Weeks 17-32)[span_10](end_span)
phase_2_tasks = {
    17: ["Categorical Data", "Frequency Tables", "Bar Graphs", "Two-way Tables", "Viz Practice", "Unit 1 Test"],
    18: ["Histograms/Stem Plots", "Box Plots", "Distributions", "Center & Spread", "Review", "Unit 2 Test"],
    19: ["Mean/Median/Mode", "IQR", "Standard Deviation", "Outliers", "Practice", "Unit 3 Test"],
    20: ["Z-Scores/Percentiles", "Normal Intro", "68-95-99.7 Rule", "Area under Curve", "Modeling", "Unit 4 Test"],
    21: ["Scatterplots", "Least-squares Regression", "Residuals", "Correlation", "Influential Points", "Unit 5 Test"],
    22: ["Samples/Populations", "Studies vs Experiments", "Bias", "Design", "Review", "Unit 6 Test"],
    23: ["Basic Prob.", "Mutually Exclusive", "Conditional Prob.", "Bayes' Theorem", "Practice", "Unit 7 Test"],
    24: ["Counting", "Permutations", "Combinations", "Binomial Theorem", "Review", "Unit 8 Test"],
    25: ["Discrete Random Vars", "Expected Value", "Binomial Dist.", "Geometric Dist.", "Review", "Unit 9 Test"],
    26: ["Sampling Proportions", "Central Limit Theorem", "Sampling Means", "Diff of Means", "Practice", "Unit 10 Test"],
    27: ["Critical Values", "Margin of Error", "One-sample Z Intervals", "T Intervals", "Review", "Unit 11 Test"],
    28: ["Hypotheses", "P-values", "Type I/II Errors", "Z Tests", "Review", "Unit 12 Test"],
    29: ["Diff of Two Means", "Diff of Proportions", "Matched Pairs", "Practice", "Inference", "Unit 13 Test"],
    30: ["Chi-square Goodness", "Homogeneity", "Independence", "Review", "Practice", "Unit 14 Test"],
    31: ["Slope Intervals", "Slope Tests", "Non-linear Trans", "Multiple Regression", "Review", "Unit 15 Test"],
    32: ["ANOVA Intro", "F-Statistics", "Final Review", "Stats Course Challenge", "Error Review", "100% Mastery"]
}

# [span_11](start_span)[span_12](start_span)Phase 3 & 4 (Weeks 33-52)[span_11](end_span)[span_12](end_span)
phase_3_tasks = {
    33: ["Limits", "Infinity", "Continuity", "IVT", "Review", "Unit 1 Test"],
    34: ["Derivatives", "Power Rule", "Product/Quotient", "Trig Rules", "Chain Rule", "Unit 2 Test"],
    35: ["Adv Chain Rule", "Implicit Diff", "Inv Trig", "Log Diff", "Review", "Unit 3 Test"],
    36: ["Related Rates", "Linear Approx", "L'Hopital", "Optimization", "Modeling", "Unit 4 Test"],
    37: ["MVT", "EVT", "Concavity", "2nd Deriv", "Curve Sketch", "Unit 5 Test"],
    38: ["Riemann Sums", "FTC", "U-Sub", "Area Under Curve", "Review", "Unit 6 Test"],
    39: ["Diff Equations", "Separation", "Slope Fields", "Exp Models", "Review", "Unit 7 Test"],
    40: ["Area Between Curves", "Disk Method", "Washer Method", "Applications", "Review", "Unit 8 Test"],
    41: ["FRQ Practice", "FRQ Practice", "Timed Drills", "Mock Exam", "Review", "Correction"],
    42: ["Mastery Review", "Practice Challenge", "Practice Challenge", "Calc AB Challenge", "Review", "100% Mastery"]
}

phase_4_tasks = {
    43: ["Vectors", "Span/Basis", "Transformations", "Matrix Products", "Practice", "Unit 1 Test"],
    44: ["Matrix Mult", "Inverse/Det", "Systems", "Null Space", "Practice", "Unit 2 Test"],
    45: ["Eigenvalues", "Change of Basis", "Diagonalization", "Orthogonality", "Review", "Unit 3 Test"],
    46: ["Rank Mastery", "Practice Challenge", "Practice Challenge", "Lin Alg Challenge", "Review", "100% Mastery"],
    47: ["Partial Deriv", "Gradient", "Directional", "Divergence", "Curl", "Unit Test"],
    48: ["Optimization", "Lagrange", "Hessian", "Gradient Descent", "Review", "Unit Test"],
    49: ["Adversarial AI", "Prompt Injection", "Securing ML", "THM Lab", "Practice", "Review"],
    50: ["Retake: Stats", "Stats Review", "Stats Practice", "Stats Mastery", "Review", "100% Mastery"],
    51: ["Retake: Lin Alg", "Lin Alg Review", "Final CTF", "Final CTF", "Final CTF", "VICTORY"],
    52: ["Portfolio Review", "Doc Review", "CCSU App Review", "CCSU App Review", "FINAL SUBMIT", "SUBMITTED"]
}

# --- RESOURCE LINKS ---
URLS = {
    "math_alg1": "https://www.khanacademy.org/math/algebra",
    "math_alg2": "https://www.khanacademy.org/math/algebra2",
    "math_stats": "https://www.khanacademy.org/math/statistics-probability",
    "math_calc": "https://www.khanacademy.org/math/ap-calculus-ab",
    "math_linalg": "https://www.khanacademy.org/math/linear-algebra",
    "math_multi": "https://www.khanacademy.org/math/multivariable-calculus",
    "thm": "https://tryhackme.com/",
    "fcc": "https://www.freecodecamp.org/learn/"
}

# --- APP LAYOUT ---
st.title("🛡️ CCSU Master's Prep Dashboard")

if 'daily_progress' not in st.session_state:
    st.session_state.daily_progress = {f"wk{w}_day{d}": False for w in range(1, 53) for d in range(1, 7)}

st.sidebar.header("Navigation")
phase_choice = st.sidebar.radio("Go to Phase:", ["Phase 1: Algebra", "Phase 2: Statistics", "Phase 3: Calculus", "Phase 4: AI & Final Prep"])

# Overall Progress
completed = sum(st.session_state.daily_progress.values())
st.sidebar.metric("Total Progress", f"{completed}/{52*6}")
st.sidebar.progress(min(completed / (52*6), 1.0))

# [span_13](start_span)[span_14](start_span)[span_15](start_span)[span_16](start_span)Logic for selecting tasks and weeks based on Phase[span_13](end_span)[span_14](end_span)[span_15](end_span)[span_16](end_span)
if "Phase 1" in phase_choice:
    weeks = range(1, 17)
    current_db = phase_1_tasks
elif "Phase 2" in phase_choice:
    weeks = range(17, 33)
    current_db = phase_2_tasks
elif "Phase 3" in phase_choice:
    weeks = range(33, 43)
    current_db = phase_3_tasks
else:
    weeks = range(43, 53)
    current_db = phase_4_tasks

# --- DYNAMIC WEEKLY VIEW ---
for week in weeks:
    with st.expander(f"📅 WEEK {week}", expanded=(week == min(weeks))):
        # [span_17](start_span)[span_18](start_span)[span_19](start_span)[span_20](start_span)Resource Buttons based on week ranges[span_17](end_span)[span_18](end_span)[span_19](end_span)[span_20](end_span)
        if week <= 9: m_url = URLS["math_alg1"]
        elif week <= 16: m_url = URLS["math_alg2"]
        elif week <= 32: m_url = URLS["math_stats"]
        elif week <= 42: m_url = URLS["math_calc"]
        elif week <= 46: m_url = URLS["math_linalg"]
        else: m_url = URLS["math_multi"]

        l_col, r_col = st.columns(2)
        l_col.link_button(f"🔢 Math Week {week}", m_url, use_container_width=True)
        r_col.link_button("🛡️ Labs / Python", URLS["thm"], use_container_width=True)

        st.markdown("---")
        tasks = current_db.get(week, ["Review", "Practice", "Lab", "Project", "Study", "Test"])
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        
        for i, task_text in enumerate(tasks):
            key = f"wk{week}_day{i+1}"
            st.session_state.daily_progress[key] = st.checkbox(
                f"**{days[i]}:** {task_text}", 
                value=st.session_state.daily_progress[key], 
                key=f"check_{key}"
            )
