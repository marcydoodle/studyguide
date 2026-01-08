import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import io

# --- 1. EMBEDDED SCHEDULE DATA (No Upload Needed) ---
# I have embedded the body of your schedule here. 
# This allows the app to run standalone.
RAW_HTML_DATA = """
<body>
<p>Phase 1: Foundations & Networking</p>
<table>
  <tr><td>Week</td><td>Day</td><td>Math</td><td>Japanese</td><td>Cybersecurity</td><td>Links</td></tr>
  <tr><td>1</td><td>1</td><td>Order of Operations</td><td>Hiragana A-O</td><td>Intro to Networking</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:intro-variables/v/order-of-operations">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=9WkCgEyxk70">Cyber</a></td></tr>
  <tr><td>1</td><td>2</td><td>Combining Like Terms</td><td>Hiragana KA-KO</td><td>The OSI Model</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:combining-like-terms/v/combining-like-terms">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=Ilk71j9kSgs">Cyber</a></td></tr>
  <tr><td>1</td><td>3</td><td>1-Step Equations</td><td>Hiragana SA-SO</td><td>TCP/IP Model</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/why-we-do-the-same-thing-to-both-sides-of-equation">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.freecodecamp.org/news/osi-model-networking-layers/">Cyber</a></td></tr>
  <tr><td>1</td><td>4</td><td>2-Step Equations</td><td>Hiragana TA-TO</td><td>Binary & Hex</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/two-step-equations">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=LpuPe81bc2w">Cyber</a></td></tr>
  <tr><td>1</td><td>5</td><td>Multi-Step Equations</td><td>Hiragana NA-NO</td><td>IP Addressing (IPv4)</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/multi-step-equations-1">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=vcAr9OSHJYA">Cyber</a></td></tr>
  <tr><td>1</td><td>6</td><td>Mean, Median, Mode</td><td>Writing Practice</td><td>Classful Subnetting</td><td><a href="https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode">Stats</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=ecC3qvIz9fQ">Cyber</a></td></tr>
  <tr><td>1</td><td>7</td><td>Week 1 Review</td><td>Anki Setup</td><td>Lab: Install VirtualBox</td><td><a href="https://apps.ankiweb.net/">Anki</a> / <a href="https://www.virtualbox.org/wiki/Downloads">Cyber Lab</a></td></tr>
  <tr><td>2</td><td>8</td><td>Slope Formula</td><td>Hiragana HA-HO</td><td>IPv6 Basics</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope/v/slope-of-a-line">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=NHqd9319Ff0">Cyber</a></td></tr>
  <tr><td>2</td><td>9</td><td>Slope-Intercept Form</td><td>Hiragana MA-MO</td><td>DNS (Domain Name Sys)</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope-intercept-form/v/slope-intercept-form">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=27r4B6kcSC4">Cyber</a></td></tr>
  <tr><td>2</td><td>10</td><td>Graphing Lines</td><td>Hiragana YA-YO</td><td>DHCP (Dynamic Host)</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope-intercept-form/v/graphing-lines-in-slope-intercept-form">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=S43jtK9U5I8">Cyber</a></td></tr>
  <tr><td>2</td><td>11</td><td>Point-Slope Form</td><td>Hiragana RA-RO</td><td>Routers & Switches</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:point-slope-form/v/point-slope-and-standard-form">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=1z0ULvg_pW8">Cyber</a></td></tr>
  <tr><td>2</td><td>12</td><td>Standard Form</td><td>Hiragana WA-N</td><td>VLANs Basics</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:standard-form/v/standard-form-linear-equations">Math</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=Mofp_3D8vX8">Cyber</a></td></tr>
  <tr><td>2</td><td>13</td><td>Range & IQR</td><td>Dakuten (ga, za)</td><td>Port Numbers 1-1024</td><td><a href="https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/interquartile-range-iqr/v/range-variance-and-standard-deviation-as-measures-of-dispersion">Stats</a> / <a href="https://www.tofugu.com/japanese/learn-hiragana/">JP</a> / <a href="https://www.youtube.com/watch?v=r_z8F54Z27g">Cyber</a></td></tr>
  <tr><td>2</td><td>14</td><td>Week 2 Review</td><td>Hiragana Test</td><td>Flashcards: Ports</td><td><a href="https://kana-quiz.tofugu.com/">JP Test</a> / <a href="https://quizlet.com/539304724/common-ports-port-numbers-flash-cards/">Cyber Quiz</a></td></tr>
  <tr><td>3</td><td>15</td><td>Systems of Eq Intro</td><td>Katakana A-NO</td><td>TCP vs UDP</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:introduction-to-systems-of-equations/v/systems-of-equations">Math</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=Vdc8TCamQMw">Cyber</a></td></tr>
  <tr><td>3</td><td>16</td><td>Substitution Method</td><td>Katakana HA-HO</td><td>Wireless Standards</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-substitution/v/solving-systems-by-substitution-1">Math</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=680o2u1sFjI">Cyber</a></td></tr>
  <tr><td>3</td><td>17</td><td>Elimination Method</td><td>Katakana MA-YO</td><td>2.4GHz vs 5GHz</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-elimination/v/solving-systems-by-elimination">Math</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=2b12R8Vn1YI">Cyber</a></td></tr>
  <tr><td>3</td><td>18</td><td>Systems Word Probs</td><td>Katakana RA-N</td><td>Network Topologies</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:systems-of-equations-word-problems/v/systems-of-equations-word-problems">Math</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=Zb7W19o335Y">Cyber</a></td></tr>
  <tr><td>3</td><td>19</td><td>Systems Review</td><td>Long Vowels</td><td>Cable Types</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations">Math</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=N4e74B7Y_8c">Cyber</a></td></tr>
  <tr><td>3</td><td>20</td><td>Box & Whisker Plots</td><td>Loanwords</td><td>Command Line Basics</td><td><a href="https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/v/box-and-whisker-plot">Stats</a> / <a href="https://www.tofugu.com/japanese/learn-katakana/">JP</a> / <a href="https://www.youtube.com/watch?v=p4JgXqyH8vU">Cyber</a></td></tr>
  <tr><td>3</td><td>21</td><td>Week 3 Review</td><td>Core 2k Deck</td><td>Lab: Ping Google</td><td><a href="https://ankiweb.net/shared/info/2141233552">JP Anki</a> / <a href="https://www.freecodecamp.org/news/how-to-use-the-ping-command/">Cyber Lab</a></td></tr>
  <tr><td>4</td><td>22</td><td>Inequalities</td><td>Desu / Da</td><td>Cloud Concepts</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:inequalities-intro/v/inequalities">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/stateofbeing">JP</a> / <a href="https://www.youtube.com/watch?v=1KPrb82e9bw">Cyber</a></td></tr>
  <tr><td>4</td><td>23</td><td>Solving Inequalities</td><td>Negatives (Janai)</td><td>Virtualization</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:solving-inequalities/v/solving-inequalities">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/stateofbeing">JP</a> / <a href="https://www.youtube.com/watch?v=G86V3e8K5qA">Cyber</a></td></tr>
  <tr><td>4</td><td>24</td><td>Graphing Inequalities</td><td>Past Tense (Datta)</td><td>Network Troubleshooting</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:graphing-two-variable-inequalities/v/graphing-inequalities">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/stateofbeing">JP</a> / <a href="https://www.youtube.com/watch?v=lUp4SSsVdJY">Cyber</a></td></tr>
  <tr><td>4</td><td>25</td><td>Systems of Ineq</td><td>Past Neg (Janakatta)</td><td>SOHO Routers</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:systems-two-variable-inequalities/v/graphing-systems-of-inequalities-2">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/stateofbeing">JP</a> / <a href="https://www.youtube.com/watch?v=tT8O9f4u6g4">Cyber</a></td></tr>
  <tr><td>4</td><td>26</td><td>Modeling with Ineq</td><td>Question Particle</td><td>Security Concepts</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs/x2f8bb11595b61c86:modeling-with-linear-inequalities/v/modeling-with-linear-inequalities">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/stateofbeing">JP</a> / <a href="https://www.youtube.com/watch?v=r2dC2iKte68">Cyber</a></td></tr>
  <tr><td>4</td><td>27</td><td>Standard Deviation</td><td>Particles WA/GA</td><td>Malware Types</td><td><a href="https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/v/variance-of-a-population">Stats</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://www.youtube.com/watch?v=n8C8vJ7F5gM">Cyber</a></td></tr>
  <tr><td>4</td><td>28</td><td>Phase 1 Math Exam</td><td>Grammar Audit</td><td>Exam: Practice Net+</td><td><a href="https://www.khanacademy.org/math/algebra">Math Exam</a> / <a href="https://kana-quiz.tofugu.com/">JP Exam</a> / <a href="https://www.examcompass.com/comptia/network-plus-certification/free-network-plus-practice-tests">Cyber Exam</a></td></tr>
  <tr><td>5</td><td>29</td><td>Function Mapping</td><td>Particle MO</td><td>Linux: Intro & Kernel</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/what-is-a-function">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://linuxjourney.com/lesson/kernel-overview">Cyber</a></td></tr>
  <tr><td>5</td><td>30</td><td>Domain & Range</td><td>Particle NO</td><td>Linux: The Shell</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:domain-range/v/domain-and-range-from-graphs">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://linuxjourney.com/lesson/the-shell">Cyber</a></td></tr>
  <tr><td>5</td><td>31</td><td>Function Notation</td><td>Particle O</td><td>Linux: ls, cd, pwd</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:evaluating-functions/v/function-notation">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://linuxjourney.com/lesson/navigate-files">Cyber</a></td></tr>
  <tr><td>5</td><td>32</td><td>Vert. Line Test</td><td>Particle NI/E</td><td>Linux: touch, mkdir</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:vertical-line-test/v/vertical-line-test">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://linuxjourney.com/lesson/creating-files">Cyber</a></td></tr>
  <tr><td>5</td><td>33</td><td>Linear vs Nonlinear</td><td>Particle DE</td><td>Linux: cp, mv, rm</td><td><a href="https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:recognizing-functions-2/v/linear-nonlinear-functions">Math</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://linuxjourney.com/lesson/copy-move-files">Cyber</a></td></tr>
  <tr><td>5</td><td>34</td><td>Histograms</td><td>All Particles</td><td>Lab: Ubuntu VM Setup</td><td><a href="https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/histograms-intro">Stats</a> / <a href="http://www.guidetojapanese.org/learn/grammar/particlesintro">JP</a> / <a href="https://ubuntu.com/tutorials/install-ubuntu-desktop-on-virtualbox#1-overview">Cyber</a></td></tr>
  <tr><td>5</td><td>35</td><td>Week 5 Review</td><td>Anki Review</td><td>Command Line Challenge</td><td><a href="https://apps.ankiweb.net/">JP Anki</a> / <a href="https://overthewire.org/wargames/bandit/bandit0.html">Cyber</a></td></tr>
</table>
</body>
"""

