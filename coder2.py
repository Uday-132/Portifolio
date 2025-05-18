import streamlit as st
from streamlit_lottie import st_lottie
import requests
# from PIL import Image # If using local images

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Uday's Portfolio - Dynamic & Animated",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed", # Collapse sidebar for more focus on content
)

# --- ASSETS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder_url = "https://assets3.lottiefiles.com/packages/lf20_AMBEWz.json"
lottie_hello_url = "https://assets6.lottiefiles.com/packages/lf20_V9t630.json"
lottie_contact_url = "https://assets1.lottiefiles.com/packages/lf20_gaplvsns.json"

lottie_coder = load_lottieurl(lottie_coder_url)
lottie_hello = load_lottieurl(lottie_hello_url)
lottie_contact = load_lottieurl(lottie_contact_url)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    :root {
        --primary-color: #17A2B8; /* Vibrant Teal/Cyan */
        --secondary-color: #2c3e50; /* Dark Slate Blue */
        --accent-hover-color: #1DCAD7;
        --card-bg-color: #ffffff;
        --skill-item-bg: #f0f2f6;
        --skill-item-hover-bg: var(--primary-color);
        --skill-item-hover-text: #ffffff;
        --text-color: #333333;
        --light-text-color: #555555;
        --border-color: #dddddd;

        /* New Classy Colors for Header/Footer */
        --header-bg-color: #2c3e50; /* Using secondary for consistency */
        --header-text-color: #ecf0f1; /* Clouds - light grey */
        --header-nav-hover-color: var(--primary-color);

        --footer-bg-color: #232931; /* Very dark, almost black grey */
        --footer-text-color: #a9b0ba; /* Muted light grey for footer text */

        /* Colors for About Me animated text */
        --anim-text-color1: #17A2B8; /* Teal - Primary */
        --anim-text-color2: #50E3C2; /* Vibrant Turquoise/Mint */
        --anim-text-color3: #4A90E2; /* A nice Blue */
        --anim-text-color4: #3498DB; /* Peter River Blue */
    }

    /* Remove Streamlit's default header/footer padding when custom ones are used */
    .main .block-container {
        padding-top: 0rem; /* Reduce if using custom header */
        padding-bottom: 0rem; /* Reduce if using custom footer */
    }
    /* For the actual app header to have space from Streamlit's own top bar */
    div[data-testid="stVerticalBlock"] > div:first-child > div[data-testid="stVerticalBlock"] > div:first-child {
        margin-top: 0rem; /* Adjust this if needed */
    }


    body {
        font-family: 'Roboto', 'Segoe UI', sans-serif;
        color: var(--text-color);
        background-color: #f7f9fc; /* Slightly off-white background for content area */
    }

    /* --- CUSTOM HEADER --- */
    .app-header {
        background-color: var(--header-bg-color);
        color: var(--header-text-color);
        padding: 0.8rem 2rem; /* Slimmer header */
        width: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        /* position: sticky; top: 0; z-index: 999; */ /* Uncomment for sticky header if desired */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .app-header .header-name {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color); /* Name stands out */
        text-decoration: none;
    }
    .app-header .nav-links a {
        color: var(--header-text-color);
        text-decoration: none;
        margin-left: 25px;
        font-size: 1.05em;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    .app-header .nav-links a:hover, .app-header .nav-links a.active {
        color: var(--header-nav-hover-color);
        /* text-decoration: underline; */
    }


    /* Hero section styling - adjusted for header */
    .hero-section-container {
        padding-top: 3rem; /* Space below custom header */
        padding-bottom: 3rem;
    }
    .hero-text h1 {
        font-size: 3.8rem; font-weight: 700; color: var(--primary-color);
        animation: slideInFromLeft 1s ease-out; margin-bottom: 0.5rem;
    }
    .hero-text h2 {
        font-size: 1.8rem; font-weight: 500; color: var(--secondary-color);
        margin-bottom: 1rem; animation: fadeIn 1.5s ease-in;
    }
    .hero-text p {
        font-size: 1.1rem; line-height: 1.7; color: var(--light-text-color);
        animation: fadeIn 2s ease-in;
    }

    /* Section headers */
    .stSubheader { /* Streamlit's subheader class, can be used or a custom one */
        font-size: 2.2rem; font-weight: 600; color: var(--secondary-color);
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: 0.7rem; margin-top: 3rem; margin-bottom: 2rem;
        animation: fadeIn 1.5s ease-out;
    }
    /* Custom section class for better control if needed */
    .section-container {
        padding: 2rem 0; /* Vertical padding for sections */
    }


    /* --- ABOUT ME - ANIMATED & LARGE TEXT --- */
    #about-me-section .content-text {
        font-size: 1.4em; /* Larger text */
        line-height: 1.9;   /* Generous line height */
        font-weight: 400;
        margin-bottom: 1.5em;
    }
    #about-me-section .animated-gradient-text {
        background-image: linear-gradient(
            -225deg,
            var(--anim-text-color1) 0%,
            var(--anim-text-color2) 25%,
            var(--anim-text-color3) 50%,
            var(--anim-text-color4) 75%,
            var(--anim-text-color1) 100%
        );
        background-size: 200% auto;
        color: #000; /* Fallback */
        background-clip: text;
        -webkit-background-clip: text;
        text-fill-color: transparent;
        -webkit-text-fill-color: transparent;
        animation: textclip 5s linear infinite;
    }
    #about-me-section .animated-gradient-text strong {
        /* Ensure strong tags also get the gradient */
        background-image: inherit;
        background-size: inherit;
        background-clip: text;
        -webkit-background-clip: text;
        text-fill-color: transparent;
        -webkit-text-fill-color: transparent;
        font-weight: 700; /* Make sure strong is actually bold */
    }

    @keyframes textclip {
      to {
        background-position: 200% center;
      }
    }


    /* Project cards styling (minor adjustments if needed) */
    .project-card {
        border: 1px solid var(--border-color); border-radius: 12px; padding: 25px;
        margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: transform 0.35s ease-in-out, box-shadow 0.35s ease-in-out;
        background-color: var(--card-bg-color);
    }
    .project-card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 0 15px 30px rgba(44, 62, 80, 0.15);
    }
    .project-card h3 { color: var(--primary-color); margin-bottom: 12px; font-size: 1.5rem; }
    .project-card .tech-stack span {
        background-color: var(--skill-item-bg); color: var(--secondary-color);
        padding: 6px 12px; border-radius: 15px; margin-right: 6px; margin-bottom: 6px;
        font-size: 0.85em; font-weight: 500; display: inline-block;
    }

    /* Skills styling */
    .skill-item-wrapper { padding: 5px; }
    .skill-item {
        background-color: var(--skill-item-bg); color: var(--secondary-color);
        padding: 15px 22px; border-radius: 8px; margin: 0; text-align: center;
        font-weight: 500; font-size: 1em; box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        border: 1px solid #d0d0d0; min-height: 60px; display: flex; align-items: center; justify-content: center;
        transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1),
                    box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1),
                    background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
    }
    .skill-item:hover {
        transform: translateY(-12px) rotate(1.5deg) scale(1.08);
        box-shadow: 0 12px 24px rgba(var(--secondary-color), 0.2);
        background-color: var(--skill-item-hover-bg); color: var(--skill-item-hover-text);
        border-color: var(--accent-hover-color);
    }

    /* Contact form styling */
    .stButton>button {
        width: 100%; border-radius: 25px; background-color: var(--primary-color);
        color: white; padding: 12px 0; font-size: 1.15rem; font-weight: 500;
        border: none; transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover { background-color: var(--accent-hover-color); transform: scale(1.03); }
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px !important; border: 1px solid var(--border-color) !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 0.2rem rgba(23, 162, 184, 0.25) !important;
    }
    .social-icons a img {
        transition: transform 0.3s ease, filter 0.3s ease;
        filter: grayscale(50%) opacity(0.7);
    }
    .social-icons a:hover img { transform: scale(1.25) rotate(5deg); filter: grayscale(0%) opacity(1); }

    /* Keyframe animations */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes slideInFromLeft { from { transform: translateX(-80px); opacity: 0; } to { transform: translateX(0); opacity: 1); } }

    /* --- CUSTOM FOOTER --- */
    .app-footer {
        background-color: var(--footer-bg-color);
        color: var(--footer-text-color);
        padding: 2rem 2rem; /* More padding for footer */
        text-align: center;
        margin-top: 4rem; /* More space above footer */
        border-top: 1px solid #3a4149; /* Darker border for dark footer */
    }
    .app-footer p {
        margin: 0.3rem 0;
        font-size: 0.95em;
    }
    .app-footer a {
        color: var(--primary-color);
        text-decoration: none;
    }
    .app-footer a:hover {
        text-decoration: underline;
    }

