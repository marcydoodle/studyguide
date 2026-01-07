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
                "cyber": {"topic": "IPv6 Basics", "link": "https://www.youtube.com/watch?v=NHqd9319Ff0"}},
            2: {"math": {"topic": "Slope-Intercept Form", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope-intercept-form/v/slope-intercept-form"},
                "jp": {"topic": "Hiragana MA-MO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "DNS Concepts", "link": "https://www.youtube.com/watch?v=27r4B6kcSC4"}},
            3: {"math": {"topic": "Graphing Lines", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope-intercept-form/v/graphing-lines-in-slope-intercept-form"},
                "jp": {"topic": "Hiragana YA-YO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "DHCP Service", "link": "https://www.youtube.com/watch?v=S43jtK9U5I8"}},
            4: {"math": {"topic": "Point-Slope Form", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:point-slope-form/v/point-slope-and-standard-form"},
                "jp": {"topic": "Hiragana RA-RO", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "Routers & Switches", "link": "https://www.youtube.com/watch?v=1z0ULvg_pW8"}},
            5: {"math": {"topic": "Standard Form", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:standard-form/v/standard-form-linear-equations"},
                "jp": {"topic": "Hiragana WA-N", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "VLANs Basics", "link": "https://www.youtube.com/watch?v=Mofp_3D8vX8"}},
            6: {"math": {"topic": "Stats: Range & IQR", "link": "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/interquartile-range-iqr/v/range-variance-and-standard-deviation-as-measures-of-dispersion"},
                "jp": {"topic": "Dakuten Practice", "link": "https://www.tofugu.com/japanese/learn-hiragana/"},
                "cyber": {"topic": "Common Ports", "link": "https://www.youtube.com/watch?v=r_z8F54Z27g"}},
            7: {"math": {"topic": "Week 2 Review", "link": "https://www.khanacademy.org/math/algebra"},
                "jp": {"topic": "Hiragana Quiz", "link": "https://kana-quiz.tofugu.com/"},
                "cyber": {"topic": "Flashcards: Ports", "link": "https://quizlet.com/539304724/common-ports-port-numbers-flash-cards/"}}
        }},
        3: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Systems of Eq Intro", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:introduction-to-systems-of-equations/v/systems-of-equations"}, "jp": {"topic": "Katakana A-NO", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "TCP vs UDP", "link": "https://www.youtube.com/watch?v=Vdc8TCamQMw"}},
            2: {"math": {"topic": "Substitution Method", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-substitution/v/solving-systems-by-substitution-1"}, "jp": {"topic": "Katakana HA-HO", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Wireless Standards", "link": "https://www.youtube.com/watch?v=680o2u1sFjI"}},
            3: {"math": {"topic": "Elimination Method", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-elimination/v/solving-systems-by-elimination"}, "jp": {"topic": "Katakana MA-YO", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "2.4 vs 5 GHz", "link": "https://www.youtube.com/watch?v=2b12R8Vn1YI"}},
            4: {"math": {"topic": "Systems Word Probs", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:systems-of-equations-word-problems/v/systems-of-equations-word-problems"}, "jp": {"topic": "Katakana RA-N", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Network Topologies", "link": "https://www.youtube.com/watch?v=Zb7W19o335Y"}},
            5: {"math": {"topic": "Systems Review", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations"}, "jp": {"topic": "Long Vowels", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Cable Types", "link": "https://www.youtube.com/watch?v=N4e74B7Y_8c"}},
            6: {"math": {"topic": "Stats: Box Plots", "link": "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/v/box-and-whisker-plot"}, "jp": {"topic": "Loanwords", "link": "https://www.tofugu.com/japanese/learn-katakana/"}, "cyber": {"topic": "Command Line Basics", "link": "https://www.youtube.com/watch?v=p4JgXqyH8vU"}},
            7: {"math": {"topic": "Week 3 Review", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Core 2k Deck", "link": "https://ankiweb.net/shared/info/2141233552"}, "cyber": {"topic": "Lab: Ping Google", "link": "https://www.freecodecamp.org/news/how-to-use-the-ping-command/"}}
        }},
        4: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Inequalities", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:inequalities-intro/v/inequalities"}, "jp": {"topic": "Desu / Da", "link": "http://www.guidetojapanese.org/learn/grammar/stateofbeing"}, "cyber": {"topic": "Cloud Concepts", "link": "https://www.youtube.com/watch?v=1KPrb82e9bw"}},
            2: {"math": {"topic": "Solving Inequalities", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:solving-inequalities/v/solving-inequalities"}, "jp": {"topic": "Negatives (Janai)", "link": "http://www.guidetojapanese.org/learn/grammar/stateofbeing"}, "cyber": {"topic": "Virtualization", "link": "https://www.youtube.com/watch?v=G86V3e8K5qA"}},
            3: {"math": {"topic": "Graphing Inequalities", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:graphing-two-variable-inequalities/v/graphing-inequalities"}, "jp": {"topic": "Past Tense (Datta)", "link": "http://www.guidetojapanese.org/learn/grammar/stateofbeing"}, "cyber": {"topic": "Troubleshooting", "link": "https://www.youtube.com/watch?v=lUp4SSsVdJY"}},
            4: {"math": {"topic": "Systems of Ineq", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:systems-two-variable-inequalities/v/graphing-systems-of-inequalities-2"}, "jp": {"topic": "Past Neg (Janakatta)", "link": "http://www.guidetojapanese.org/learn/grammar/stateofbeing"}, "cyber": {"topic": "SOHO Routers", "link": "https://www.youtube.com/watch?v=tT8O9f4u6g4"}},
            5: {"math": {"topic": "Modeling with Ineq", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:modeling-with-linear-inequalities/v/modeling-with-linear-inequalities"}, "jp": {"topic": "Question Particle", "link": "http://www.guidetojapanese.org/learn/grammar/stateofbeing"}, "cyber": {"topic": "CIA Triad", "link": "https://www.youtube.com/watch?v=r2dC2iKte68"}},
            6: {"math": {"topic": "Stats: Standard Dev", "link": "https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/v/variance-of-a-population"}, "jp": {"topic": "Particles WA/GA", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Malware Types", "link": "https://www.youtube.com/watch?v=n8C8vJ7F5gM"}},
            7: {"math": {"topic": "Exam: Phase 1 Math", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Grammar Audit", "link": "https://kana-quiz.tofugu.com/"}, "cyber": {"topic": "Exam: Practice Net+", "link": "https://www.examcompass.com/comptia/network-plus-certification/free-network-plus-practice-tests"}}
        }},
        5: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Function Mapping", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/what-is-a-function"}, "jp": {"topic": "Particle MO", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Linux: Intro", "link": "https://linuxjourney.com/lesson/kernel-overview"}},
            2: {"math": {"topic": "Domain & Range", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:domain-range/v/domain-and-range-from-graphs"}, "jp": {"topic": "Particle NO", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Linux: The Shell", "link": "https://linuxjourney.com/lesson/the-shell"}},
            3: {"math": {"topic": "Function Notation", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/function-notation"}, "jp": {"topic": "Particle O", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Linux: ls, cd, pwd", "link": "https://linuxjourney.com/lesson/navigate-files"}},
            4: {"math": {"topic": "Vert. Line Test", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:vertical-line-test/v/vertical-line-test"}, "jp": {"topic": "Particle NI/E", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Linux: touch, mkdir", "link": "https://linuxjourney.com/lesson/creating-files"}},
            5: {"math": {"topic": "Linear vs Nonlinear", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:recognizing-functions-2/v/linear-nonlinear-functions"}, "jp": {"topic": "Particle DE", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Linux: cp, mv, rm", "link": "https://linuxjourney.com/lesson/copy-move-files"}},
            6: {"math": {"topic": "Stats: Histograms", "link": "https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/histograms-intro"}, "jp": {"topic": "All Particles", "link": "http://www.guidetojapanese.org/learn/grammar/particlesintro"}, "cyber": {"topic": "Lab: Ubuntu VM", "link": "https://ubuntu.com/tutorials/install-ubuntu-desktop-on-virtualbox#1-overview"}},
            7: {"math": {"topic": "Week 5 Review", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Anki Review", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Bandit Level 0", "link": "https://overthewire.org/wargames/bandit/bandit0.html"}}
        }},
        6: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Absolute Value", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:absolute-value-piecewise-functions/x2f8bb11595b61c86:absolute-value-equations/v/absolute-value-equations"}, "jp": {"topic": "I-Adjectives", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: cat, less", "link": "https://linuxjourney.com/lesson/read-files"}},
            2: {"math": {"topic": "Graphing Abs Val", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:absolute-value-piecewise-functions/x2f8bb11595b61c86:graphs-absolute-value/v/shifting-absolute-value-graphs"}, "jp": {"topic": "I-Adj Conjugation", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: grep", "link": "https://linuxjourney.com/lesson/grep-command"}},
            3: {"math": {"topic": "Piecewise Func", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:absolute-value-piecewise-functions/x2f8bb11595b61c86:piecewise-functions/v/piecewise-functions"}, "jp": {"topic": "Na-Adjectives", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: Pipes", "link": "https://linuxjourney.com/lesson/pipes-redirection"}},
            4: {"math": {"topic": "Transformations", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:absolute-value-piecewise-functions/x2f8bb11595b61c86:graphs-absolute-value/v/transforming-absolute-value-functions"}, "jp": {"topic": "Na-Adj Conjugation", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: Permissions", "link": "https://linuxjourney.com/lesson/file-permissions"}},
            5: {"math": {"topic": "Shifting Func", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:absolute-value-piecewise-functions/x2f8bb11595b61c86:graphs-absolute-value/v/shifting-absolute-value-graphs"}, "jp": {"topic": "Adj Vocabulary", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: User Mgmt", "link": "https://linuxjourney.com/lesson/users-groups"}},
            6: {"math": {"topic": "Composite Func", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:transformations/x2ec2f6f830c9fb89:composite-functions/v/function-composition"}, "jp": {"topic": "Adj Sentences", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Linux: apt/dpkg", "link": "https://linuxjourney.com/lesson/dpkg-apt"}},
            7: {"math": {"topic": "Stats: Skewness", "link": "https://www.khanacademy.org/math/ap-statistics/summarizing-quantitative-data-ap/measuring-center-quantitative/v/skewed-data-and-mean-vs-median"}, "jp": {"topic": "Adj Review", "link": "http://www.guidetojapanese.org/learn/grammar/adjectives"}, "cyber": {"topic": "Lab: OverTheWire", "link": "https://overthewire.org/wargames/bandit/"}}
        }},
        7: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Exponent Rules", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:rational-exponents-radicals/x2f8bb11595b61c86:exponent-properties/v/exponent-rules-part-1"}, "jp": {"topic": "Ru-Verbs", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Intro to Python", "link": "https://www.youtube.com/watch?v=eWRfhZUzrAc"}},
            2: {"math": {"topic": "Negative Exponents", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:rational-exponents-radicals/x2f8bb11595b61c86:exponent-properties/v/negative-exponents"}, "jp": {"topic": "U-Verbs", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Python: Variables", "link": "https://www.w3schools.com/python/python_variables.asp"}},
            3: {"math": {"topic": "Power Rules", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:rational-exponents-radicals/x2f8bb11595b61c86:exponent-properties/v/exponent-rules-part-2"}, "jp": {"topic": "Irregular Verbs", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Python: Lists", "link": "https://www.w3schools.com/python/python_lists.asp"}},
            4: {"math": {"topic": "Rational Exponents", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:rational-exponents-radicals/x2f8bb11595b61c86:rational-exponents/v/rational-exponents"}, "jp": {"topic": "Masu Form", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Python: Loops", "link": "https://www.w3schools.com/python/python_for_loops.asp"}},
            5: {"math": {"topic": "Scientific Notation", "link": "https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals/pre-algebra-scientific-notation/v/scientific-notation"}, "jp": {"topic": "Dictionary Form", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Python: If/Else", "link": "https://www.w3schools.com/python/python_conditions.asp"}},
            6: {"math": {"topic": "Stats: Probability", "link": "https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/basic-probability"}, "jp": {"topic": "Polite vs Plain", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Python: Functions", "link": "https://www.w3schools.com/python/python_functions.asp"}},
            7: {"math": {"topic": "Week 7 Review", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Verb Drill", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Lab: Python Calc", "link": "https://www.geeksforgeeks.org/make-simple-calculator-using-python/"}}
        }},
        8: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Exp. Growth", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:exponential-growth-decay/x2f8bb11595b61c86:exponential-vs-linear-growth/v/exponential-growth-functions"}, "jp": {"topic": "Verb Neg (Nai)", "link": "http://www.guidetojapanese.org/learn/grammar/negativeverbs"}, "cyber": {"topic": "Intro to Crypto", "link": "https://www.youtube.com/watch?v=jhXCTbFnK8o"}},
            2: {"math": {"topic": "Exp. Decay", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:exponential-growth-decay/x2f8bb11595b61c86:exponential-vs-linear-growth/v/exponential-decay-functions"}, "jp": {"topic": "Verb Past (Ta)", "link": "http://www.guidetojapanese.org/learn/grammar/past_tense"}, "cyber": {"topic": "Sym vs Asym", "link": "https://www.youtube.com/watch?v=ERp8420ucGs"}},
            3: {"math": {"topic": "Compound Interest", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:exponential-growth-decay/x2f8bb11595b61c86:exponential-models/v/compound-interest"}, "jp": {"topic": "Past Neg (Nakatta)", "link": "http://www.guidetojapanese.org/learn/grammar/past_tense"}, "cyber": {"topic": "Hashing", "link": "https://www.youtube.com/watch?v=2BfMuFAUNQs"}},
            4: {"math": {"topic": "Modeling Exp", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:exponential-growth-decay/x2f8bb11595b61c86:exponential-models/v/constructing-exponential-models"}, "jp": {"topic": "SOV Structure", "link": "http://www.guidetojapanese.org/learn/grammar/basic"}, "cyber": {"topic": "Digital Sigs", "link": "https://www.youtube.com/watch?v=s22eJ1eVLTU"}},
            5: {"math": {"topic": "Stats: Permutations", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinatorics/v/permutations"}, "jp": {"topic": "Counting (1-10)", "link": "https://www.tofugu.com/japanese/counting-in-japanese/"}, "cyber": {"topic": "PKI Concepts", "link": "https://www.youtube.com/watch?v=QSsx3h-k0zM"}},
            6: {"math": {"topic": "Math Review", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "High Numbers", "link": "https://www.tofugu.com/japanese/counting-in-japanese/"}, "cyber": {"topic": "Steganography", "link": "https://www.youtube.com/watch?v=2_X7lQ4G_Sg"}},
            7: {"math": {"topic": "Exam: Phase 1", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Monthly Review", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Hash Calc", "link": "https://md5file.com/calculator"}}
        }},
        9: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "FOIL Method", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:multiply-binomial/v/multiplying-binomials"}, "jp": {"topic": "Kanji 1-10", "link": "https://kanji.garden/"}, "cyber": {"topic": "Social Eng", "link": "https://www.youtube.com/watch?v=lc7scxvKQOo"}},
            2: {"math": {"topic": "Factoring (a=1)", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-quadratics-intro/v/factoring-quadratic-expressions"}, "jp": {"topic": "Kanji Days", "link": "https://kanji.garden/"}, "cyber": {"topic": "Phishing Types", "link": "https://www.youtube.com/watch?v=Y7zNlEMDmI4"}},
            3: {"math": {"topic": "Factoring (a>1)", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-quadratics-strategy/v/factoring-by-grouping"}, "jp": {"topic": "Kanji Body", "link": "https://kanji.garden/"}, "cyber": {"topic": "Malware Types", "link": "https://www.youtube.com/watch?v=fMn_jM5pMZY"}},
            4: {"math": {"topic": "Diff of Squares", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-difference-squares/v/factoring-difference-of-squares"}, "jp": {"topic": "Adverbs", "link": "http://www.guidetojapanese.org/learn/grammar/adverbs"}, "cyber": {"topic": "Ransomware", "link": "https://www.youtube.com/watch?v=N64vL6752dM"}},
            5: {"math": {"topic": "Perfect Squares", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-perfect-squares/v/factoring-perfect-square-trinomials"}, "jp": {"topic": "Locations", "link": "https://kanji.garden/"}, "cyber": {"topic": "DoS & DDoS", "link": "https://www.youtube.com/watch?v=hYiYg7J3rks"}},
            6: {"math": {"topic": "Stats: Scatterplots", "link": "https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/scatterplots-and-correlation/v/constructing-scatter-plot"}, "jp": {"topic": "Interrogatives", "link": "http://www.guidetojapanese.org/learn/grammar/question"}, "cyber": {"topic": "MITM Attack", "link": "https://www.youtube.com/watch?v=-enHmsxOnmM"}},
            7: {"math": {"topic": "Week 9 Review", "link": "https://www.khanacademy.org/math/algebra"}, "jp": {"topic": "Stroke Order", "link": "https://www.tofugu.com/japanese/kanji-stroke-order/"}, "cyber": {"topic": "Lab: Phish Quiz", "link": "https://phishingquiz.withgoogle.com/"}}
        }},
        10: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Solve by Factoring", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:quad-factoring/v/example-1-solving-a-quadratic-equation-by-factoring"}, "jp": {"topic": "Give/Receive", "link": "http://www.guidetojapanese.org/learn/grammar/giving"}, "cyber": {"topic": "Physical Sec", "link": "https://www.youtube.com/watch?v=1F8_qnggC9U"}},
            2: {"math": {"topic": "Complete the Square", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:completing-square-quadratics/v/completing-the-square-1"}, "jp": {"topic": "Desiring (~Tai)", "link": "http://www.guidetojapanese.org/learn/grammar/desire"}, "cyber": {"topic": "Password Attacks", "link": "https://www.youtube.com/watch?v=7U-rbspLDsU"}},
            3: {"math": {"topic": "Quadratic Formula", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-equation/v/using-quadratic-formula"}, "jp": {"topic": "Tari Tari", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Rainbow Tables", "link": "https://www.youtube.com/watch?v=0Apkx4hh0ZI"}},
            4: {"math": {"topic": "Discriminant", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-equation/v/discriminant-of-quadratic-equations"}, "jp": {"topic": "Exist (Aru/Iru)", "link": "http://www.guidetojapanese.org/learn/grammar/verbs"}, "cyber": {"topic": "Logic Bombs", "link": "https://www.techtarget.com/whatis/definition/logic-bomb"}},
            5: {"math": {"topic": "Vertex Form", "link": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:vertex-form/v/vertex-form-intro"}, "jp": {"topic": "Counters (~nin)", "link": "https://www.tofugu.com/japanese/counting-people-nin-ri/"}, "cyber": {"topic": "Insider Threat", "link": "https://www.cisa.gov/topics/physical-security/insider-threat-mitigation"}},
            6: {"math": {"topic": "Stats: Correlation", "link": "https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/scatterplots-and-correlation/v/correlation-coefficient-intuition"}, "jp": {"topic": "Short Stories", "link": "https://www3.nhk.or.jp/news/easy/"}, "cyber": {"topic": "Zero Day", "link": "https://www.youtube.com/watch?v=l5-_xI5_bKQ"}},
            7: {"math": {"topic": "Week 10 Review", "link": "https://www.desmos.com/calculator"}, "jp": {"topic": "Review", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Pwd Check", "link": "https://password.kaspersky.com/"}}
        }},

        # --- PHASE 2: SECURITY+ & N5 (Weeks 11-20) ---
        11: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Poly Arithmetic", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic/x2ec2f6f830c9fb89:poly-add-sub/v/adding-polynomials"}, "jp": {"topic": "Te-form (Ru)", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Identity Mgmt", "link": "https://www.youtube.com/watch?v=0I6u9-6oG3c"}},
            2: {"math": {"topic": "Long Division", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic/x2ec2f6f830c9fb89:poly-div-by-linear/v/polynomial-division"}, "jp": {"topic": "Te-form (U)", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "MFA Factors", "link": "https://www.youtube.com/watch?v=vWdha6c0v9g"}},
            3: {"math": {"topic": "Synthetic Div", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic/x2ec2f6f830c9fb89:synthetic-division/v/synthetic-division"}, "jp": {"topic": "Te-form (Irr)", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Biometrics", "link": "https://www.youtube.com/watch?v=5Q6_fH1hOVM"}},
            4: {"math": {"topic": "Remainder Thm", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic/x2ec2f6f830c9fb89:remainder-theorem/v/polynomial-remainder-theorem"}, "jp": {"topic": "Te Connect", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Authorization", "link": "https://www.youtube.com/watch?v=7pC6vR9vJp0"}},
            5: {"math": {"topic": "Factor Theorem", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:poly-arithmetic/x2ec2f6f830c9fb89:poly-zeros/v/factor-theorem"}, "jp": {"topic": "Te Requests", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "SSO & Fed", "link": "https://www.youtube.com/watch?v=iStxGzp9Vbw"}},
            6: {"math": {"topic": "Stats: Best Fit", "link": "https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/regression-library/v/fitting-a-line-to-data"}, "jp": {"topic": "Te States", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Account Policy", "link": "https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/account-policies"}},
            7: {"math": {"topic": "Week 11 Review", "link": "https://www.khanacademy.org/math/algebra2"}, "jp": {"topic": "Te-form Drill", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Lab: Win Users", "link": "https://www.youtube.com/watch?v=5UeX-wd6Hbw"}}
        }},
        12: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Rational Funcs", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:rational-functions/x2ec2f6f830c9fb89:rational-graphs/v/graphs-of-rational-functions"}, "jp": {"topic": "~Mo ii (Perm)", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "Firewalls", "link": "https://www.youtube.com/watch?v=jW01e2L7qGw"}},
            2: {"math": {"topic": "Simplify Rat.", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:rational-functions/x2ec2f6f830c9fb89:simplify-rational-expressions/v/simplifying-rational-expressions-1"}, "jp": {"topic": "Prohibition", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "VPNs", "link": "https://www.youtube.com/watch?v=P2f0W7Z0W1k"}},
            3: {"math": {"topic": "Mult/Div Rat.", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:rational-functions/x2ec2f6f830c9fb89:multiply-divide-rational-expressions/v/multiplying-rational-expressions"}, "jp": {"topic": "~Te kara", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "IDS vs IPS", "link": "https://www.youtube.com/watch?v=0h9x_Uj9n2I"}},
            4: {"math": {"topic": "Add/Sub Rat.", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:rational-functions/x2ec2f6f830c9fb89:add-sub-rational-expressions/v/adding-rational-expressions"}, "jp": {"topic": "N5 Grammar", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Proxies", "link": "https://www.youtube.com/watch?v=q6d_a_V6cIQ"}},
            5: {"math": {"topic": "Solving Rat Eq", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:rational-functions/x2ec2f6f830c9fb89:rational-equations/v/solving-rational-equations-1"}, "jp": {"topic": "N5 Vocab", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Load Balancers", "link": "https://www.youtube.com/watch?v=2n475k2f54E"}},
            6: {"math": {"topic": "Stats: Residuals", "link": "https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/regression-library/v/residual-plots"}, "jp": {"topic": "N5 Listening", "link": "https://www.youtube.com/watch?v=sFiP5YW1m48"}, "cyber": {"topic": "SIEM Basics", "link": "https://www.youtube.com/watch?v=95-M4fQhY8w"}},
            7: {"math": {"topic": "Week 12 Review", "link": "https://www.khanacademy.org/math/algebra2"}, "jp": {"topic": "Exam Prep", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Win FW", "link": "https://www.youtube.com/watch?v=7uKzVf7rYy8"}}
        }},
        13: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Pythagorean Thm", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-pythagorean-theorem/v/the-pythagorean-theorem"}, "jp": {"topic": "Kanji (Nature)", "link": "https://kanji.garden/"}, "cyber": {"topic": "Hardening", "link": "https://www.youtube.com/watch?v=1F_4S1j3Xy0"}},
            2: {"math": {"topic": "Circle Area", "link": "https://www.khanacademy.org/math/geometry/hs-geo-circles/hs-geo-circle-basics/v/area-of-a-circle"}, "jp": {"topic": "Kanji (Direction)", "link": "https://kanji.garden/"}, "cyber": {"topic": "Patch Mgmt", "link": "https://www.youtube.com/watch?v=1K_4q2_Xy0s"}},
            3: {"math": {"topic": "Vol (Cylinder)", "link": "https://www.khanacademy.org/math/geometry/hs-geo-solids/hs-geo-solids-intro/v/cylinder-volume-and-surface-area"}, "jp": {"topic": "Kanji (Time)", "link": "https://kanji.garden/"}, "cyber": {"topic": "Endpoint Sec", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "Vol (Cone/Sph)", "link": "https://www.khanacademy.org/math/geometry/hs-geo-solids/hs-geo-solids-intro/v/volume-cone"}, "jp": {"topic": "Potential (Ru)", "link": "http://www.guidetojapanese.org/learn/grammar/potential"}, "cyber": {"topic": "Disk Encrypt", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            5: {"math": {"topic": "Surface Area", "link": "https://www.khanacademy.org/math/geometry/hs-geo-solids/hs-geo-solids-intro/v/surface-area-of-a-box"}, "jp": {"topic": "Potential (U)", "link": "http://www.guidetojapanese.org/learn/grammar/potential"}, "cyber": {"topic": "TPM / HSM", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            6: {"math": {"topic": "Stats: Sampling", "link": "https://www.khanacademy.org/math/statistics-probability/designing-studies/types-samples-surveys/v/random-sampling-vs-random-assignment"}, "jp": {"topic": "'I can do...'", "link": "http://www.guidetojapanese.org/learn/grammar/potential"}, "cyber": {"topic": "Secure Boot", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Week 13 Review", "link": "https://www.khanacademy.org/math/geometry"}, "jp": {"topic": "Potential Drill", "link": "http://www.guidetojapanese.org/learn/grammar/potential"}, "cyber": {"topic": "Lab: BitLocker", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}}
        }},
        14: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "SOH CAH TOA", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-trig-ratios-intro/v/basic-trigonometry"}, "jp": {"topic": "Nouns (Koto)", "link": "http://www.guidetojapanese.org/learn/grammar/nounverbs"}, "cyber": {"topic": "Vuln Scanning", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            2: {"math": {"topic": "Missing Sides", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-solve-for-a-side/v/example-trig-to-solve-for-a-side"}, "jp": {"topic": "~N desu", "link": "http://www.guidetojapanese.org/learn/grammar/nounverbs"}, "cyber": {"topic": "Pentest Intro", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            3: {"math": {"topic": "Inverse Trig", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-solve-for-an-angle/v/inverse-trig-functions-intro"}, "jp": {"topic": "~To omou", "link": "http://www.guidetojapanese.org/learn/grammar/nounverbs"}, "cyber": {"topic": "Recon Types", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "45-45-90 Tri", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-special-right-triangles/v/45-45-90-triangles"}, "jp": {"topic": "~To iu", "link": "http://www.guidetojapanese.org/learn/grammar/nounverbs"}, "cyber": {"topic": "Box Testing", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            5: {"math": {"topic": "30-60-90 Tri", "link": "https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-special-right-triangles/v/30-60-90-triangle-example-problem"}, "jp": {"topic": "Relative Clause", "link": "http://www.guidetojapanese.org/learn/grammar/relativeclause"}, "cyber": {"topic": "Rules of Engage", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            6: {"math": {"topic": "Stats: Bias", "link": "https://www.khanacademy.org/math/statistics-probability/designing-studies/types-samples-surveys/v/identifying-bias-survey"}, "jp": {"topic": "Complex Sent.", "link": "http://www.guidetojapanese.org/learn/grammar/relativeclause"}, "cyber": {"topic": "Red/Blue Teams", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Week 14 Review", "link": "https://www.khanacademy.org/math/geometry"}, "jp": {"topic": "Sent Mod", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Nmap", "link": "https://nmap.org/book/install.html"}}
        }},
        15: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Radians/Degs", "link": "https://www.khanacademy.org/math/trigonometry/unit-circle-trig-func/radians/v/introduction-to-radians"}, "jp": {"topic": "Comparisons", "link": "http://www.guidetojapanese.org/learn/grammar/comparison"}, "cyber": {"topic": "Python Sockets", "link": "https://realpython.com/python-sockets/"}},
            2: {"math": {"topic": "Unit Circle", "link": "https://www.khanacademy.org/math/trigonometry/unit-circle-trig-func/unit-circle-definition-of-trig-functions/v/unit-circle-definition-of-trig-functions-1"}, "jp": {"topic": "Superlatives", "link": "http://www.guidetojapanese.org/learn/grammar/comparison"}, "cyber": {"topic": "Port Scanner", "link": "https://www.geeksforgeeks.org/port-scanner-using-python/"}},
            3: {"math": {"topic": "Circle Coords", "link": "https://www.khanacademy.org/math/trigonometry/unit-circle-trig-func/unit-circle-definition-of-trig-functions/v/unit-circle"}, "jp": {"topic": "~Tara (If)", "link": "http://www.guidetojapanese.org/learn/grammar/conditionals"}, "cyber": {"topic": "Scripting", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "Ref Angles", "link": "https://www.khanacademy.org/math/trigonometry/unit-circle-trig-func/trig-values-special-angles/v/reference-angle-1"}, "jp": {"topic": "~Ba (If)", "link": "http://www.guidetojapanese.org/learn/grammar/conditionals"}, "cyber": {"topic": "Packet Analysis", "link": "https://www.youtube.com/watch?v=TkCSr30UojM"}},
            5: {"math": {"topic": "Sin/Cos Graph", "link": "https://www.khanacademy.org/math/trigonometry/trig-with-general-angles/sine-and-cosine-graphs/v/graphing-sine-and-cosine-functions"}, "jp": {"topic": "Volitional", "link": "http://www.guidetojapanese.org/learn/grammar/volitional"}, "cyber": {"topic": "Attack Vectors", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            6: {"math": {"topic": "Stats: Z-Score", "link": "https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores/v/z-score-introduction"}, "jp": {"topic": "Transitive", "link": "http://www.guidetojapanese.org/learn/grammar/transitive"}, "cyber": {"topic": "Threat Actors", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Week 15 Review", "link": "https://www.khanacademy.org/math/trigonometry"}, "jp": {"topic": "Trig Graphs", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Wireshark", "link": "https://wiki.wireshark.org/SampleCaptures"}}
        }},
        16: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Log Intro", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/logarithms"}, "jp": {"topic": "Particle SHI", "link": "http://www.guidetojapanese.org/learn/grammar/particles2"}, "cyber": {"topic": "OWASP Top 10", "link": "https://owasp.org/www-project-top-ten/"}},
            2: {"math": {"topic": "Log Properties", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-prop/v/introduction-to-logarithm-properties"}, "jp": {"topic": "NAGARA", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "SQL Injection", "link": "https://portswigger.net/web-security/sql-injection"}},
            3: {"math": {"topic": "Expand/Condense", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-prop/v/using-properties-of-logarithms-example"}, "jp": {"topic": "NODE / KARA", "link": "http://www.guidetojapanese.org/learn/grammar/compound"}, "cyber": {"topic": "XSS Attacks", "link": "https://portswigger.net/web-security/cross-site-scripting"}},
            4: {"math": {"topic": "Natural Log", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/natural-logarithm-and-natural-exponential-function"}, "jp": {"topic": "~Kana (Wonder)", "link": "http://www.guidetojapanese.org/learn/grammar/sentence_ending"}, "cyber": {"topic": "CSRF Attacks", "link": "https://portswigger.net/web-security/csrf"}},
            5: {"math": {"topic": "Log Equations", "link": "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:exponential-models/v/solving-logarithmic-equations"}, "jp": {"topic": "Passive Voice", "link": "http://www.guidetojapanese.org/learn/grammar/passive"}, "cyber": {"topic": "Dir Traversal", "link": "https://portswigger.net/web-security/file-path-traversal"}},
            6: {"math": {"topic": "Stats: Normal Dist", "link": "https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/v/introduction-to-the-normal-distribution"}, "jp": {"topic": "Causative", "link": "http://www.guidetojapanese.org/learn/grammar/causative"}, "cyber": {"topic": "App Hardening", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Exam: Trig/Log", "link": "https://www.khanacademy.org/math/algebra2"}, "jp": {"topic": "Phase 4 Rev", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: PortSwigger", "link": "https://portswigger.net/web-security"}}
        }},
        17: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Binomial Thm", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polynomials/x9e81a4f98389efdf:binomial/v/binomial-theorem"}, "jp": {"topic": "Keigo Intro", "link": "http://www.guidetojapanese.org/learn/grammar/honorific"}, "cyber": {"topic": "Business Cont.", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            2: {"math": {"topic": "Arith Sequence", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:series/x9e81a4f98389efdf:seq-intro/v/explicit-and-recursive-definitions-of-sequences"}, "jp": {"topic": "Kenjougo", "link": "http://www.guidetojapanese.org/learn/grammar/honorific"}, "cyber": {"topic": "Disaster Rec", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            3: {"math": {"topic": "Geom Sequence", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:series/x9e81a4f98389efdf:seq-intro/v/geometric-sequences-introduction"}, "jp": {"topic": "Business JP", "link": "http://www.guidetojapanese.org/learn/grammar/honorific"}, "cyber": {"topic": "Incident Resp", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "Sigma Notation", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:series/x9e81a4f98389efdf:summation/v/sigma-notation-summation"}, "jp": {"topic": "Formal Phone", "link": "http://www.guidetojapanese.org/learn/grammar/honorific"}, "cyber": {"topic": "Forensics", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            5: {"math": {"topic": "Induction", "link": "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:series/x9e81a4f98389efdf:induction/v/proof-by-induction"}, "jp": {"topic": "Advice", "link": "http://www.guidetojapanese.org/learn/grammar/recommendation"}, "cyber": {"topic": "Chain of Cust", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            6: {"math": {"topic": "Stats: Sampling", "link": "https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library/sampling-distribution-mean/v/sampling-distribution-of-the-sample-mean"}, "jp": {"topic": "~Te shimau", "link": "http://www.guidetojapanese.org/learn/grammar/unintended"}, "cyber": {"topic": "GDPR", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Week 17 Review", "link": "https://www.khanacademy.org/math/precalculus"}, "jp": {"topic": "Keigo Audit", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: IR Plan", "link": "https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf"}}
        }},
        18: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Limits Concept", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-limit-intro/v/introduction-to-limits-hd"}, "jp": {"topic": "~Sou desu", "link": "http://www.guidetojapanese.org/learn/grammar/hearsay"}, "cyber": {"topic": "Cloud Types", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            2: {"math": {"topic": "Estimating Lim", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-estimating-limits-from-graphs/v/estimating-limit-from-graph"}, "jp": {"topic": "~Rashii", "link": "http://www.guidetojapanese.org/learn/grammar/hearsay"}, "cyber": {"topic": "VM Security", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            3: {"math": {"topic": "Substitution Lim", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-evaluating-limits-using-substitution/v/limits-by-substitution"}, "jp": {"topic": "~Deshou", "link": "http://www.guidetojapanese.org/learn/grammar/hearsay"}, "cyber": {"topic": "Mobile Sec", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "One-Sided Lim", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-one-sided-limits/v/one-sided-limits-graphs"}, "jp": {"topic": "~Tame ni", "link": "http://www.guidetojapanese.org/learn/grammar/cause"}, "cyber": {"topic": "IoT Security", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            5: {"math": {"topic": "Continuity", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-continuity-at-a-point/v/continuity-at-a-point"}, "jp": {"topic": "~Yasui/Nikui", "link": "http://www.guidetojapanese.org/learn/grammar/easy_hard"}, "cyber": {"topic": "Physical Ctrl", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            6: {"math": {"topic": "Stats: CLT", "link": "https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library/sampling-distribution-mean/v/central-limit-theorem"}, "jp": {"topic": "Podcasts", "link": "https://nihongoconteppei.com/"}, "cyber": {"topic": "Social Eng", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            7: {"math": {"topic": "Week 18 Review", "link": "https://www.khanacademy.org/math/calculus-1"}, "jp": {"topic": "Audit", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Exam: Practice Sec+", "link": "https://www.examcompass.com/comptia/security-plus-certification/free-security-plus-practice-tests"}}
        }},
        19: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Algebraic Lim", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-limits-algebraically/v/limits-by-factoring"}, "jp": {"topic": "News Reading", "link": "https://www3.nhk.or.jp/news/easy/"}, "cyber": {"topic": "HTML Basics", "link": "https://www.w3schools.com/html/"}},
            2: {"math": {"topic": "Conjugates", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-limits-algebraically/v/limits-by-rationalizing"}, "jp": {"topic": "Journaling", "link": "https://lang-8.com/"}, "cyber": {"topic": "Cookies", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            3: {"math": {"topic": "Infinite Limits", "link": "https://www.khanacademy.org/math/calculus-1/cs-limits-and-continuity/cs-infinite-limits/v/limits-at-infinity"}, "jp": {"topic": "Lang Exchange", "link": "https://www.hellotalk.com/"}, "cyber": {"topic": "HTTP Headers", "link": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers"}},
            4: {"math": {"topic": "Derivative Intro", "link": "https://www.khanacademy.org/math/calculus-1/cs-derivatives-definition-and-basic-rules/cs-derivative-intro/v/derivative-as-a-concept"}, "jp": {"topic": "Slang", "link": "http://www.guidetojapanese.org/learn/grammar/slang"}, "cyber": {"topic": "Burp Intro", "link": "https://portswigger.net/burp/documentation/desktop/getting-started"}},
            5: {"math": {"topic": "Limit Definition", "link": "https://www.khanacademy.org/math/calculus-1/cs-derivatives-definition-and-basic-rules/cs-derivative-intro/v/derivative-as-limit"}, "jp": {"topic": "Anime No Subs", "link": "https://animelon.com/"}, "cyber": {"topic": "Intercepting", "link": "https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic"}},
            6: {"math": {"topic": "Power Rule", "link": "https://www.khanacademy.org/math/calculus-1/cs-derivatives-definition-and-basic-rules/cs-power-rule/v/power-rule"}, "jp": {"topic": "Shadowing", "link": "https://www.tofugu.com/japanese/shadowing/"}, "cyber": {"topic": "Repeater", "link": "https://portswigger.net/burp/documentation/desktop/tools/repeater"}},
            7: {"math": {"topic": "Week 19 Review", "link": "https://www.khanacademy.org/math/calculus-1"}, "jp": {"topic": "Quiz", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Lab: Burp", "link": "https://portswigger.net/burp/communitydownload"}}
        }},
        20: {"phase": "Phase 2: Security+ & N5", "days": {
            1: {"math": {"topic": "Deriv Practice", "link": "https://www.khanacademy.org/math/calculus-1"}, "jp": {"topic": "N4 Review", "link": "http://www.guidetojapanese.org/"}, "cyber": {"topic": "Linux PrivEsc", "link": "https://tryhackme.com/room/linuxprivesc"}},
            2: {"math": {"topic": "Integrals Intro", "link": "https://www.khanacademy.org/math/calculus-1/cs-integration/cs-integration-intro/v/introduction-to-integral-calculus"}, "jp": {"topic": "Kanji Audit", "link": "https://kanji.garden/"}, "cyber": {"topic": "Win PrivEsc", "link": "https://tryhackme.com/room/windows10privesc"}},
            3: {"math": {"topic": "Fund Theorem", "link": "https://www.khanacademy.org/math/calculus-1/cs-integration/cs-fundamental-theorem-of-calculus/v/fundamental-theorem-of-calculus"}, "jp": {"topic": "Immersion", "link": "https://www.youtube.com/user/MATTvsJapan"}, "cyber": {"topic": "Reverse Shells", "link": "https://www.youtube.com/watch?v=1X_4Xy0_5_0"}},
            4: {"math": {"topic": "Final Exam", "link": "https://www.khanacademy.org/math/calculus-1"}, "jp": {"topic": "Monologue", "link": "https://vocaroo.com/"}, "cyber": {"topic": "Metasploit", "link": "https://www.metasploit.com/"}},
            5: {"math": {"topic": "Stats: Hypothesis", "link": "https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/idea-of-significance-tests/v/introduction-to-hypothesis-testing"}, "jp": {"topic": "N3 Planning", "link": "https://jlptsensei.com/"}, "cyber": {"topic": "Exploit DB", "link": "https://www.exploit-db.com/"}},
            6: {"math": {"topic": "Note Cleanup", "link": "https://www.notion.so/"}, "jp": {"topic": "Anki Goals", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "CTF", "link": "https://picoctf.org/"}},
            7: {"math": {"topic": "PHASE 2 DONE", "link": "https://www.khanacademy.org/"}, "jp": {"topic": "CELEBRATE", "link": "https://www.youtube.com/"}, "cyber": {"topic": "GRADUATION", "link": "https://tryhackme.com/"}}
        }}
    }

# --- SIDEBAR ---
with st.sidebar:
    st.title("📊 Mastery Tracker")
    st.markdown("---")
    
    # Calculate Stats
    full_data = get_curriculum()
    total_tasks = 20 * 7 * 3 
    completed_count = sum(st.session_state.progress.values())
    percent_complete = min((completed_count / total_tasks), 1.0)
    
    st.metric("Total Progress", f"{percent_complete:.1%}")
    st.progress(percent_complete)
    
    st.markdown("### Navigation")
    selected_week = st.selectbox("Select Current Week", list(range(1, 21)))
    
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
            link = day_data['math']['link']
            key = f"w{selected_week}_d{day_num}_math"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        # JAPANESE
        with col2:
            st.subheader("🇯🇵 Japanese")
            topic = day_data['jp']['topic']
            link = day_data['jp']['link']
            key = f"w{selected_week}_d{day_num}_jp"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        # CYBER
        with col3:
            st.subheader("🛡️ Cyber")
            topic = day_data['cyber']['topic']
            link = day_data['cyber']['link']
            key = f"w{selected_week}_d{day_num}_cyber"
            is_done = st.checkbox("Complete", key=key, value=st.session_state.progress.get(key, False))
            if is_done: st.session_state.progress[key] = True
            else: st.session_state.progress[key] = False
            st.markdown(f"**Topic:** {topic}")
            st.link_button("Go to Resource", link)

        st.markdown("---")
        
        # Success Message
        day_keys = [f"w{selected_week}_d{day_num}_{subj}" for subj in ["math", "jp", "cyber"]]
        if all(st.session_state.progress.get(k, False) for k in day_keys):
            st.markdown(f"<div class='success-box'>🎉 <b>Day {day_num} Complete!</b> Great work.</div>", unsafe_allow_html=True)
