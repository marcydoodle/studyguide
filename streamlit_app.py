# --- RESOURCE CONSTANTS (EASY TO UPDATE) ---
# Math
KHAN = "https://www.khanacademy.org/search?page_search_query="
TREFOR_DISCRETE = "https://www.youtube.com/playlist?list=PLDDGPdw7e6Ag1EIznZ-m-qXu4XX3A0cIz" # Best Discrete Math Playlist
MIT_LIN_ALG = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_lectures/" # Gilbert Strang (Gold Standard)
# Cyber & Python
PYTHON_DOCS = "https://docs.python.org/3/library/"
SCAPY_DOCS = "https://scapy.readthedocs.io/en/latest/usage.html"
SKLEARN = "https://scikit-learn.org/stable/user_guide.html"
ARXIV = "https://arxiv.org/list/cs.CR/recent" # New Research
# Japanese
TAE_KIM = "http://www.guidetojapanese.org/learn/grammar/"
JLPT_SENSEI = "https://jlptsensei.com/"
TOFUGU = "https://www.tofugu.com/japanese/"
# OIST
OIST_URL = "https://admissions.oist.jp/"

def get_curriculum():
    return {
        # --- PHASE 1 & 2 (Foundations) ---
        # (Keeping Week 1 & 11 as placeholders for the early stuff)
        1: {"phase": "Phase 1: Foundations", "days": {
            1: {"math": {"topic": "Order of Operations", "summary": "PEMDAS rules.", "link": f"{KHAN}Order+of+operations"}, "jp": {"topic": "Hiragana A-O", "summary": "First 5 vowels.", "link": f"{TOFUGU}learn-hiragana/"}, "cyber": {"topic": "Network: OSI Model", "summary": "Layers 1-7.", "link": "https://www.professormesser.com/"}},
            7: {"math": {"topic": "Week 1 Review", "summary": "Algebra basics.", "link": f"{KHAN}Algebra"}, "jp": {"topic": "Anki Setup", "summary": "Daily reps.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Lab: VirtualBox", "summary": "Setup Victim/Attacker VMs.", "link": "https://www.virtualbox.org/"}}
        }},
        11: {"phase": "Phase 2: Sec+ & Scripting", "days": {
            1: {"math": {"topic": "Functions Intro", "summary": "Inputs/Outputs.", "link": f"{KHAN}Functions"}, "jp": {"topic": "Te-Form (Ru)", "summary": "Conjugation.", "link": TAE_KIM}, "cyber": {"topic": "Python: Variables", "summary": "Data types.", "link": "https://www.w3schools.com/python/"}},
            7: {"math": {"topic": "Review", "summary": "Functions.", "link": f"{KHAN}Algebra2"}, "jp": {"topic": "Te-Form Drill", "summary": "Drill.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Milestone 1: Log Parser", "summary": "Read CSV logs with Python.", "link": f"{PYTHON_DOCS}csv.html"}}
        }},

        # --- PHASE 3: DISCRETE MATH & NET-SENTRY (Weeks 21-30) ---
        # FOCUS: Math of Logic/Networks + Building Traffic Sniffer
        21: {"phase": "Phase 3: Discrete Math & Net-Sentry", "days": {
            1: {"math": {"topic": "Logic: Truth Tables", "summary": "AND, OR, XOR basics.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Passive Voice", "summary": "Rareru form.", "link": f"{TAE_KIM}passive"}, 
                "cyber": {"topic": "Raw Sockets", "summary": "Python socket library.", "link": "https://realpython.com/python-sockets/"}},
            2: {"math": {"topic": "Logic: Implications", "summary": "If P then Q.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Passive Sentences", "summary": "Practice.", "link": f"{TAE_KIM}passive"}, 
                "cyber": {"topic": "Python: Try/Except", "summary": "Error Handling.", "link": "https://www.w3schools.com/python/python_try_except.asp"}},
            3: {"math": {"topic": "Set Theory", "summary": "Unions, Intersections.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Causative Voice", "summary": "Make/Let.", "link": f"{TAE_KIM}causative"}, 
                "cyber": {"topic": "Tool: Scapy Basics", "summary": "Packet manipulation.", "link": SCAPY_DOCS}},
            4: {"math": {"topic": "Venn Diagrams", "summary": "Visualizing sets.", "link": f"{KHAN}Venn+diagrams"}, 
                "jp": {"topic": "Causative Practice", "summary": "Drill.", "link": f"{TAE_KIM}causative"}, 
                "cyber": {"topic": "Lab: Local Sniffer", "summary": "Sniff localhost.", "link": "https://thepacketgeek.com/scapy/sniffing-custom-packets/"}},
            5: {"math": {"topic": "Boolean Algebra", "summary": "Simplifying circuits.", "link": f"{KHAN}Boolean+algebra"}, 
                "jp": {"topic": "Keigo: Intro", "summary": "Polite speech.", "link": f"{TAE_KIM}honorific"}, 
                "cyber": {"topic": "Lab: Filtering", "summary": "Filter TCP/80.", "link": SCAPY_DOCS}},
            6: {"math": {"topic": "Logic Gates", "summary": "Physical circuits.", "link": f"{KHAN}Logic+gates"}, 
                "jp": {"topic": "Keigo: Sonkeigo", "summary": "Respectful.", "link": f"{TAE_KIM}honorific"}, 
                "cyber": {"topic": "Project: Basic Sniffer", "summary": "Build CLI tool.", "link": "https://github.com/"}},
            7: {"math": {"topic": "Week 21 Review", "summary": "Logic & Sets.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Keigo Audit", "summary": "Review.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Journal", "summary": "Update Log.", "link": "https://github.com/"}}
        }},
        25: {"phase": "Phase 3: Discrete Math & Net-Sentry", "days": {
            1: {"math": {"topic": "Combinatorics", "summary": "Permutations.", "link": f"{KHAN}Permutations"}, 
                "jp": {"topic": "Transitive Verbs", "summary": "Action on object.", "link": f"{TAE_KIM}transitive"}, 
                "cyber": {"topic": "Attack Sim: Nmap", "summary": "Scan your VM.", "link": "https://nmap.org/book/man.html"}},
            2: {"math": {"topic": "Combinations", "summary": "Order implies set.", "link": f"{KHAN}Combinations"}, 
                "jp": {"topic": "Intransitive Verbs", "summary": "Action happens.", "link": f"{TAE_KIM}transitive"}, 
                "cyber": {"topic": "Lab: Capture Scan", "summary": "Record Nmap.", "link": SCAPY_DOCS}},
            3: {"math": {"topic": "Pigeonhole Principle", "summary": "Proof concept.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Trans/Intrans Pairs", "summary": "Drill.", "link": f"{TAE_KIM}transitive"}, 
                "cyber": {"topic": "Lab: Signatures", "summary": "Identify flags.", "link": SCAPY_DOCS}},
            4: {"math": {"topic": "Binomial Coeffs", "summary": "Pascal's Triangle.", "link": f"{KHAN}Binomial+coefficient"}, 
                "jp": {"topic": "Appearance (~Sou)", "summary": "Looks like...", "link": f"{TAE_KIM}similarity"}, 
                "cyber": {"topic": "Python: Detection", "summary": "Detect SYN pattern.", "link": SCAPY_DOCS}},
            5: {"math": {"topic": "Bayes' Theorem", "summary": "Conditional Prob.", "link": f"{KHAN}Bayes+theorem"}, 
                "jp": {"topic": "Hearsay (~Sou)", "summary": "I heard...", "link": f"{TAE_KIM}hearsay"}, 
                "cyber": {"topic": "Project: Scan Alert", "summary": "Print ALERT.", "link": "https://github.com/"}},
            6: {"math": {"topic": "Expected Value", "summary": "Weighted average.", "link": f"{KHAN}Expected+value"}, 
                "jp": {"topic": "Likeness (~You)", "summary": "Metaphor.", "link": f"{TAE_KIM}similarity"}, 
                "cyber": {"topic": "Paper: IDS", "summary": "Read IDS paper.", "link": ARXIV}},
            7: {"math": {"topic": "Exam: Midterm", "summary": "Discrete Math.", "link": TREFOR_DISCRETE}, 
                "jp": {"topic": "Monthly Review", "summary": "Audit.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Journal", "summary": "Update Log.", "link": "https://github.com/"}}
        }},
        30: {"phase": "Phase 3: Net-Sentry V1.0 Launch", "days": {
            1: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Causative Rev", "summary": "Review.", "link": TAE_KIM}, "cyber": {"topic": "Code: Refactor", "summary": "Clean code.", "link": "https://peps.python.org/pep-0008/"}},
            2: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Keigo Rev", "summary": "Review.", "link": TAE_KIM}, "cyber": {"topic": "Docs: README", "summary": "Write docs.", "link": "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes"}},
            3: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Business Phrases", "summary": "Vocab.", "link": JLPT_SENSEI}, "cyber": {"topic": "Test: Live Run", "summary": "Home network.", "link": "https://github.com/"}},
            4: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Phone Call", "summary": "Phrases.", "link": JLPT_SENSEI}, "cyber": {"topic": "Release: GitHub", "summary": "Push v1.0.", "link": "https://github.com/"}},
            5: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Advice Rev", "summary": "Review.", "link": TAE_KIM}, "cyber": {"topic": "Video: Demo", "summary": "Record demo.", "link": "https://obsproject.com/"}},
            6: {"math": {"topic": "Project Week", "summary": "Code focus.", "link": "https://github.com/"}, "jp": {"topic": "Regret Rev", "summary": "Review.", "link": TAE_KIM}, "cyber": {"topic": "Submit: Portfolio", "summary": "Add to CV.", "link": "https://linkedin.com/"}},
            7: {"math": {"topic": "MILESTONE", "summary": "Net-Sentry Live.", "link": "https://github.com/"}, "jp": {"topic": "Keigo Audit", "summary": "Final check.", "link": TAE_KIM}, "cyber": {"topic": "Celebration", "summary": "Phase 3 Done.", "link": "https://www.youtube.com/"}}
        }},

        # --- PHASE 4: LINEAR ALGEBRA & AI RESEARCH (Weeks 31-40) ---
        # FOCUS: Math of AI (Vectors/Matrices) + OIST Proposal + AI Tool
        31: {"phase": "Phase 4: Linear Algebra & AI Research", "days": {
            1: {"math": {"topic": "Vectors Intro", "summary": "Magnitude/Direction.", "link": f"{KHAN}Vectors"}, 
                "jp": {"topic": "Academic Vocab", "summary": "Research terms.", "link": JLPT_SENSEI}, 
                "cyber": {"topic": "Intro to AI Security", "summary": "Adversarial ML.", "link": "https://openai.com/research/attacking-machine-learning"}},
            2: {"math": {"topic": "Vector Ops", "summary": "Add/Scale.", "link": f"{KHAN}Vector+addition"}, 
                "jp": {"topic": "Formal Writing", "summary": "Thesis style.", "link": f"{TAE_KIM}formal"}, 
                "cyber": {"topic": "Concept: Supervised", "summary": "Labelled data.", "link": "https://developers.google.com/machine-learning/crash-course"}},
            3: {"math": {"topic": "Dot Product", "summary": "Similarity.", "link": f"{KHAN}Dot+product"}, 
                "jp": {"topic": "Reading Tech", "summary": "Qiita.", "link": "https://qiita.com/"}, 
                "cyber": {"topic": "Concept: Unsupervised", "summary": "Clustering.", "link": "https://developers.google.com/machine-learning/crash-course"}},
            4: {"math": {"topic": "Unit Vectors", "summary": "Normalization.", "link": f"{KHAN}Unit+vector"}, 
                "jp": {"topic": "Speaking Prep", "summary": "Self-intro.", "link": "https://vocaroo.com/"}, 
                "cyber": {"topic": "Lab: Scikit-Learn", "summary": "Install.", "link": SKLEARN}},
            5: {"math": {"topic": "Linear Combinations", "summary": "Spanning space.", "link": f"{KHAN}Linear+combinations"}, 
                "jp": {"topic": "Research Email", "summary": "Draft email.", "link": f"{TOFUGU}writing-emails-in-japanese/"}, 
                "cyber": {"topic": "Lab: Pandas", "summary": "Loading Data.", "link": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html"}},
            6: {"math": {"topic": "Basis Vectors", "summary": "Coordinates.", "link": f"{KHAN}Basis+vectors"}, 
                "jp": {"topic": "Listening", "summary": "Tech news.", "link": "https://www.youtube.com/user/NHKonline"}, 
                "cyber": {"topic": "Paper: ML in Cyber", "summary": "Read survey.", "link": ARXIV}},
            7: {"math": {"topic": "Week 31 Review", "summary": "Vectors.", "link": MIT_LIN_ALG}, 
                "jp": {"topic": "Review", "summary": "Audit.", "link": "https://apps.ankiweb.net/"}, 
                "cyber": {"topic": "Log: Journal", "summary": "Update Log.", "link": "https://github.com/"}}
        }},
        35: {"phase": "Phase 4: Linear Algebra & AI Research", "days": {
            1: {"math": {"topic": "Orthogonality", "summary": "Perpendicular.", "link": f"{KHAN}Orthogonal+vectors"}, 
                "jp": {"topic": "Particle SHI", "summary": "Listing reasons.", "link": f"{TAE_KIM}particles"}, 
                "cyber": {"topic": "OIST Prep: CV", "summary": "Polish CV.", "link": OIST_URL}},
            2: {"math": {"topic": "Orthogonal Sets", "summary": "Independence.", "link": MIT_LIN_ALG}, 
                "jp": {"topic": "NAGARA", "summary": "While doing...", "link": f"{TAE_KIM}concurrent"}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Draft Intro.", "link": OIST_URL}},
            3: {"math": {"topic": "Projections", "summary": "Shadows.", "link": f"{KHAN}Projections+linear+algebra"}, 
                "jp": {"topic": "NODE/KARA", "summary": "Reasons.", "link": f"{TAE_KIM}compound"}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Draft Research.", "link": OIST_URL}},
            4: {"math": {"topic": "Gram-Schmidt", "summary": "Orthonormalizing.", "link": f"{KHAN}Gram+schmidt"}, 
                "jp": {"topic": "~Kana", "summary": "Wondering.", "link": JLPT_SENSEI}, 
                "cyber": {"topic": "OIST Prep: SOP", "summary": "Academic History.", "link": OIST_URL}},
            5: {"math": {"topic": "Least Squares", "summary": "Regression.", "link": f"{KHAN}Least+squares"}, 
                "jp": {"topic": "Passive Rev", "summary": "Review.", "link": TAE_KIM}, 
                "cyber": {"topic": "Output: SOP Draft", "summary": "Complete draft.", "link": OIST_URL}},
            6: {"math": {"topic": "Least Squares II", "summary": "Apps.", "link": MIT_LIN_ALG}, 
                "jp": {"topic": "Causative Rev", "summary": "Review.", "link": TAE_KIM}, 
                "cyber": {"topic": "Deadlines", "summary": "Check Internship.", "link": OIST_URL}},
            7: {"math": {"topic": "Week 35 Review", "summary": "Orthogonality.", "link": MIT_LIN_ALG}, 
                "jp": {"topic": "Output Check", "summary": "Review SOP.", "link": OIST_URL}, 
                "cyber": {"topic": "Log: Journal", "summary": "Update Log.", "link": "https://github.com/"}}
        }},
        40: {"phase": "Phase 4: Graduation & Application", "days": {
            1: {"math": {"topic": "PCA Intro", "summary": "Dim Reduction.", "link": "https://setosa.io/ev/principal-component-analysis/"}, "jp": {"topic": "Final Audit", "summary": "N3 Check.", "link": JLPT_SENSEI}, "cyber": {"topic": "Portfolio: Polish", "summary": "Finalize GitHub.", "link": "https://github.com/"}},
            2: {"math": {"topic": "SVD Intro", "summary": "Singular Value.", "link": MIT_LIN_ALG}, "jp": {"topic": "Interview Prep", "summary": "Why OIST?", "link": "https://vocaroo.com/"}, "cyber": {"topic": "Master's Syllabus", "summary": "Review.", "link": "https://ccsu.edu/"}},
            3: {"math": {"topic": "Linear Alg Final", "summary": "Review.", "link": MIT_LIN_ALG}, "jp": {"topic": "Resume JP", "summary": "Translate CV.", "link": f"{TOFUGU}resume/"}, "cyber": {"topic": "Submit: Internship", "summary": "Apply.", "link": OIST_URL}},
            4: {"math": {"topic": "Tensors Preview", "summary": "Deep Learning.", "link": "https://www.tensorflow.org/guide/tensor"}, "jp": {"topic": "Celebration", "summary": "Sushi.", "link": "https://www.youtube.com/"}, "cyber": {"topic": "Email Professors", "summary": "Cold emails.", "link": "https://nii.ac.jp/"}},
            5: {"math": {"topic": "Master's Prep", "summary": "Textbooks.", "link": "https://amazon.com/"}, "jp": {"topic": "Anki Clean", "summary": "Archive.", "link": "https://apps.ankiweb.net/"}, "cyber": {"topic": "Capstone: Release", "summary": "Public repo.", "link": "https://github.com/"}},
            6: {"math": {"topic": "Rest", "summary": "Recover.", "link": "https://headspace.com/"}, "jp": {"topic": "Rest", "summary": "Recover.", "link": "https://headspace.com/"}, "cyber": {"topic": "Rest", "summary": "Recover.", "link": "https://headspace.com/"}},
            7: {"math": {"topic": "GRADUATION", "summary": "Ready.", "link": MIT_LIN_ALG}, "jp": {"topic": "NEXT PHASE", "summary": "Road to OIST.", "link": OIST_URL}, "cyber": {"topic": "MISSION START", "summary": "Begin Cyber MS.", "link": OIST_URL}}
        }}
    }