# --- 2. PARSING ENGINE ---
@st.cache_data
def parse_html_data(html_string):
    """
    Parses the embedded HTML string into a structured DataFrame.
    """
    soup = BeautifulSoup(html_string, 'html.parser')
    rows = soup.find_all('tr')
    
    data = []
    
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
            
        # Get clean text
        get_text = lambda x: x.get_text(" ", strip=True)
        
        # Check column count to determine phase structure
        # Phase 1-2 usually has 6 columns (Link column separate)
        # Phase 3-4 usually has 5 columns (Links embedded)
        
        week = get_text(cells[0])
        day_str = get_text(cells[1])
        
        if not day_str.isdigit():
            continue
            
        day = int(day_str)
        
        math_topic, math_link = "", ""
        jp_topic, jp_link = "", ""
        cyber_topic, cyber_link = "", ""
        
        if len(cells) >= 6:
            # Structure: Week | Day | Math | JP | Cyber | Links
            math_topic = get_text(cells[2])
            jp_topic = get_text(cells[3])
            cyber_topic = get_text(cells[4])
            
            # Extract links from the 6th column
            link_cell = cells[5]
            links = link_cell.find_all('a')
            
            # Heuristic: 1st link -> Math, 2nd -> JP, 3rd -> Cyber
            if len(links) >= 1: math_link = links[0].get('href', '')
            if len(links) >= 2: jp_link = links[1].get('href', '')
            if len(links) >= 3: cyber_link = links[2].get('href', '')
            
        elif len(cells) == 5:
            # Structure: Week | Day | Math(Link) | JP(Link) | Cyber(Link)
            def extract_cell(cell):
                text = get_text(cell)
                link_tag = cell.find('a')
                link = link_tag.get('href', '') if link_tag else ""
                return text, link
            
            math_topic, math_link = extract_cell(cells[2])
            jp_topic, jp_link = extract_cell(cells[3])
            cyber_topic, cyber_link = extract_cell(cells[4])

        # Clean Google Redirects
        clean = lambda u: u.split("google.com/url?q=")[1].split("&")[0] if "google.com/url?q=" in u else u
        
        data.append({
            "Week": week,
            "Day": day,
            "Math Topic": math_topic,
            "Math Link": clean(math_link),
            "Japanese Topic": jp_topic,
            "JP Link": clean(jp_link),
            "Cyber Topic": cyber_topic,
            "Cyber Link": clean(cyber_link)
        })
        
    return pd.DataFrame(data)