</style>
""", unsafe_allow_html=True)


# --- CUSTOM HEADER ---
# Using st.markdown for HTML structure allows more control over layout with CSS
st.markdown(
    """
    <div class="app-header">
        <a href="#" class="header-name">Uday</a>
        <div class="nav-links">
            <a href="#about-me-section">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#experience">Experience</a>
            <a href="#contact-me">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- HERO SECTION ---
# Added a wrapper container for better top padding after custom header
with st.container():
    st.markdown("<div class='hero-section-container'>", unsafe_allow_html=True) # Wrapper for padding
    left_column, right_column = st.columns((2, 1.2))
    with left_column:
        st.markdown("<div class='hero-text'>", unsafe_allow_html=True)
        st.markdown(f"<h1>Hi, I'm Uday <span style='font-size: 3.5rem;'>👋</span></h1>", unsafe_allow_html=True)
        st.markdown("<h2>A Passionate Developer & Tech Innovator</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <p>
            I specialize in crafting elegant digital experiences and robust software solutions.
            From Python backends to interactive frontends, I love bringing ideas to life.
            Welcome to my creative space!
            </p>
            """, unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
        hero_btns_cols = st.columns((1,1,2))
        with hero_btns_cols[0]:
            st.link_button("View My Projects", "#projects", use_container_width=True)
        with hero_btns_cols[1]:
            st.link_button("Get In Touch", "#contact-me", type="secondary", use_container_width=True)
    with right_column:
        if lottie_coder:
            st_lottie(lottie_coder, height=450, quality="high", key="coder_animation_hero")
    st.markdown("</div>", unsafe_allow_html=True) # Close hero-section-container


# --- ABOUT ME ---
st.markdown("---") # Visual separator, can be removed if sections have enough space
with st.container(): # Use a section container for consistent padding
    st.markdown("<div id='about-me-section' class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='stSubheader'>About Me 🚀</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns((1.2, 0.8))
    with col1:
        st.markdown(
            """
            <div class="content-text animated-gradient-text">
            Hello! I'm <strong>Uday</strong>, a <strong>Full-Stack Software Engineer</strong> 
            based in <strong>[Your City, Country]</strong>. My journey into technology was sparked by 
            <strong>[briefly, your origin story, e.g., a fascination with how websites worked / a coding bootcamp / a university project]</strong>. 
            This initial curiosity has blossomed into a dedicated career focused on building 
            <strong>impactful and innovative software solutions</strong> that solve real-world problems.
            </div>
            <div class="content-text animated-gradient-text" style="animation-delay: 0.3s;">
            I thrive on the challenge of transforming <strong>complex requirements</strong> into 
            <strong>intuitive, user-friendly applications</strong>. I'm a lifelong learner, constantly exploring 
            new frameworks, architectural patterns, and best practices to stay at the forefront of the
            ever-evolving tech landscape. My core expertise lies in 
            <strong>Python development, API design, and cloud-native architectures</strong>.
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        # This part can remain standard text or also be animated if desired
        st.markdown(
            """
            <div style="padding-left: 1rem; margin-top: 1.5rem;">
            <h3 style="color: var(--secondary-color);">Core Values:</h3>
            <ul style="font-size: 1.1em; line-height: 1.8; list-style-position: outside; padding-left: 20px;">
                <li>💡 <strong>Innovation:</strong> Consistently seeking creative and efficient solutions.</li>
                <li>📈 <strong>Continuous Growth:</strong> Passionately embracing lifelong learning and skill development.</li>
                <li>🤝 <strong>Collaboration:</strong> Believing in the synergistic power of teamwork.</li>
                <li>🎯 <strong>User-Centricity:</strong> Designing and developing with the end-user experience as a priority.</li>
            </ul>
            <p style="font-size: 1.1em; line-height: 1.8; margin-top: 1.5em;">
            Outside the world of code, I find joy and inspiration in 
            <strong>[Your Hobbies, e.g., landscape photography, competitive chess, exploring culinary arts, hiking new trails]</strong>.
            </p>
            </div>
            """, unsafe_allow_html=True
        )
        if lottie_hello:
            st_lottie(lottie_hello, height=150, quality="medium", key="hello_animation_about")
    st.markdown("</div>", unsafe_allow_html=True) # Close about-me-section

# --- SKILLS ---
st.markdown("---")
with st.container():
    st.markdown("<div id='skills' class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='stSubheader'>My Technical Skills 🛠️</h2>", unsafe_allow_html=True)
    skills = {
        "Programming & Scripting": ["Python", "JavaScript (ES6+)", "Java", "Bash", "SQL"],
        "Web Technologies": ["HTML5", "CSS3", "React", "Node.js", "Streamlit", "Flask/Django"],
        "Databases & Storage": ["PostgreSQL", "MongoDB", "MySQL", "Redis", "AWS S3"],
        "Cloud & DevOps": ["AWS", "Docker", "Git & GitHub", "CI/CD", "Terraform"],
        "Data Science & ML": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Jupyter"],
    }
    num_skill_cols = 5
    for category, skill_list in skills.items():
        st.markdown(f"<h4 style='color: var(--secondary-color); margin-top:1.5rem; margin-bottom:0.8rem;'>{category}</h4>", unsafe_allow_html=True)
        cols = st.columns(num_skill_cols)
        for i, skill in enumerate(skill_list):
            with cols[i % num_skill_cols]:
                st.markdown(f"<div class='skill-item-wrapper'><div class='skill-item'>{skill}</div></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) # Close skills section


# --- PROJECTS ---
st.markdown("---")
with st.container():
    st.markdown("<div id='projects' class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='stSubheader'>Featured Projects 💡</h2>", unsafe_allow_html=True)
    projects_data = [
        {
            "title": "AI Recommendation Engine",
            "description": "Collaborative filtering system for e-commerce, improving user engagement by 15%. Python, Scikit-learn, Flask API.",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=500&q=60",
            "tech": ["Python", "Scikit-learn", "Flask", "Pandas", "API"],
            "link": "https://github.com/uday/recommendation-engine"
        },
        {
            "title": "Interactive Data Dashboard",
            "description": "Streamlit dashboard for real-time sensor data visualization with Plotly charts and user-configurable filters.",
            "image": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=500&q=60",
            "tech": ["Streamlit", "Plotly", "Python", "Pandas", "DataViz"],
            "link": "https://github.com/uday/streamlit-data-dashboard"
        },
        {
            "title": "Cloud-Native Task Scheduler",
            "description": "Serverless task scheduling using AWS Lambda, API Gateway, and DynamoDB for efficient cron-like job management.",
            "image": "https://images.unsplash.com/photo-1587620962725-abab7fe55159?auto=format&fit=crop&w=500&q=60",
            "tech": ["AWS Lambda", "API Gateway", "DynamoDB", "Serverless"],
            "link": "https://github.com/uday/cloud-task-scheduler"
        }
    ]
    num_project_columns = 3
    project_cols = st.columns(num_project_columns)
    for i, project in enumerate(projects_data):
        with project_cols[i % num_project_columns]:
            st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)
            if project.get("image"): st.image(project["image"], use_column_width=True)
            st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
            st.write(project['description'])
            tech_stack_html = "".join([f"<span>{tech}</span>" for tech in project['tech']])
            st.markdown(f"<div class='tech-stack' style='margin-top:10px; margin-bottom:15px;'>{tech_stack_html}</div>", unsafe_allow_html=True)
            if project.get("link"): st.link_button("View Project 🔗", project["link"], type="primary", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True) # Close projects section


# --- EXPERIENCE ---
st.markdown("---")
with st.container():
    st.markdown("<div id='experience' class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='stSubheader'>Professional Experience 💼</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: var(--primary-color);'>Senior Software Engineer | Innovatech Global</h4>", unsafe_allow_html=True)
    st.markdown("<em>Jan 2021 - Present | Remote</em>", unsafe_allow_html=True)
    st.markdown(
        """<ul style="list-style-type: disc; margin-left: 20px; font-size: 1.05em; line-height: 1.7;">
            <li>Lead development of [Project X], resulting in Y% performance improvement.</li>
            <li>Mentored junior engineers, fostering a collaborative team environment.</li>
            <li>Architected and implemented scalable microservices using [Tech Stack].</li>
        </ul>""", unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: var(--primary-color);'>Software Developer | NextGen Solutions</h4>", unsafe_allow_html=True)
    st.markdown("<em>Jun 2018 - Dec 2020 | City, State</em>", unsafe_allow_html=True)
    st.markdown(
        """<ul style="list-style-type: disc; margin-left: 20px; font-size: 1.05em; line-height: 1.7;">
            <li>Developed and maintained features for [Product Z] using [Tech Stack].</li>
            <li>Contributed to CI/CD pipeline automation, reducing deployment times.</li>
            <li>Collaborated in an Agile team to deliver bi-weekly software increments.</li>
        </ul>""", unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True) # Close experience section


# --- CONTACT ---
st.markdown("---")
with st.container():
    st.markdown("<div id='contact-me' class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='stSubheader'>Let's Connect 📬</h2>", unsafe_allow_html=True)
    contact_left, contact_right = st.columns((1.2, 0.8))
    with contact_left:
        st.markdown(
            """<p style="font-size: 1.1em;">
            I'm always excited to discuss new projects, collaborations, or interesting opportunities. 
            Feel free to reach out!
            </p>""", unsafe_allow_html=True
        )
        with st.form("contact_form"):
            name = st.text_input("Your Name", placeholder="e.g., Uday Kumar")
            email = st.text_input("Your Email", placeholder="uday@example.com")
            subject = st.text_input("Subject", placeholder="Project Idea / Collaboration")
            message = st.text_area("Your Message", placeholder="Hi Uday, I'd love to discuss...", height=150)
            submit_button = st.form_submit_button("Send Message")
            if submit_button:
                if name and email and subject and message:
                    st.success(f"Thanks, {name}! Message regarding '{subject}' 'sent'. (Demo)")
                else:
                    st.error("Please fill in all fields.")
        st.markdown("<h3 style='color: var(--secondary-color); margin-top: 2rem;'>Find me on:</h3>", unsafe_allow_html=True)
        st.markdown(
            """<div class="social-icons" style="font-size: 1.2rem; margin-top:0.5rem;">
                <a href="https://github.com/YOUR_USERNAME" target="_blank" title="GitHub"><img src="https://img.icons8.com/fluency-systems-filled/48/2c3e50/github.png" alt="GitHub" style="width:40px; height:40px; margin-right:15px;"/></a>
                <a href="https://linkedin.com/in/YOUR_USERNAME" target="_blank" title="LinkedIn"><img src="https://img.icons8.com/fluency-systems-filled/48/2c3e50/linkedin.png" alt="LinkedIn" style="width:40px; height:40px; margin-right:15px;"/></a>
                <a href="https://twitter.com/YOUR_USERNAME" target="_blank" title="Twitter/X"><img src="https://img.icons8.com/fluency-systems-filled/48/2c3e50/twitterx.png" alt="Twitter" style="width:40px; height:40px; margin-right:15px;"/></a>
                <a href="mailto:uday.your.email@example.com" title="Email"><img src="https://img.icons8.com/fluency-systems-filled/48/2c3e50/filled-message.png" alt="Email" style="width:40px; height:40px;"/></a>
            </div>""", unsafe_allow_html=True
        )
    with contact_right:
        if lottie_contact:
            st_lottie(lottie_contact, height=400, quality="high", key="contact_animation_form")
    st.markdown("</div>", unsafe_allow_html=True) # Close contact-me section


# --- CUSTOM FOOTER ---
st.markdown(
    """
    <div class="app-footer">
        <p>© 2024 Uday Kumar. All Rights Reserved.</p>
        <p>
            Crafted with <span style="color: var(--primary-color);">❤</span> using 
            <a href="https://streamlit.io" target="_blank">Streamlit</a>. 
            Inspired by creativity, driven by code.
        </p>
        <p>
            <a href="#about-me-section">About</a> | 
            <a href="#skills">Skills</a> | 
            <a href="#projects">Projects</a> |
            <a href="#contact-me">Contact</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)