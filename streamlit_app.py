import streamlit as st
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="Triple Threat Mastery (Weeks 1-40)",
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
    .stCaption {
        font-size: 0.9rem;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'progress' not in st.session_state:
    st.session_state.progress = {}

# --- LINK CONSTANTS ---
MESSER_NET = "https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/"
MESSER_SEC = "https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/"
NET_CHUCK_LINUX = "https://www.youtube.com/playlist?list=PLIhvC56v631Mol7fo3oIzxPHfWdyod8t6"
PYTHON_HUB = "https://www.w3schools.com/python/"
PORT_SWIGGER = "https://portswigger.net/web-security/dashboard"
KHAN_ALG = "https://www.khanacademy.org/math/algebra"
KHAN_CALC1 = "https://www.khanacademy.org/math/calculus-1"
KHAN_LINALG = "https://www.khanacademy.org/math/linear-algebra"
# Replaced Multivariable Calc link with Discrete Math / Statistics
KHAN_STATS = "https://www.khanacademy.org/math/statistics-probability" 

# --- CURRICULUM DATA (WEEKS 1-40) ---
def get_curriculum():
    return {
        # ==========================================
        # PHASE 1: FOUNDATIONS (Weeks 1-10)
        # ==========================================
        1: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Order of Operations", "summary": "Master PEMDAS/BODMAS rules.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana A-O", "summary": "First 5 vowels.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Intro to Networking", "summary": "Purpose of networks.", "link": MESSER_NET}},
            2: {"math": {"topic": "Combining Like Terms", "summary": "Simplify expressions.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana KA-KO", "summary": "K column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "The OSI Model", "summary": "7 Layers.", "link": MESSER_NET}},
            3: {"math": {"topic": "1-Step Equations", "summary": "Solve for x.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana SA-SO", "summary": "S column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "TCP/IP Model", "summary": "4 Layers vs 7 Layers.", "link": MESSER_NET}},
            4: {"math": {"topic": "2-Step Equations", "summary": "Two operations to isolate variable.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana TA-TO", "summary": "T column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Binary & Hex", "summary": "Base-2 and Base-16.", "link": MESSER_NET}},
            5: {"math": {"topic": "Multi-Step Equations", "summary": "Variables on both sides.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana NA-NO", "summary": "N column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "IPv4 Addressing", "summary": "Octets and Classes.", "link": MESSER_NET}},
            6: {"math": {"topic": "Stats: Mean, Median", "summary": "Central tendencies.", "link": KHAN_ALG}, "jp": {"topic": "Writing Practice", "summary": "Drill characters.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Classful Subnetting", "summary": "Default masks.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 1 Review", "summary": "Review Algebra.", "link": KHAN_ALG}, "jp": {"topic": "Anki Setup", "summary": "Install flashcards.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Lab: Install VirtualBox", "summary": "Setup virtualization.", "link": "https://www.virtualbox.org/"}}
        }},
        2: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Slope Formula", "summary": "Rise over run.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana HA-HO", "summary": "H column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "IPv6 Basics", "summary": "128-bit addresses.", "link": MESSER_NET}},
            2: {"math": {"topic": "Slope-Intercept Form", "summary": "y = mx + b.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana MA-MO", "summary": "M column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "DNS Concepts", "summary": "Name resolution.", "link": MESSER_NET}},
            3: {"math": {"topic": "Graphing Lines", "summary": "Plotting linear equations.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana YA-YO", "summary": "Y column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "DHCP Service", "summary": "Dynamic addressing.", "link": MESSER_NET}},
            4: {"math": {"topic": "Point-Slope Form", "summary": "y - y1 = m(x - x1).", "link": KHAN_ALG}, "jp": {"topic": "Hiragana RA-RO", "summary": "R column.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Routers & Switches", "summary": "L2 vs L3.", "link": MESSER_NET}},
            5: {"math": {"topic": "Standard Form", "summary": "Ax + By = C.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana WA-N", "summary": "Final characters.", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "VLANs Basics", "summary": "Network segmentation.", "link": MESSER_NET}},
            6: {"math": {"topic": "Stats: Range & IQR", "summary": "Data spread.", "link": KHAN_ALG}, "jp": {"topic": "Dakuten", "summary": "Voiced sounds (Ga, Za, etc).", "link": "https://www.tofugu.com/japanese/learn-hiragana/"}, "cyber": {"topic": "Common Ports", "summary": "FTP, SSH, HTTP, HTTPS.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 2 Review", "summary": "Linear equations.", "link": KHAN_ALG}, "jp": {"topic": "Hiragana Quiz", "summary": "Full mastery test.", "link": "https://kana-quiz.tofugu.com/"}, "cyber": {"topic": "Flashcards: Ports", "summary": "Memorize port numbers.", "link": "https://quizlet.com/"}}
        }},
        3: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Systems of Eq Intro", "summary": "Intersection of lines.", "link": KHAN_ALG}, "jp": {"topic": "Katakana A-NO", "summary": "Start Katakana.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "TCP vs UDP", "summary": "Reliable vs Fast.", "link": MESSER_NET}},
            2: {"math": {"topic": "Substitution Method", "summary": "Solve by sub.", "link": KHAN_ALG}, "jp": {"topic": "Katakana HA-HO", "summary": "Ha-Ho rows.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Wireless Standards", "summary": "802.11 a/b/g/n/ac/ax.", "link": MESSER_NET}},
            3: {"math": {"topic": "Elimination Method", "summary": "Add/Subtract equations.", "link": KHAN_ALG}, "jp": {"topic": "Katakana MA-YO", "summary": "Ma-Yo rows.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "2.4 vs 5 GHz", "summary": "Frequencies.", "link": MESSER_NET}},
            4: {"math": {"topic": "Systems Word Probs", "summary": "Real world models.", "link": KHAN_ALG}, "jp": {"topic": "Katakana RA-N", "summary": "Finish Katakana.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Network Topologies", "summary": "Star, Ring, Mesh.", "link": MESSER_NET}},
            5: {"math": {"topic": "Systems Review", "summary": "Practice all methods.", "link": KHAN_ALG}, "jp": {"topic": "Long Vowels", "summary": "Dash symbol.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Cable Types", "summary": "Copper, Fiber, Plenum.", "link": MESSER_NET}},
            6: {"math": {"topic": "Stats: Box Plots", "summary": "Visualizing quartiles.", "link": KHAN_ALG}, "jp": {"topic": "Loanwords", "summary": "Reading English in JP.", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Command Line", "summary": "Ping, ipconfig.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 3 Review", "summary": "Systems and Katakana.", "link": KHAN_ALG}, "jp": {"topic": "Core 2k Deck", "summary": "Start vocab deck.", "link": "https://ankiweb.net/"}, "cyber": {"topic": "Lab: Ping Google", "summary": "First CLI usage.", "link": "https://www.freecodecamp.org/"}}
        }},
        4: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Inequalities", "summary": "Less than / Greater than.", "link": KHAN_ALG}, "jp": {"topic": "Desu / Da", "summary": "To be.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Cloud Concepts", "summary": "SaaS, PaaS, IaaS.", "link": MESSER_NET}},
            2: {"math": {"topic": "Solving Inequalities", "summary": "Flip sign on negative div.", "link": KHAN_ALG}, "jp": {"topic": "Negatives (Janai)", "summary": "Is not.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Virtualization", "summary": "Hypervisors.", "link": MESSER_NET}},
            3: {"math": {"topic": "Graphing Inequalities", "summary": "Shading regions.", "link": KHAN_ALG}, "jp": {"topic": "Past Tense (Datta)", "summary": "Was.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Troubleshooting", "summary": "Methodology.", "link": MESSER_NET}},
            4: {"math": {"topic": "Systems of Ineq", "summary": "Overlapping regions.", "link": KHAN_ALG}, "jp": {"topic": "Past Neg (Janakatta)", "summary": "Was not.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "SOHO Routers", "summary": "Home setup.", "link": MESSER_NET}},
            5: {"math": {"topic": "Modeling with Ineq", "summary": "Word problems.", "link": KHAN_ALG}, "jp": {"topic": "Question Particle", "summary": "Ka.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "CIA Triad", "summary": "Confidentiality, Integrity, Avail.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Standard Dev", "summary": "Variance.", "link": KHAN_ALG}, "jp": {"topic": "Particles WA/GA", "summary": "Topic vs Subject.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Malware Types", "summary": "Virus, Worm, Trojan.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Exam: Phase 1 Math", "summary": "Algebra basics test.", "link": KHAN_ALG}, "jp": {"topic": "Grammar Audit", "summary": "Review weeks 1-4.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Exam: Practice Net+", "summary": "Practice quiz.", "link": "https://www.examcompass.com/"}}
        }},
        5: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Function Mapping", "summary": "Inputs and Outputs.", "link": KHAN_ALG}, "jp": {"topic": "Particle MO", "summary": "Also.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: Intro", "summary": "Kernel vs GUI.", "link": NET_CHUCK_LINUX}},
            2: {"math": {"topic": "Domain & Range", "summary": "Valid inputs/outputs.", "link": KHAN_ALG}, "jp": {"topic": "Particle NO", "summary": "Possession.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: The Shell", "summary": "Terminal basics.", "link": NET_CHUCK_LINUX}},
            3: {"math": {"topic": "Function Notation", "summary": "f(x).", "link": KHAN_ALG}, "jp": {"topic": "Particle O", "summary": "Object marker.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: ls, cd, pwd", "summary": "Navigation.", "link": NET_CHUCK_LINUX}},
            4: {"math": {"topic": "Vert. Line Test", "summary": "Is it a function?", "link": KHAN_ALG}, "jp": {"topic": "Particle NI/E", "summary": "Direction.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: touch, mkdir", "summary": "Creation.", "link": NET_CHUCK_LINUX}},
            5: {"math": {"topic": "Linear vs Nonlinear", "summary": "Constant rate of change.", "link": KHAN_ALG}, "jp": {"topic": "Particle DE", "summary": "Context/Means.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: cp, mv, rm", "summary": "File manipulation.", "link": NET_CHUCK_LINUX}},
            6: {"math": {"topic": "Stats: Histograms", "summary": "Frequency graphs.", "link": KHAN_ALG}, "jp": {"topic": "All Particles", "summary": "Review particles.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Ubuntu VM", "summary": "Install Linux VM.", "link": "https://ubuntu.com/"}},
            7: {"math": {"topic": "Week 5 Review", "summary": "Functions.", "link": KHAN_ALG}, "jp": {"topic": "Anki Review", "summary": "Catch up.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Bandit Level 0", "summary": "OverTheWire Wargame.", "link": "https://overthewire.org/"}}
        }},
        6: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Absolute Value", "summary": "|x| equations.", "link": KHAN_ALG}, "jp": {"topic": "I-Adjectives", "summary": "Conjugation.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: cat, less", "summary": "Reading files.", "link": NET_CHUCK_LINUX}},
            2: {"math": {"topic": "Graphing Abs Val", "summary": "The 'V' shape.", "link": KHAN_ALG}, "jp": {"topic": "I-Adj Conjugation", "summary": "Past/Neg.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: grep", "summary": "Searching text.", "link": NET_CHUCK_LINUX}},
            3: {"math": {"topic": "Piecewise Func", "summary": "Multiple rules.", "link": KHAN_ALG}, "jp": {"topic": "Na-Adjectives", "summary": "Noun-like adjectives.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: Pipes", "summary": "Connecting commands |.", "link": NET_CHUCK_LINUX}},
            4: {"math": {"topic": "Transformations", "summary": "Shifting graphs.", "link": KHAN_ALG}, "jp": {"topic": "Na-Adj Conjugation", "summary": "Past/Neg.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: Permissions", "summary": "chmod.", "link": NET_CHUCK_LINUX}},
            5: {"math": {"topic": "Shifting Func", "summary": "H and K shifts.", "link": KHAN_ALG}, "jp": {"topic": "Adj Vocabulary", "summary": "Colors/Feelings.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: User Mgmt", "summary": "Adduser.", "link": NET_CHUCK_LINUX}},
            6: {"math": {"topic": "Composite Func", "summary": "f(g(x)).", "link": KHAN_ALG}, "jp": {"topic": "Adj Sentences", "summary": "Describing things.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux: apt/dpkg", "summary": "Package managers.", "link": NET_CHUCK_LINUX}},
            7: {"math": {"topic": "Stats: Skewness", "summary": "Left/Right skew.", "link": KHAN_ALG}, "jp": {"topic": "Adj Review", "summary": "Drill adjectives.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: OverTheWire", "summary": "Bandit 1-5.", "link": "https://overthewire.org/"}}
        }},
        7: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Exponent Rules", "summary": "Mult/Div rules.", "link": KHAN_ALG}, "jp": {"topic": "Ru-Verbs", "summary": "Conjugation basics.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Intro to Python", "summary": "Hello World.", "link": PYTHON_HUB}},
            2: {"math": {"topic": "Negative Exponents", "summary": "Reciprocals.", "link": KHAN_ALG}, "jp": {"topic": "U-Verbs", "summary": "Conjugation basics.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: Variables", "summary": "Data types.", "link": PYTHON_HUB}},
            3: {"math": {"topic": "Power Rules", "summary": "Exp to Exp.", "link": KHAN_ALG}, "jp": {"topic": "Irregular Verbs", "summary": "Suru/Kuru.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: Lists", "summary": "Arrays.", "link": PYTHON_HUB}},
            4: {"math": {"topic": "Rational Exponents", "summary": "Fractions as roots.", "link": KHAN_ALG}, "jp": {"topic": "Masu Form", "summary": "Polite form.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: Loops", "summary": "For/While.", "link": PYTHON_HUB}},
            5: {"math": {"topic": "Scientific Notation", "summary": "Large numbers.", "link": KHAN_ALG}, "jp": {"topic": "Dictionary Form", "summary": "Casual form.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: If/Else", "summary": "Logic.", "link": PYTHON_HUB}},
            6: {"math": {"topic": "Stats: Probability", "summary": "Theoretical prob.", "link": KHAN_ALG}, "jp": {"topic": "Polite vs Plain", "summary": "Context usage.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python: Functions", "summary": "Def/Return.", "link": PYTHON_HUB}},
            7: {"math": {"topic": "Week 7 Review", "summary": "Exponents.", "link": KHAN_ALG}, "jp": {"topic": "Verb Drill", "summary": "Conjugation practice.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Python Calc", "summary": "Build calculator.", "link": "https://www.geeksforgeeks.org/"}}
        }},
        8: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Exp. Growth", "summary": "Graphing growth.", "link": KHAN_ALG}, "jp": {"topic": "Verb Neg (Nai)", "summary": "Don't do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Intro to Crypto", "summary": "Encryption basics.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Exp. Decay", "summary": "Graphing decay.", "link": KHAN_ALG}, "jp": {"topic": "Verb Past (Ta)", "summary": "Did.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Sym vs Asym", "summary": "Keys.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Compound Interest", "summary": "Financial formula.", "link": KHAN_ALG}, "jp": {"topic": "Past Neg (Nakatta)", "summary": "Didn't do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Hashing", "summary": "Integrity.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Modeling Exp", "summary": "Word problems.", "link": KHAN_ALG}, "jp": {"topic": "SOV Structure", "summary": "Sentence order.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Digital Sigs", "summary": "Non-repudiation.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Stats: Permutations", "summary": "Order matters.", "link": KHAN_ALG}, "jp": {"topic": "Counting (1-10)", "summary": "Numbers.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "PKI Concepts", "summary": "Certificates.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Math Review", "summary": "Review exp models.", "link": KHAN_ALG}, "jp": {"topic": "High Numbers", "summary": "100+.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Steganography", "summary": "Hidden messages.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Exam: Phase 1", "summary": "Midpoint check.", "link": KHAN_ALG}, "jp": {"topic": "Monthly Review", "summary": "Grammar check.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Hash Calc", "summary": "Verify files.", "link": "https://md5file.com/calculator"}}
        }},
        9: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "FOIL Method", "summary": "Multiplying binomials.", "link": KHAN_ALG}, "jp": {"topic": "Kanji 1-10", "summary": "Basic numbers.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Social Eng", "summary": "Human hacking.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Factoring (a=1)", "summary": "Simple quadratics.", "link": KHAN_ALG}, "jp": {"topic": "Kanji Days", "summary": "Weekdays.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Phishing Types", "summary": "Spear, Whale.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Factoring (a>1)", "summary": "Grouping method.", "link": KHAN_ALG}, "jp": {"topic": "Kanji Body", "summary": "Parts of body.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Malware Types", "summary": "Adware, Rootkit.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Diff of Squares", "summary": "a^2 - b^2.", "link": KHAN_ALG}, "jp": {"topic": "Adverbs", "summary": "Quickly, etc.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Ransomware", "summary": "Extortion.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Perfect Squares", "summary": "(a+b)^2.", "link": KHAN_ALG}, "jp": {"topic": "Locations", "summary": "School, Station.", "link": "https://kanji.garden/"}, "cyber": {"topic": "DoS & DDoS", "summary": "Denial of Service.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Scatterplots", "summary": "Correlations.", "link": KHAN_ALG}, "jp": {"topic": "Interrogatives", "summary": "Question words.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "MITM Attack", "summary": "Interception.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 9 Review", "summary": "Factoring.", "link": KHAN_ALG}, "jp": {"topic": "Stroke Order", "summary": "Writing rules.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Lab: Phish Quiz", "summary": "Google quiz.", "link": "https://phishingquiz.withgoogle.com/"}}
        }},
        10: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Solve by Factoring", "summary": "Zero product property.", "link": KHAN_ALG}, "jp": {"topic": "Give/Receive", "summary": "Ageru/Morau.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Physical Sec", "summary": "Locks, cameras.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Complete the Square", "summary": "Vertex form prep.", "link": KHAN_ALG}, "jp": {"topic": "Desiring (~Tai)", "summary": "Want to do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Password Attacks", "summary": "Brute force.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Quadratic Formula", "summary": "The big formula.", "link": KHAN_ALG}, "jp": {"topic": "Tari Tari", "summary": "Listing actions.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Rainbow Tables", "summary": "Pre-computed hashes.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Discriminant", "summary": "Number of solutions.", "link": KHAN_ALG}, "jp": {"topic": "Exist (Aru/Iru)", "summary": "Living vs Non-living.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Logic Bombs", "summary": "Triggered malware.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Vertex Form", "summary": "Graphing parabolas.", "link": KHAN_ALG}, "jp": {"topic": "Counters (~nin)", "summary": "Counting people.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Insider Threat", "summary": "Employee risks.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Correlation", "summary": "R value.", "link": KHAN_ALG}, "jp": {"topic": "Short Stories", "summary": "Reading practice.", "link": "https://www3.nhk.or.jp/news/easy/"}, "cyber": {"topic": "Zero Day", "summary": "No patch available.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 10 Review", "summary": "Quadratics.", "link": KHAN_ALG}, "jp": {"topic": "Review", "summary": "Phase 1 done.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Pwd Check", "summary": "Test strength.", "link": "https://password.kaspersky.com/"}}
        }},
        # ==========================================
        # PHASE 2: SECURITY+ & N5 (Weeks 11-19)
        # ==========================================
        11: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Poly Arithmetic", "summary": "Add/Sub polynomials.", "link": KHAN_ALG}, "jp": {"topic": "Te-form (Ru)", "summary": "Connective form.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Identity Mgmt", "summary": "IAM.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Long Division", "summary": "Poly division.", "link": KHAN_ALG}, "jp": {"topic": "Te-form (U)", "summary": "U-verb rules.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "MFA Factors", "summary": "Know, Have, Are.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Synthetic Div", "summary": "Shortcut division.", "link": KHAN_ALG}, "jp": {"topic": "Te-form (Irr)", "summary": "Suru/Kuru.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Biometrics", "summary": "Physical traits.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Remainder Thm", "summary": "Evaluate via division.", "link": KHAN_ALG}, "jp": {"topic": "Te Connect", "summary": "And then...", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Authorization", "summary": "Least Privilege.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Factor Theorem", "summary": "Is it a factor?", "link": KHAN_ALG}, "jp": {"topic": "Te Requests", "summary": "Please do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "SSO & Fed", "summary": "Single Sign On.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Best Fit", "summary": "Regression lines.", "link": KHAN_ALG}, "jp": {"topic": "Te States", "summary": "Currently doing.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Account Policy", "summary": "Lockouts.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 11 Review", "summary": "Polynomials.", "link": KHAN_ALG}, "jp": {"topic": "Te-form Drill", "summary": "Drill until perfect.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Win Users", "summary": "User mgmt.", "link": "https://www.youtube.com/"}}
        }},
        12: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Rational Funcs", "summary": "Asymptotes.", "link": KHAN_ALG}, "jp": {"topic": "~Mo ii (Perm)", "summary": "May I?", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Firewalls", "summary": "Packet filtering.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Simplify Rat.", "summary": "Cancel factors.", "link": KHAN_ALG}, "jp": {"topic": "Prohibition", "summary": "Must not.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "VPNs", "summary": "Tunnels.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Mult/Div Rat.", "summary": "Operations.", "link": KHAN_ALG}, "jp": {"topic": "~Te kara", "summary": "After doing.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "IDS vs IPS", "summary": "Detect vs Prevent.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Add/Sub Rat.", "summary": "LCD.", "link": KHAN_ALG}, "jp": {"topic": "N5 Grammar", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Proxies", "summary": "Intermediaries.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Solving Rat Eq", "summary": "Clear denominators.", "link": KHAN_ALG}, "jp": {"topic": "N5 Vocab", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Load Balancers", "summary": "Distribution.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Residuals", "summary": "Error analysis.", "link": KHAN_ALG}, "jp": {"topic": "N5 Listening", "summary": "Practice audio.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "SIEM Basics", "summary": "Log aggregation.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 12 Review", "summary": "Rationals.", "link": KHAN_ALG}, "jp": {"topic": "Exam Prep", "summary": "Mock test.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Win FW", "summary": "Config firewall.", "link": "https://www.youtube.com/"}}
        }},
        13: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Pythagorean Thm", "summary": "Right triangles.", "link": KHAN_ALG}, "jp": {"topic": "Kanji (Nature)", "summary": "Elements.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Hardening", "summary": "Securing OS.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Circle Area", "summary": "Pi r squared.", "link": KHAN_ALG}, "jp": {"topic": "Kanji (Direction)", "summary": "Compass.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Patch Mgmt", "summary": "Updates.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Vol (Cylinder)", "summary": "3D shapes.", "link": KHAN_ALG}, "jp": {"topic": "Kanji (Time)", "summary": "Calendar.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Endpoint Sec", "summary": "AV/EDR.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Vol (Cone/Sph)", "summary": "More solids.", "link": KHAN_ALG}, "jp": {"topic": "Potential (Ru)", "summary": "Can do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Disk Encrypt", "summary": "FDE.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Surface Area", "summary": "Covering shapes.", "link": KHAN_ALG}, "jp": {"topic": "Potential (U)", "summary": "Can do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "TPM / HSM", "summary": "Hardware security.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Sampling", "summary": "Methods.", "link": KHAN_ALG}, "jp": {"topic": "'I can do...'", "summary": "Sentences.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Secure Boot", "summary": "Integrity.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 13 Review", "summary": "Geometry.", "link": KHAN_ALG}, "jp": {"topic": "Potential Drill", "summary": "Drill forms.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: BitLocker", "summary": "Encrypt drive.", "link": "https://www.youtube.com/"}}
        }},
        14: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "SOH CAH TOA", "summary": "Trig ratios.", "link": KHAN_ALG}, "jp": {"topic": "Nouns (Koto)", "summary": "Nominalization.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Vuln Scanning", "summary": "Finding flaws.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Missing Sides", "summary": "Solve triangle.", "link": KHAN_ALG}, "jp": {"topic": "~N desu", "summary": "Explanation.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Pentest Intro", "summary": "Ethical hacking.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Inverse Trig", "summary": "Find angles.", "link": KHAN_ALG}, "jp": {"topic": "~To omou", "summary": "I think.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Recon Types", "summary": "Active/Passive.", "link": MESSER_SEC}},
            4: {"math": {"topic": "45-45-90 Tri", "summary": "Special tris.", "link": KHAN_ALG}, "jp": {"topic": "~To iu", "summary": "Quote.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Box Testing", "summary": "Black/White/Gray.", "link": MESSER_SEC}},
            5: {"math": {"topic": "30-60-90 Tri", "summary": "Special tris.", "link": KHAN_ALG}, "jp": {"topic": "Relative Clause", "summary": "Modifying nouns.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Rules of Engage", "summary": "Permissions.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Bias", "summary": "Survey errors.", "link": KHAN_ALG}, "jp": {"topic": "Complex Sent.", "summary": "Nesting.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Red/Blue Teams", "summary": "Roles.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 14 Review", "summary": "Trig basics.", "link": KHAN_ALG}, "jp": {"topic": "Sent Mod", "summary": "Review clauses.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Nmap", "summary": "Scanning.", "link": "https://nmap.org/"}}
        }},
        15: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Radians/Degs", "summary": "Conversion.", "link": KHAN_ALG}, "jp": {"topic": "Comparisons", "summary": "Yori.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Python Sockets", "summary": "Networking code.", "link": PYTHON_HUB}},
            2: {"math": {"topic": "Unit Circle", "summary": "Memorize.", "link": KHAN_ALG}, "jp": {"topic": "Superlatives", "summary": "Ichiban.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Port Scanner", "summary": "Build tool.", "link": PYTHON_HUB}},
            3: {"math": {"topic": "Circle Coords", "summary": "Sin/Cos.", "link": KHAN_ALG}, "jp": {"topic": "~Tara (If)", "summary": "Conditional.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Scripting", "summary": "Automation.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Ref Angles", "summary": "Quadrants.", "link": KHAN_ALG}, "jp": {"topic": "~Ba (If)", "summary": "Conditional.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Packet Analysis", "summary": "Wireshark.", "link": "https://www.wireshark.org/"}},
            5: {"math": {"topic": "Sin/Cos Graph", "summary": "Waves.", "link": KHAN_ALG}, "jp": {"topic": "Volitional", "summary": "Let's do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Attack Vectors", "summary": "Entry points.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Z-Score", "summary": "Normalization.", "link": KHAN_ALG}, "jp": {"topic": "Transitive", "summary": "Verb pairs.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Threat Actors", "summary": "Profiles.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 15 Review", "summary": "Unit Circle.", "link": KHAN_ALG}, "jp": {"topic": "Trig Graphs", "summary": "Plotting.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Wireshark", "summary": "Analyze PCAP.", "link": "https://wiki.wireshark.org/"}}
        }},
        16: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Log Intro", "summary": "Inverse exp.", "link": KHAN_ALG}, "jp": {"topic": "Particle SHI", "summary": "Reasons.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "OWASP Top 10", "summary": "Web risks.", "link": "https://owasp.org/"}},
            2: {"math": {"topic": "Log Properties", "summary": "Expansion.", "link": KHAN_ALG}, "jp": {"topic": "NAGARA", "summary": "Simultaneous.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "SQL Injection", "summary": "Database hack.", "link": PORT_SWIGGER}},
            3: {"math": {"topic": "Expand/Condense", "summary": "Manipulation.", "link": KHAN_ALG}, "jp": {"topic": "NODE / KARA", "summary": "Because.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "XSS Attacks", "summary": "Cross-site script.", "link": PORT_SWIGGER}},
            4: {"math": {"topic": "Natural Log", "summary": "Ln.", "link": KHAN_ALG}, "jp": {"topic": "~Kana (Wonder)", "summary": "Wondering.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "CSRF Attacks", "summary": "Forgery.", "link": PORT_SWIGGER}},
            5: {"math": {"topic": "Log Equations", "summary": "Solving.", "link": KHAN_ALG}, "jp": {"topic": "Passive Voice", "summary": "Rareru.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Dir Traversal", "summary": "File path.", "link": PORT_SWIGGER}},
            6: {"math": {"topic": "Stats: Normal Dist", "summary": "Bell curve.", "link": KHAN_ALG}, "jp": {"topic": "Causative", "summary": "Saseru.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "App Hardening", "summary": "Secure coding.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Exam: Trig/Log", "summary": "Adv Algebra.", "link": KHAN_ALG}, "jp": {"topic": "Phase 4 Rev", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: PortSwigger", "summary": "Web labs.", "link": PORT_SWIGGER}}
        }},
        17: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Binomial Thm", "summary": "Expansion.", "link": KHAN_ALG}, "jp": {"topic": "Keigo Intro", "summary": "Honorifics.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Business Cont.", "summary": "BCP.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Arith Sequence", "summary": "Linear patterns.", "link": KHAN_ALG}, "jp": {"topic": "Kenjougo", "summary": "Humble.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Disaster Rec", "summary": "DRP.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Geom Sequence", "summary": "Exp patterns.", "link": KHAN_ALG}, "jp": {"topic": "Business JP", "summary": "Phrases.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Incident Resp", "summary": "IR Plan.", "link": MESSER_SEC}},
            4: {"math": {"topic": "Sigma Notation", "summary": "Summation.", "link": KHAN_ALG}, "jp": {"topic": "Formal Phone", "summary": "Etiquette.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Forensics", "summary": "Evidence.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Induction", "summary": "Proofs.", "link": KHAN_ALG}, "jp": {"topic": "Advice", "summary": "Suggestions.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Chain of Cust", "summary": "Legal track.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: Sampling", "summary": "Distributions.", "link": KHAN_ALG}, "jp": {"topic": "~Te shimau", "summary": "Regret.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "GDPR", "summary": "Privacy.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 17 Review", "summary": "Sequences.", "link": KHAN_ALG}, "jp": {"topic": "Keigo Audit", "summary": "Check usage.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: IR Plan", "summary": "Playbook.", "link": "https://www.cisa.gov/"}}
        }},
        18: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Limits Concept", "summary": "Approaching.", "link": KHAN_CALC1}, "jp": {"topic": "~Sou desu", "summary": "Looks like.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Cloud Types", "summary": "Public/Private.", "link": MESSER_SEC}},
            2: {"math": {"topic": "Estimating Lim", "summary": "Graphs.", "link": KHAN_CALC1}, "jp": {"topic": "~Rashii", "summary": "Seemingly.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "VM Security", "summary": "Hypervisor sec.", "link": MESSER_SEC}},
            3: {"math": {"topic": "Substitution Lim", "summary": "Plug in.", "link": KHAN_CALC1}, "jp": {"topic": "~Deshou", "summary": "Probably.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Mobile Sec", "summary": "MDM.", "link": MESSER_SEC}},
            4: {"math": {"topic": "One-Sided Lim", "summary": "Left/Right.", "link": KHAN_CALC1}, "jp": {"topic": "~Tame ni", "summary": "For purpose.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "IoT Security", "summary": "Smart devices.", "link": MESSER_SEC}},
            5: {"math": {"topic": "Continuity", "summary": "Smooth curves.", "link": KHAN_CALC1}, "jp": {"topic": "~Yasui/Nikui", "summary": "Easy/Hard.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Physical Ctrl", "summary": "Fences.", "link": MESSER_SEC}},
            6: {"math": {"topic": "Stats: CLT", "summary": "Central Limit.", "link": KHAN_CALC1}, "jp": {"topic": "Podcasts", "summary": "Listening.", "link": "https://nihongoconteppei.com/"}, "cyber": {"topic": "Social Eng", "summary": "Review.", "link": MESSER_SEC}},
            7: {"math": {"topic": "Week 18 Review", "summary": "Limits.", "link": KHAN_CALC1}, "jp": {"topic": "Audit", "summary": "Review.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Exam: Practice Sec+", "summary": "Mock test.", "link": "https://www.examcompass.com/"}}
        }},
        19: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Algebraic Lim", "summary": "Factoring.", "link": KHAN_CALC1}, "jp": {"topic": "News Reading", "summary": "NHK Easy.", "link": "https://www3.nhk.or.jp/news/easy/"}, "cyber": {"topic": "HTML Basics", "summary": "Web structure.", "link": "https://www.w3schools.com/html/"}},
            2: {"math": {"topic": "Conjugates", "summary": "Rationalize.", "link": KHAN_CALC1}, "jp": {"topic": "Journaling", "summary": "Writing.", "link": "https://lang-8.com/"}, "cyber": {"topic": "Cookies", "summary": "Sessions.", "link": "https://developer.mozilla.org/"}},
            3: {"math": {"topic": "Infinite Limits", "summary": "Vertical Asym.", "link": KHAN_CALC1}, "jp": {"topic": "Lang Exchange", "summary": "Chat.", "link": "https://www.hellotalk.com/"}, "cyber": {"topic": "HTTP Headers", "summary": "Requests.", "link": "https://developer.mozilla.org/"}},
            4: {"math": {"topic": "Derivative Intro", "summary": "Slope.", "link": KHAN_CALC1}, "jp": {"topic": "Slang", "summary": "Casual.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Burp Intro", "summary": "Proxy setup.", "link": PORT_SWIGGER}},
            5: {"math": {"topic": "Limit Definition", "summary": "Formal def.", "link": KHAN_CALC1}, "jp": {"topic": "Anime No Subs", "summary": "Immersion.", "link": "https://animelon.com/"}, "cyber": {"topic": "Intercepting", "summary": "Burp basics.", "link": PORT_SWIGGER}},
            6: {"math": {"topic": "Power Rule", "summary": "nx^n-1.", "link": KHAN_CALC1}, "jp": {"topic": "Shadowing", "summary": "Speaking.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Repeater", "summary": "Burp tools.", "link": PORT_SWIGGER}},
            7: {"math": {"topic": "Week 19 Review", "summary": "Derivatives.", "link": KHAN_CALC1}, "jp": {"topic": "Quiz", "summary": "Vocab.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Burp", "summary": "Practice.", "link": PORT_SWIGGER}}
        }},
        # ==========================================
        # PHASE 3: LINEAR ALGEBRA & CYSA+ (Weeks 20-24)
        # ==========================================
        20: {"phase": "Phase 3: Pivot to Blue Team", "days": {
            1: {"math": {"topic": "Vectors Intro", "summary": "Definition, R2/R3, geometric interpretation.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N4 Review", "summary": "Solidify passive/causative forms.", "link": "http://www.guidetojapanese.org/"}, 
                "cyber": {"topic": "CySA+ Domain 1", "summary": "Threat Intelligence concepts.", "link": MESSER_NET}},
            2: {"math": {"topic": "Vector Add/Sub", "summary": "Head-to-tail, parallelogram rules.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Kanji N4 Audit", "summary": "Review weak Kanji.", "link": "https://kanji.garden/"}, 
                "cyber": {"topic": "Threat Actors", "summary": "APT, Hacktivist, Insider profiles.", "link": MESSER_NET}},
            3: {"math": {"topic": "Scalar Multiplication", "summary": "Scaling vectors, direction reversals.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Listening N4", "summary": "JLPT Sample audio.", "link": "https://www.youtube.com/"}, 
                "cyber": {"topic": "Kill Chain", "summary": "Lockheed Martin Cyber Kill Chain.", "link": MESSER_NET}},
            4: {"math": {"topic": "Dot Product", "summary": "Calculation and geometric meaning (angle).", "link": KHAN_LINALG}, 
                "jp": {"topic": "Reading N4", "summary": "Short stories/NHKEasy.", "link": "https://www3.nhk.or.jp/news/easy/"}, 
                "cyber": {"topic": "MITRE ATT&CK", "summary": "Tactics, Techniques, and Procedures (TTPs).", "link": "https://attack.mitre.org/"}},
            5: {"math": {"topic": "Unit Vectors", "summary": "Normalization and standard basis.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Writing", "summary": "Simple diary entry.", "link": "https://lang-8.com/"}, 
                "cyber": {"topic": "Diamond Model", "summary": "Intrusion analysis.", "link": MESSER_NET}},
            6: {"math": {"topic": "Parametric Lines", "summary": "Line equations in vector form.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Speaking", "summary": "Shadowing basics.", "link": "https://www.tofugu.com/"}, 
                "cyber": {"topic": "Log Types", "summary": "Firewall, Switch, Router, Server logs.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 20 Review", "summary": "Vectors basics.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Weekly Test", "summary": "N4 Grammar quiz.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Lab: SIEM Intro", "summary": "Install Splunk Free or ELK Stack.", "link": "https://www.splunk.com/"}}
        }},
        21: {"phase": "Phase 3: Linear Algebra & CySA+", "days": {
            1: {"math": {"topic": "Linear Combinations", "summary": "Spanning a space.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N3 Intro", "summary": "Overview of N3 roadmap.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Syslog & Rsyslog", "summary": "Log collection standards.", "link": MESSER_NET}},
            2: {"math": {"topic": "Span", "summary": "The set of all linear combinations.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Bakari (N3)", "summary": "Just finished doing.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Windows Events", "summary": "Event IDs (4624, 4625, etc).", "link": MESSER_NET}},
            3: {"math": {"topic": "Linear Independence", "summary": "Redundant vectors.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Sa (Suffix)", "summary": "Turning adj into nouns.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Linux Logs", "summary": "/var/log/auth.log, syslog, etc.", "link": MESSER_NET}},
            4: {"math": {"topic": "Subspaces", "summary": "Closure under add/mult.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Mitaida", "summary": "Looks like (N3).", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Vulnerability Mgmt", "summary": "Identification -> Remediation.", "link": MESSER_NET}},
            5: {"math": {"topic": "Basis", "summary": "Minimal spanning set.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Rashii", "summary": "Typical of.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "CVSS Scoring", "summary": "Base, Temporal, Environmental metrics.", "link": "https://nvd.nist.gov/vuln-metrics/cvss"}},
            6: {"math": {"topic": "Dimension", "summary": "Number of vectors in basis.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Ppoi", "summary": "-ish (Casual).", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Scanner Types", "summary": "Credentialed vs Non-credentialed.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 21 Review", "summary": "Span and Basis.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N3 Vocab", "summary": "Anki N3 Deck start.", "link": "https://ankiweb.net/"}, 
                "cyber": {"topic": "Lab: Nessus", "summary": "Run a vulnerability scan.", "link": "https://www.tenable.com/"}}
        }},
        22: {"phase": "Phase 3: Linear Algebra & CySA+", "days": {
            1: {"math": {"topic": "Matrices Intro", "summary": "Rows, Cols, Notation.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Gachi", "summary": "Tend to be.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Software Security", "summary": "SDLC integration.", "link": MESSER_NET}},
            2: {"math": {"topic": "Matrix mult (Vector)", "summary": "Matrix-Vector products.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Kimi", "summary": "Slightly/Touch of.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "OWASP Top 10", "summary": "Review with defensive mindset.", "link": "https://owasp.org/"}},
            3: {"math": {"topic": "Matrix mult (Matrix)", "summary": "Matrix-Matrix products.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Darake", "summary": "Full of (negative).", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Code Analysis", "summary": "Static (SAST) vs Dynamic (DAST).", "link": MESSER_NET}},
            4: {"math": {"topic": "Linear Transformations", "summary": "Matrices as functions.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Muki", "summary": "Suitable for.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Identity Federation", "summary": "SAML, OAuth, OpenID Connect.", "link": MESSER_NET}},
            5: {"math": {"topic": "Identity Matrix", "summary": "Properties of I.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Muke", "summary": "Made for.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Access Controls", "summary": "MAC, DAC, RBAC, ABAC.", "link": MESSER_NET}},
            6: {"math": {"topic": "Matrix Transpose", "summary": "Flipping rows/cols.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Comparisons", "summary": "Review N3 comparison grammar.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Cloud Security", "summary": "Shared Responsibility Model.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 22 Review", "summary": "Matrices.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N3 Kanji", "summary": "First 50 N3 Kanji.", "link": "https://kanji.garden/"}, 
                "cyber": {"topic": "Lab: Burp Suite", "summary": "Analyze web traffic.", "link": "https://portswigger.net/"}}
        }},
        23: {"phase": "Phase 3: Linear Algebra & CySA+", "days": {
            1: {"math": {"topic": "Gaussian Elimination", "summary": "Row reduction (RREF).", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Koto da", "summary": "You should (advice).", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Incident Response", "summary": "Detection & Analysis.", "link": MESSER_NET}},
            2: {"math": {"topic": "Solving Linear Systems", "summary": "Using RREF.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Ni Niteiru", "summary": "Resembles.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Containment", "summary": "Isolation strategies.", "link": MESSER_NET}},
            3: {"math": {"topic": "Homogeneous Systems", "summary": "Ax = 0 solutions.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~You ni suru", "summary": "Make effort to.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Eradication", "summary": "Sanitization & Reimaging.", "link": MESSER_NET}},
            4: {"math": {"topic": "Non-Homogeneous", "summary": "Ax = b solutions.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~You ni naru", "summary": "Become able to.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Recovery", "summary": "Restoration priorities.", "link": MESSER_NET}},
            5: {"math": {"topic": "Matrix Inverses", "summary": "Calculating A^-1.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~You da", "summary": "Appears to be.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Post-Incident", "summary": "Lessons Learned.", "link": MESSER_NET}},
            6: {"math": {"topic": "Invertibility Thm", "summary": "Conditions for inverse.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Keigo (N3)", "summary": "Review honorifics.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Digital Forensics", "summary": "Chain of Custody.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 23 Review", "summary": "Systems of Eq.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N3 Reading", "summary": "Mid-length articles.", "link": "https://www3.nhk.or.jp/"}, 
                "cyber": {"topic": "Lab: IR Plan", "summary": "Draft a tabletop exercise.", "link": "https://www.cisa.gov/"}}
        }},
        24: {"phase": "Phase 3: Linear Algebra & CySA+", "days": {
            1: {"math": {"topic": "Determinants (2x2)", "summary": "ad-bc.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Wake da", "summary": "That's why.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Forensics Tools", "summary": "FTK, EnCase, Volatility.", "link": MESSER_NET}},
            2: {"math": {"topic": "Determinants (3x3)", "summary": "Cofactor expansion.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Wake ga nai", "summary": "No way that...", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Network Forensics", "summary": "Wireshark, TCPDump.", "link": MESSER_NET}},
            3: {"math": {"topic": "Determinant Props", "summary": "Mult/Row Ops.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Wake dewa nai", "summary": "Doesn't mean that...", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Endpoint Forensics", "summary": "Registry, Event Logs.", "link": MESSER_NET}},
            4: {"math": {"topic": "Cross Product", "summary": "Geometry in R3.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Hazu da", "summary": "Supposed to be.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Compliance Frameworks", "summary": "GDPR, PCI-DSS, HIPAA.", "link": MESSER_NET}},
            5: {"math": {"topic": "Cramer's Rule", "summary": "Solving with Dets.", "link": KHAN_LINALG}, 
                "jp": {"topic": "~Hazu ga nai", "summary": "Cannot be.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Risk Management", "summary": "Risk Register, Heat maps.", "link": MESSER_NET}},
            6: {"math": {"topic": "Volume of Parallelepiped", "summary": "Scalar triple product.", "link": KHAN_LINALG}, 
                "jp": {"topic": "N3 Grammar", "summary": "Halfway check.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Privacy", "summary": "PII, PHI, Data Sovereignty.", "link": MESSER_NET}},
            7: {"math": {"topic": "Week 24 Review", "summary": "Determinants.", "link": KHAN_LINALG}, 
                "jp": {"topic": "Mock N3 Quiz", "summary": "20 questions.", "link": "https://jlptsensei.com/"}, 
                "cyber": {"topic": "Lab: Volatility", "summary": "Analyze a memory dump.", "link": "https://github.com/volatilityfoundation/volatility"}}
        }},
        # ==========================================
        # PHASE 4: LINALG II & PENTEST+ (Weeks 25-30)
        # ==========================================
        25: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Eigenvalues Intro", "summary": "Ax = lambda x.", "link": KHAN_LINALG}, "jp": {"topic": "~Sugiru", "summary": "Too much.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Pentest Intro", "summary": "Rules of Engagement.", "link": MESSER_NET}},
            2: {"math": {"topic": "Finding Eigenvectors", "summary": "Null space of (A-lambda I).", "link": KHAN_LINALG}, "jp": {"topic": "~Yasui/Nikui", "summary": "Easy/Hard to do.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Reconnaissance", "summary": "OSINT, Shodan, Maltego.", "link": "https://www.shodan.io/"}},
            3: {"math": {"topic": "Diagonalization", "summary": "PDP^-1.", "link": KHAN_LINALG}, "jp": {"topic": "Trans Drill", "summary": "Verbs practice.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Scanning", "summary": "Nmap advanced techniques.", "link": "https://nmap.org/"}},
            4: {"math": {"topic": "Linear Dynamic Systems", "summary": "Matrix exponentials.", "link": KHAN_LINALG}, "jp": {"topic": "Imperative", "summary": "Commands.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Enumeration", "summary": "SMB, SNMP, LDAP.", "link": "https://www.kali.org/"}},
            5: {"math": {"topic": "Complex Eigenvalues", "summary": "Rotation matrices.", "link": KHAN_LINALG}, "jp": {"topic": "~Te Oku", "summary": "Prep in advance.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Vulnerability Scanning", "summary": "OpenVAS/Greenbone.", "link": "https://www.openvas.org/"}},
            6: {"math": {"topic": "Systems of Diff Eq", "summary": "Eigenvalue application.", "link": KHAN_LINALG}, "jp": {"topic": "~Te Shimau", "summary": "Regret.", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "False Positives", "summary": "Validating scans.", "link": "https://www.tenable.com/"}},
            7: {"math": {"topic": "Week 25 Review", "summary": "Eigenvalues.", "link": KHAN_LINALG}, "jp": {"topic": "N3 Grammar Quiz", "summary": "Test.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Lab: OpenVAS", "summary": "Scan Metasploitable.", "link": "https://docs.greenbone.net/"}}
        }},
        26: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Orthogonality", "summary": "Perpendicular vectors.", "link": KHAN_LINALG}, "jp": {"topic": "~Koto da", "summary": "Advice.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Exploitation Basics", "summary": "Reverse Shells.", "link": "https://tryhackme.com/"}},
            2: {"math": {"topic": "Orthogonal Complements", "summary": "Null vs Row space.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni Niteiru", "summary": "Resemble.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Metasploit Framework", "summary": "Msfconsole usage.", "link": "https://www.metasploit.com/"}},
            3: {"math": {"topic": "Projections", "summary": "Shadows on subspaces.", "link": KHAN_LINALG}, "jp": {"topic": "~You ni suru", "summary": "Effort.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Privilege Escalation", "summary": "Linux SUID/Kernel.", "link": "https://tryhackme.com/"}},
            4: {"math": {"topic": "Least Squares", "summary": "Approximation.", "link": KHAN_LINALG}, "jp": {"topic": "~You ni naru", "summary": "Change.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Windows PrivEsc", "summary": "Token impersonation.", "link": "https://tryhackme.com/"}},
            5: {"math": {"topic": "Orthonormal Basis", "summary": "Length 1, orthogonal.", "link": KHAN_LINALG}, "jp": {"topic": "~You da", "summary": "Conjecture.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Password Cracking", "summary": "John & Hashcat.", "link": "https://hashcat.net/"}},
            6: {"math": {"topic": "Gram-Schmidt", "summary": "Process to orthogonalize.", "link": KHAN_LINALG}, "jp": {"topic": "Keigo Adv", "summary": "Business.", "link": "https://www.tofugu.com/"}, "cyber": {"topic": "Lateral Movement", "summary": "PsExec, Pass-the-Hash.", "link": "https://attack.mitre.org/"}},
            7: {"math": {"topic": "Week 26 Rev", "summary": "Projections.", "link": KHAN_LINALG}, "jp": {"topic": "Shadowing", "summary": "Speaking.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Lab: THM Blue", "summary": "EternalBlue exploit.", "link": "https://tryhackme.com/"}}
        }},
        27: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Symmetric Matrices", "summary": "A = A^T.", "link": KHAN_LINALG}, "jp": {"topic": "~Wake da", "summary": "Reason.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Persistence", "summary": "Registry keys/Cron.", "link": "https://attack.mitre.org/"}},
            2: {"math": {"topic": "Spectral Theorem", "summary": "Real eigenvalues.", "link": KHAN_LINALG}, "jp": {"topic": "~Wake ga nai", "summary": "No way.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Covering Tracks", "summary": "Log cleaning.", "link": "https://attack.mitre.org/"}},
            3: {"math": {"topic": "Quadratic Forms", "summary": "x^T A x.", "link": KHAN_LINALG}, "jp": {"topic": "~Wake dewa", "summary": "Not really.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Web App Attacks", "summary": "SQL Injection.", "link": PORT_SWIGGER}},
            4: {"math": {"topic": "Positive Definite", "summary": "Energy functions.", "link": KHAN_LINALG}, "jp": {"topic": "~Hazu da", "summary": "Expect.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "XSS", "summary": "Cross-Site Scripting.", "link": PORT_SWIGGER}},
            5: {"math": {"topic": "SVD Intro", "summary": "Singular Value Decomp.", "link": KHAN_LINALG}, "jp": {"topic": "~Hazu ga nai", "summary": "Impossible.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Wireless Attacks", "summary": "Aircrack-ng.", "link": "https://www.aircrack-ng.org/"}},
            6: {"math": {"topic": "SVD Applications", "summary": "Compression.", "link": KHAN_LINALG}, "jp": {"topic": "Kanji N3", "summary": "Writing.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Report Writing", "summary": "Executive Summaries.", "link": "https://www.offensive-security.com/"}},
            7: {"math": {"topic": "Week 27 Rev", "summary": "Symmetric/SVD.", "link": KHAN_LINALG}, "jp": {"topic": "Listening", "summary": "N3 Test.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Lab: DVWA", "summary": "Web vulnerabilities.", "link": "https://github.com/"}}
        }},
        28: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Vector Spaces Rev", "summary": "Axioms review.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni taishite", "summary": "In contrast.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Python Requests", "summary": "Web automation.", "link": "https://realpython.com/"}},
            2: {"math": {"topic": "Null/Col Space Rev", "summary": "Deep dive.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni tsuite", "summary": "About.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Python Scapy", "summary": "Packet crafting.", "link": "https://scapy.net/"}},
            3: {"math": {"topic": "Change of Basis Rev", "summary": "Practice.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni kanshite", "summary": "Concerning.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Bash Scripting", "summary": "Recon loops.", "link": "https://tldp.org/"}},
            4: {"math": {"topic": "LinAlg Apps", "summary": "Markov Chains.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni yotte", "summary": "By means of.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "PowerShell", "summary": "Empire/BloodHound.", "link": "https://github.com/"}},
            5: {"math": {"topic": "LinAlg Apps", "summary": "PageRank.", "link": KHAN_LINALG}, "jp": {"topic": "N3 Reading", "summary": "Articles.", "link": "https://www3.nhk.or.jp/"}, "cyber": {"topic": "Active Directory", "summary": "Kerberoasting.", "link": "https://tryhackme.com/"}},
            6: {"math": {"topic": "LinAlg Apps", "summary": "PCA (Principal Comp).", "link": KHAN_LINALG}, "jp": {"topic": "N3 Vocab", "summary": "Drill.", "link": "https://ankiweb.net/"}, "cyber": {"topic": "AD Persistence", "summary": "Golden Ticket.", "link": "https://tryhackme.com/"}},
            7: {"math": {"topic": "Week 28 Rev", "summary": "Applications.", "link": KHAN_LINALG}, "jp": {"topic": "Mock N3", "summary": "Test.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Lab: AD Lab", "summary": "Attack AD.", "link": "https://www.youtube.com/"}}
        }},
        29: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Intro to Probability", "summary": "Set theory basis.", "link": KHAN_LINALG}, "jp": {"topic": "~To shite", "summary": "As a...", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Buffer Overflow", "summary": "Stack anatomy.", "link": "https://tryhackme.com/"}},
            2: {"math": {"topic": "Perm/Comb Rev", "summary": "Counting.", "link": KHAN_LINALG}, "jp": {"topic": "~To tomo ni", "summary": "Together with.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Fuzzing", "summary": "Spike/Boofuzz.", "link": "https://tryhackme.com/"}},
            3: {"math": {"topic": "Cond Probability", "summary": "P(A|B).", "link": KHAN_LINALG}, "jp": {"topic": "~Ni tsurete", "summary": "As X happens.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Shellcode", "summary": "Generating bad bytes.", "link": "https://www.offsec.com/"}},
            4: {"math": {"topic": "Bayes Theorem", "summary": "Posterior prob.", "link": KHAN_LINALG}, "jp": {"topic": "~Ni shitagatte", "summary": "Following.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "EIP Control", "summary": "Overwriting pointer.", "link": "https://tryhackme.com/"}},
            5: {"math": {"topic": "Random Variables", "summary": "Discrete X.", "link": KHAN_LINALG}, "jp": {"topic": "~Toori ni", "summary": "According to.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "JMP ESP", "summary": "Finding gadgets.", "link": "https://tryhackme.com/"}},
            6: {"math": {"topic": "Expectation/Var", "summary": "E[X] and V[X].", "link": KHAN_LINALG}, "jp": {"topic": "N3 Listening", "summary": "Practice.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Reverse Eng", "summary": "Ghidra intro.", "link": "https://ghidra-sre.org/"}},
            7: {"math": {"topic": "Week 29 Rev", "summary": "Probability.", "link": KHAN_LINALG}, "jp": {"topic": "Writing", "summary": "Essay.", "link": "https://lang-8.com/"}, "cyber": {"topic": "Lab: Brainpan", "summary": "Buffer Overflow.", "link": "https://tryhackme.com/"}}
        }},
        30: {"phase": "Phase 4: LinAlg II & Pentest+", "days": {
            1: {"math": {"topic": "Binomial Dist", "summary": "Success/Fail.", "link": KHAN_LINALG}, "jp": {"topic": "~Koto kara", "summary": "From the fact.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CTF Practice", "summary": "PicoCTF Gen.", "link": "https://picoctf.org/"}},
            2: {"math": {"topic": "Poisson Dist", "summary": "Rare events.", "link": KHAN_LINALG}, "jp": {"topic": "~Koto naku", "summary": "Without doing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CTF Web", "summary": "PicoCTF Web.", "link": "https://picoctf.org/"}},
            3: {"math": {"topic": "Normal Dist Rev", "summary": "Gaussian.", "link": KHAN_LINALG}, "jp": {"topic": "~Mono da", "summary": "Natural thing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CTF Crypto", "summary": "PicoCTF Cryp.", "link": "https://picoctf.org/"}},
            4: {"math": {"topic": "Covariance/Corr", "summary": "Relationships.", "link": KHAN_LINALG}, "jp": {"topic": "Mock Exam", "summary": "N3 Full.", "link": "https://www.jlpt.jp/"}, "cyber": {"topic": "CTF Forensics", "summary": "PicoCTF For.", "link": "https://picoctf.org/"}},
            5: {"math": {"topic": "Markov Chains", "summary": "State transitions.", "link": KHAN_LINALG}, "jp": {"topic": "Analysis", "summary": "Review errors.", "link": "https://www.jlpt.jp/"}, "cyber": {"topic": "CTF BinExp", "summary": "PicoCTF Bin.", "link": "https://picoctf.org/"}},
            6: {"math": {"topic": "Phase 4 Final", "summary": "LinAlg/Prob.", "link": KHAN_LINALG}, "jp": {"topic": "Relax", "summary": "Movie.", "link": "https://www.netflix.com/"}, "cyber": {"topic": "CTF Comp", "summary": "Weekend CTF.", "link": "https://ctftime.org/"}},
            7: {"math": {"topic": "PHASE 4 DONE", "summary": "Review.", "link": KHAN_LINALG}, "jp": {"topic": "CELEBRATE", "summary": "Food.", "link": "https://www.justonecookbook.com/"}, "cyber": {"topic": "RETROSPECT", "summary": "Portfolio.", "link": "https://github.com/"}}
        }},
        # ==========================================
        # PHASE 5: EXPERT - DISCRETE MATH & CASP+ (Weeks 31-40)
        # ==========================================
        31: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Logic: Prop Logic", "summary": "Truth tables, implications.", "link": KHAN_STATS}, "jp": {"topic": "N2 Intro", "summary": "Textbook selection.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASP+ Intro", "summary": "Architecture.", "link": "https://www.comptia.org/"}},
            2: {"math": {"topic": "Logic: Predicates", "summary": "Quantifiers (For all, Exists).", "link": KHAN_STATS}, "jp": {"topic": "~Ni taishite", "summary": "In contrast to.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Ent Security", "summary": "Frameworks.", "link": "https://www.nist.gov/"}},
            3: {"math": {"topic": "Logic: Proofs", "summary": "Direct, Contrapositive.", "link": KHAN_STATS}, "jp": {"topic": "~Ni tsuite", "summary": "Regarding.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Zero Trust", "summary": "Never trust.", "link": "https://www.nist.gov/"}},
            4: {"math": {"topic": "Set Theory", "summary": "Unions, Intersections.", "link": KHAN_STATS}, "jp": {"topic": "~Ni kanshite", "summary": "Concerning.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Virtualization", "summary": "Microservices.", "link": "https://www.docker.com/"}},
            5: {"math": {"topic": "Functions", "summary": "Injective, Surjective.", "link": KHAN_STATS}, "jp": {"topic": "~Ni yotte", "summary": "Depending on.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Container Sec", "summary": "Kubernetes.", "link": "https://kubernetes.io/"}},
            6: {"math": {"topic": "Relations", "summary": "Reflexive, Symmetric, Transitive.", "link": KHAN_STATS}, "jp": {"topic": "N2 Vocab", "summary": "Core 2k.", "link": "https://ankiweb.net/"}, "cyber": {"topic": "Serverless", "summary": "Lambda/Azure Func.", "link": "https://aws.amazon.com/"}},
            7: {"math": {"topic": "Week 31 Rev", "summary": "Logic & Sets.", "link": KHAN_STATS}, "jp": {"topic": "Reading", "summary": "Tech blog.", "link": "https://qiita.com/"}, "cyber": {"topic": "Lab: Docker", "summary": "Secure container.", "link": "https://www.docker.com/"}}
        }},
        32: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Number Theory", "summary": "Divisibility.", "link": KHAN_STATS}, "jp": {"topic": "~To shite", "summary": "As a...", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Crypto Adv", "summary": "Quantum safe.", "link": "https://csrc.nist.gov/"}},
            2: {"math": {"topic": "Modular Arith", "summary": "Clock math (Mod n).", "link": KHAN_STATS}, "jp": {"topic": "~To tomo ni", "summary": "Together with.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Blockchain", "summary": "Ledger sec.", "link": "https://www.ibm.com/"}},
            3: {"math": {"topic": "Primes & GCD", "summary": "Euclidean Algorithm.", "link": KHAN_STATS}, "jp": {"topic": "~Ni tsurete", "summary": "As X happens.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Homomorphic", "summary": "Compute on enc.", "link": "https://www.microsoft.com/"}},
            4: {"math": {"topic": "RSA Math", "summary": "Euler's Totient.", "link": KHAN_STATS}, "jp": {"topic": "~Ni shitagatte", "summary": "Following.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Hardware Sec", "summary": "Firmware.", "link": "https://www.cisa.gov/"}},
            5: {"math": {"topic": "Induction Rev", "summary": "Strong induction.", "link": KHAN_STATS}, "jp": {"topic": "~Toori ni", "summary": "According to.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Mobile Adv", "summary": "Baseband attacks.", "link": "https://owasp.org/"}},
            6: {"math": {"topic": "Recursion", "summary": "Recursive definitions.", "link": KHAN_STATS}, "jp": {"topic": "Listening", "summary": "News.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Drone Sec", "summary": "Signal jamming.", "link": "https://www.cisa.gov/"}},
            7: {"math": {"topic": "Week 32 Rev", "summary": "Num Theory.", "link": KHAN_STATS}, "jp": {"topic": "Kanji N2", "summary": "Start.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Lab: GPG", "summary": "Email enc.", "link": "https://gnupg.org/"}}
        }},
        33: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Counting Basics", "summary": "Pigeonhole Principle.", "link": KHAN_STATS}, "jp": {"topic": "~Koto kara", "summary": "From the fact.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Risk Mgmt", "summary": "RMF.", "link": "https://csrc.nist.gov/"}},
            2: {"math": {"topic": "Permutations", "summary": "Advanced counting.", "link": KHAN_STATS}, "jp": {"topic": "~Koto naku", "summary": "Without doing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Governance", "summary": "Oversight.", "link": "https://www.isaca.org/"}},
            3: {"math": {"topic": "Combinations", "summary": "Binomial coefficients.", "link": KHAN_STATS}, "jp": {"topic": "~Mono da", "summary": "It is natural.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Compliance", "summary": "Intl Stds.", "link": "https://www.iso.org/"}},
            4: {"math": {"topic": "Probability Rev", "summary": "Discrete prob.", "link": KHAN_STATS}, "jp": {"topic": "~Mono dakara", "summary": "Because (Excuse).", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Legal", "summary": "E-discovery.", "link": "https://www.americanbar.org/"}},
            5: {"math": {"topic": "Bayes Rev", "summary": "Conditional.", "link": KHAN_STATS}, "jp": {"topic": "~Mono nara", "summary": "If I could.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Procurement", "summary": "Supply chain.", "link": "https://www.cisa.gov/"}},
            6: {"math": {"topic": "Expected Value", "summary": "Risk calculation.", "link": KHAN_STATS}, "jp": {"topic": "Reading", "summary": "Novels.", "link": "https://syosetu.com/"}, "cyber": {"topic": "Vendor Risk", "summary": "Assessments.", "link": "https://www.cisa.gov/"}},
            7: {"math": {"topic": "Week 33 Rev", "summary": "Combinatorics.", "link": KHAN_STATS}, "jp": {"topic": "Writing", "summary": "Essay.", "link": "https://lang-8.com/"}, "cyber": {"topic": "Lab: Risk Assess", "summary": "Mock audit.", "link": "https://www.nist.gov/"}}
        }},
        34: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Graph Theory", "summary": "Nodes & Edges.", "link": KHAN_STATS}, "jp": {"topic": "~Tatoe ~Temo", "summary": "Even if.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Cloud Arch", "summary": "Hybrid design.", "link": "https://aws.amazon.com/"}},
            2: {"math": {"topic": "Paths & Cycles", "summary": "Eulerian/Hamiltonian.", "link": KHAN_STATS}, "jp": {"topic": "~Ageku", "summary": "In the end (Bad).", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASB", "summary": "Broker.", "link": "https://www.gartner.com/"}},
            3: {"math": {"topic": "Trees", "summary": "Rooted trees.", "link": KHAN_STATS}, "jp": {"topic": "~Sue ni", "summary": "In the end (Good).", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "SDN", "summary": "Software Def Net.", "link": "https://www.cisco.com/"}},
            4: {"math": {"topic": "Spanning Trees", "summary": "MST Algorithms.", "link": KHAN_STATS}, "jp": {"topic": "~Amari", "summary": "So much that.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Infrastructure", "summary": "IaC (Terraform).", "link": "https://www.terraform.io/"}},
            5: {"math": {"topic": "Shortest Path", "summary": "Dijkstra's Alg.", "link": KHAN_STATS}, "jp": {"topic": "~Ijou", "summary": "Since/Now that.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Automation", "summary": "Ansible.", "link": "https://www.ansible.com/"}},
            6: {"math": {"topic": "Network Flow", "summary": "Max flow.", "link": KHAN_STATS}, "jp": {"topic": "~Ippo", "summary": "On one hand.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "DevSecOps", "summary": "Pipeline sec.", "link": "https://www.redhat.com/"}},
            7: {"math": {"topic": "Week 34 Rev", "summary": "Graphs.", "link": KHAN_STATS}, "jp": {"topic": "Speaking", "summary": "Advanced.", "link": "https://www.italki.com/"}, "cyber": {"topic": "Lab: Terraform", "summary": "Deploy VPC.", "link": "https://learn.hashicorp.com/"}}
        }},
        35: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Planar Graphs", "summary": "Euler's Formula.", "link": KHAN_STATS}, "jp": {"topic": "~Ue de", "summary": "Upon doing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Endpoint Adv", "summary": "EDR tuning.", "link": "https://www.crowdstrike.com/"}},
            2: {"math": {"topic": "Coloring", "summary": "Graph coloring.", "link": KHAN_STATS}, "jp": {"topic": "~Ue wa", "summary": "Since (Formal).", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "HIPS/NIPS", "summary": "Signatures.", "link": "https://www.trellix.com/"}},
            3: {"math": {"topic": "Finite State Machine", "summary": "FSM basics.", "link": KHAN_STATS}, "jp": {"topic": "~Kagiri", "summary": "As long as.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "MDM/UEM", "summary": "Enterprise mobile.", "link": "https://www.vmware.com/"}},
            4: {"math": {"topic": "Automata", "summary": "DFA/NFA.", "link": KHAN_STATS}, "jp": {"topic": "~Osoire ga", "summary": "Fear that.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Boot Sec", "summary": "UEFI/BIOS.", "link": "https://docs.microsoft.com/"}},
            5: {"math": {"topic": "Turing Machines", "summary": "Computation limits.", "link": KHAN_STATS}, "jp": {"topic": "~Ka ~Nai Ka", "summary": "Whether or not.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "WiFi Ent", "summary": "EAP-TLS.", "link": "https://www.cisco.com/"}},
            6: {"math": {"topic": "Algorithm Complexity", "summary": "Big O.", "link": KHAN_STATS}, "jp": {"topic": "N2 Reading", "summary": "News.", "link": "https://www.asahi.com/"}, "cyber": {"topic": "VPN Adv", "summary": "Always-on.", "link": "https://docs.paloaltonetworks.com/"}},
            7: {"math": {"topic": "Week 35 Rev", "summary": "Automata.", "link": KHAN_STATS}, "jp": {"topic": "Immersion", "summary": "Drama.", "link": "https://www.viki.com/"}, "cyber": {"topic": "Lab: EDR", "summary": "Wazuh setup.", "link": "https://wazuh.com/"}}
        }},
        36: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Boolean Algebra", "summary": "Gates/Circuits.", "link": KHAN_STATS}, "jp": {"topic": "~Kane nai", "summary": "Might happen.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Adv Attacks", "summary": "APT lifecycle.", "link": "https://www.mandiant.com/"}},
            2: {"math": {"topic": "Logic Simplification", "summary": "Karnaugh Maps.", "link": KHAN_STATS}, "jp": {"topic": "~Kaneru", "summary": "Cannot do.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Kill Chain", "summary": "Lockheed.", "link": "https://www.lockheedmartin.com/"}},
            3: {"math": {"topic": "Groups & Rings", "summary": "Abstract Algebra Intro.", "link": KHAN_STATS}, "jp": {"topic": "~Gatai", "summary": "Hard to.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "MITRE ATT&CK", "summary": "Mapping.", "link": "https://attack.mitre.org/"}},
            4: {"math": {"topic": "Fields", "summary": "Finite Fields (Crypto).", "link": KHAN_STATS}, "jp": {"topic": "~Zaru o enai", "summary": "Must do.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Threat Hunt", "summary": "Hypothesis.", "link": "https://www.threathunting.net/"}},
            5: {"math": {"topic": "Elliptic Curves", "summary": "ECC basics.", "link": KHAN_STATS}, "jp": {"topic": "~Te yamanai", "summary": "Forever doing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "C2 Frameworks", "summary": "Cobalt Strike.", "link": "https://www.cobaltstrike.com/"}},
            6: {"math": {"topic": "Crypto Math", "summary": "Discrete Log.", "link": KHAN_STATS}, "jp": {"topic": "~Ni wa", "summary": "For a...", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Data Exfil", "summary": "Techniques.", "link": "https://attack.mitre.org/"}},
            7: {"math": {"topic": "Week 36 Rev", "summary": "Boolean/Fields.", "link": KHAN_STATS}, "jp": {"topic": "Vocab N2", "summary": "Business.", "link": "https://ankiweb.net/"}, "cyber": {"topic": "Lab: C2", "summary": "Sliver C2.", "link": "https://github.com/BishopFox/sliver"}}
        }},
        37: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Information Theory", "summary": "Entropy.", "link": KHAN_STATS}, "jp": {"topic": "~Ni watatte", "summary": "Throughout.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Purple Team", "summary": "Collab.", "link": "https://www.sans.org/"}},
            2: {"math": {"topic": "Error Correction", "summary": "Hamming codes.", "link": KHAN_STATS}, "jp": {"topic": "~Oite", "summary": "In/At.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Incident Mgmt", "summary": "Coordination.", "link": "https://www.pagerduty.com/"}},
            3: {"math": {"topic": "Hashing Math", "summary": "Collisions.", "link": KHAN_STATS}, "jp": {"topic": "~Sai ni", "summary": "When.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Crisis Comm", "summary": "PR.", "link": "https://www.ready.gov/"}},
            4: {"math": {"topic": "Discrete Review", "summary": "Logic/Sets.", "link": KHAN_STATS}, "jp": {"topic": "~Sai chuu", "summary": "In middle of.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Forensics Adv", "summary": "Malware Rev.", "link": "https://www.sans.org/"}},
            5: {"math": {"topic": "Adv Problems", "summary": "Proof practice.", "link": KHAN_STATS}, "jp": {"topic": "~Bekida", "summary": "Should.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Mobile Foren", "summary": "iOS/Android.", "link": "https://www.magnetforensics.com/"}},
            6: {"math": {"topic": "App Practice", "summary": "Real world.", "link": KHAN_STATS}, "jp": {"topic": "~Beki dewa", "summary": "Should not.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Network Foren", "summary": "Zeek/Bro.", "link": "https://zeek.org/"}},
            7: {"math": {"topic": "Week 37 Rev", "summary": "Info Theory.", "link": KHAN_STATS}, "jp": {"topic": "Kanji N2", "summary": "Audit.", "link": "https://kanji.garden/"}, "cyber": {"topic": "Lab: Zeek", "summary": "Log analysis.", "link": "https://docs.zeek.org/"}}
        }},
        38: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Final Prep", "summary": "Review 1.", "link": KHAN_STATS}, "jp": {"topic": "~Ta mono da", "summary": "Used to do.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASP+ Rev 1", "summary": "Architecture.", "link": "https://www.comptia.org/"}},
            2: {"math": {"topic": "Final Prep", "summary": "Review 2.", "link": KHAN_STATS}, "jp": {"topic": "~Tsutsu", "summary": "While.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASP+ Rev 2", "summary": "Ops.", "link": "https://www.comptia.org/"}},
            3: {"math": {"topic": "Final Prep", "summary": "Review 3.", "link": KHAN_STATS}, "jp": {"topic": "~Tsutsu aru", "summary": "In process of.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASP+ Rev 3", "summary": "Risk.", "link": "https://www.comptia.org/"}},
            4: {"math": {"topic": "Mock Final", "summary": "Full test.", "link": KHAN_STATS}, "jp": {"topic": "~To wa kagiranai", "summary": "Not always.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "CASP+ Mock", "summary": "Full test.", "link": "https://www.udemy.com/"}},
            5: {"math": {"topic": "Analysis", "summary": "Weak points.", "link": KHAN_STATS}, "jp": {"topic": "~Dake ni", "summary": "Being the case.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Weak Points", "summary": "Drill.", "link": "https://www.comptia.org/"}},
            6: {"math": {"topic": "Relax", "summary": "Mental prep.", "link": KHAN_STATS}, "jp": {"topic": "N2 Mock", "summary": "Full test.", "link": "https://www.jlpt.jp/"}, "cyber": {"topic": "CTF Adv", "summary": "Hard challenge.", "link": "https://ctftime.org/"}},
            7: {"math": {"topic": "Week 38 Rev", "summary": "Ready.", "link": KHAN_STATS}, "jp": {"topic": "Review", "summary": "Correction.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Lab: Final", "summary": "Full network build.", "link": "https://gns3.com/"}}
        }},
        39: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Mastery Check", "summary": "Logic.", "link": KHAN_STATS}, "jp": {"topic": "~Dake atte", "summary": "Appropriate for.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Emerging Tech", "summary": "AI/ML Security.", "link": "https://arxiv.org/"}},
            2: {"math": {"topic": "Mastery Check", "summary": "Graphs.", "link": KHAN_STATS}, "jp": {"topic": "~Tara Saigo", "summary": "Once X happens.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Bio-hacking", "summary": "Medical devices.", "link": "https://www.fda.gov/"}},
            3: {"math": {"topic": "Mastery Check", "summary": "Number Theory.", "link": KHAN_STATS}, "jp": {"topic": "~Tokoro datta", "summary": "Almost happened.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Auto Attacks", "summary": "Car hacking.", "link": "https://timur.tcarisland.com/"}},
            4: {"math": {"topic": "Mastery Check", "summary": "Proofs.", "link": KHAN_STATS}, "jp": {"topic": "~Nai koto wa nai", "summary": "It's not that...", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Space Sec", "summary": "Satellites.", "link": "https://aerospace.org/"}},
            5: {"math": {"topic": "Portfolio", "summary": "Documenting.", "link": "https://github.com/"}, "jp": {"topic": "~Te irai", "summary": "Since doing.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Portfolio", "summary": "GitHub cleanup.", "link": "https://github.com/"}},
            6: {"math": {"topic": "Mentorship", "summary": "Teach someone.", "link": "https://discord.com/"}, "jp": {"topic": "N2 Prep", "summary": "Final Polish.", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Community", "summary": "Write a blog.", "link": "https://medium.com/"}},
            7: {"math": {"topic": "Week 39 Rev", "summary": "Wrap up.", "link": KHAN_STATS}, "jp": {"topic": "Immersion", "summary": "No subs.", "link": "https://www.netflix.com/"}, "cyber": {"topic": "Lab: Custom", "summary": "Build tool.", "link": "https://github.com/"}}
        }},
        40: {"phase": "Phase 5: Expert - Discrete & CASP+", "days": {
            1: {"math": {"topic": "Math Final", "summary": "Discrete Math.", "link": KHAN_STATS}, "jp": {"topic": "N2 Final", "summary": "Review.", "link": "https://www.jlpt.jp/"}, "cyber": {"topic": "CASP+ Final", "summary": "Exam prep.", "link": "https://www.comptia.org/"}},
            2: {"math": {"topic": "Reflection", "summary": "Look back.", "link": "https://dayoneapp.com/"}, "jp": {"topic": "Reflection", "summary": "Look back.", "link": "https://dayoneapp.com/"}, "cyber": {"topic": "Reflection", "summary": "Look back.", "link": "https://dayoneapp.com/"}},
            3: {"math": {"topic": "Planning", "summary": "What's next?", "link": "https://trello.com/"}, "jp": {"topic": "Planning", "summary": "N1?", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Planning", "summary": "CISSP/OSCP?", "link": "https://www.isc2.org/"}},
            4: {"math": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}, "jp": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}, "cyber": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}},
            5: {"math": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}, "jp": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}, "cyber": {"topic": "Rest", "summary": "Recover.", "link": "https://www.headspace.com/"}},
            6: {"math": {"topic": "CELEBRATION", "summary": "You did it.", "link": "https://www.youtube.com/"}, "jp": {"topic": "CELEBRATION", "summary": "You did it.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "CELEBRATION", "summary": "You did it.", "link": "https://www.youtube.com/"}},
            7: {"math": {"topic": "GRADUATION", "summary": "Triple Threat.", "link": "https://www.linkedin.com/"}, "jp": {"topic": "GRADUATION", "summary": "Triple Threat.", "link": "https://www.linkedin.com/"}, "cyber": {"topic": "GRADUATION", "summary": "Triple Threat.", "link": "https://www.linkedin.com/"}}
        }}
    }

# --- SIDEBAR ---
with st.sidebar:
    st.title("📊 Mastery Tracker")
    st.markdown("---")
    
    # Calculate Stats
    full_data = get_curriculum()
    total_tasks = 40 * 7 * 3 
    completed_count = sum(st.session_state.progress.values())
    percent_complete = min((completed_count / total_tasks), 1.0)
    
    st.metric("Total Progress", f"{percent_complete:.1%}")
    st.progress(percent_complete)
    
    st.markdown("### Navigation")
    selected_week = st.selectbox("Select Current Week", list(range(1, 41)))
    
    # Add a reset button
    if st.button("Reset All Progress"):
        st.session_state.progress = {}
        st.experimental_rerun()

# --- MAIN PAGE ---
curr_week_data = get_curriculum()[selected_week]
st.header(f"Week {selected_week}: {curr_week_data['phase']}")
st.markdown("Check off tasks as you complete them to track your 'Triple Threat' journey.")

tabs = st.tabs([f"Day {i}" for i in range(1, 8)])

for day_num, tab in zip(range(1, 8), tabs):
    with tab:
        day_data = curr_week_data["days"][day_num]
        
        col1, col2, col3 = st.columns(3)
        
        # MATH
        with col1:
            st.subheader("📐 Math")
            topic = day_data['math']['topic']
            summary = day_data['math'].get('summary', '')
            link = day_data['math']['link']
            key = f"w{selected_week}_d{day_num}_math"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            if summary:
                st.caption(f"📝 {summary}")
            st.link_button("Go to Resource", link)

        # JAPANESE
        with col2:
            st.subheader("🇯🇵 Japanese")
            topic = day_data['jp']['topic']
            summary = day_data['jp'].get('summary', '')
            link = day_data['jp']['link']
            key = f"w{selected_week}_d{day_num}_jp"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            if summary:
                st.caption(f"📝 {summary}")
            st.link_button("Go to Resource", link)

        # CYBER
        with col3:
            st.subheader("🛡️ Cyber")
            topic = day_data['cyber']['topic']
            summary = day_data['cyber'].get('summary', '')
            link = day_data['cyber']['link']
            key = f"w{selected_week}_d{day_num}_cyber"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            if summary:
                st.caption(f"📝 {summary}")
            st.link_button("Go to Resource", link)

        st.markdown("---")
        
        # Success Message
        day_keys = [f"w{selected_week}_d{day_num}_{subj}" for subj in ["math", "jp", "cyber"]]
        if all(st.session_state.progress.get(k, False) for k in day_keys):
            st.markdown(f"<div class='success-box'>🎉 <b>Day {day_num} Complete!</b> Great work.</div>", unsafe_allow_html=True)