# --- 3. STREAMLIT APP UI ---

st.set_page_config(page_title="Master Study Schedule", layout="wide")

st.title("📅 Master Study Dashboard")
st.markdown("""
**Progress Tracker:** Math (Algebra/Stats/Calc), Japanese (N5-N3), and Cybersecurity (Network+/Security+).
""")

# Load Data
df = parse_html_data(RAW_HTML_DATA)

# Filters
st.sidebar.header("Filters")
phase_filter = st.sidebar.radio("Select Phase:", 
    ["All", "Phase 1: Foundations (Days 1-70)", "Phase 2: Security+ (Days 71-140)", "Phase 3: Discrete Math (Days 141-210)", "Phase 4: Linear Algebra (Days 211+)"])

filtered_df = df.copy()

if "Phase 1" in phase_filter:
    filtered_df = df[df['Day'] <= 70]
elif "Phase 2" in phase_filter:
    filtered_df = df[(df['Day'] > 70) & (df['Day'] <= 140)]
elif "Phase 3" in phase_filter:
    filtered_df = df[(df['Day'] > 140) & (df['Day'] <= 210)]
elif "Phase 4" in phase_filter:
    filtered_df = df[df['Day'] > 210]

# Search
search_q = st.sidebar.text_input("🔍 Search Topics")
if search_q:
    filtered_df = filtered_df[
        filtered_df['Math Topic'].str.contains(search_q, case=False) |
        filtered_df['Japanese Topic'].str.contains(search_q, case=False) |
        filtered_df['Cyber Topic'].str.contains(search_q, case=False)
    ]

# Display Helper
def make_link(text, url):
    if url and text:
        return f"[{text}]({url})"
    return text

display_df = filtered_df.copy()
display_df['Math'] = display_df.apply(lambda x: make_link(x['Math Topic'], x['Math Link']), axis=1)
display_df['Japanese'] = display_df.apply(lambda x: make_link(x['Japanese Topic'], x['JP Link']), axis=1)
display_df['Cybersecurity'] = display_df.apply(lambda x: make_link(x['Cyber Topic'], x['Cyber Link']), axis=1)

final_view = display_df[['Week', 'Day', 'Math', 'Japanese', 'Cybersecurity']]

st.markdown(f"### Showing {len(final_view)} Days")
st.markdown(final_view.to_markdown(index=False), unsafe_allow_html=True)

# Metrics
st.sidebar.markdown("---")
progress = min(1.0, len(filtered_df) / 280)
st.sidebar.progress(progress)
st.sidebar.write(f"Total Days Loaded: **{len(df)}**")
