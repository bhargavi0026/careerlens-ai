
import re
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CareerLens AI",
    page_icon="🎯",
    layout="wide"
)

KNOWN_SKILLS = [
    "Python", "SQL", "Pandas", "Excel", "Power BI",
    "Machine Learning", "Scikit-learn", "Statistics",
    "Tableau", "Git"
]


def extract_skills(text):
    found = []

    for skill in KNOWN_SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found


def analyze_skills(required_skills, candidate_skills):
    required = {s.lower() for s in required_skills}
    candidate_lookup = {s.lower(): s for s in KNOWN_SKILLS
                        if s.lower() in {x.lower() for x in candidate_skills}}

    candidate = set(candidate_lookup.keys())
    matched = required & candidate
    missing = required - candidate
    score = round(len(matched) / len(required) * 100, 2) if required else 0

    display_names = {s.lower(): s for s in KNOWN_SKILLS}

    return (
        score,
        sorted(display_names[s] for s in matched),
        sorted(display_names[s] for s in missing)
    )


st.title("🎯 CareerLens AI")
st.subheader("Job & Skill Gap Analyzer")
st.write(
    "Compare your current skills with a job description "
    "and identify skills you may need to learn."
)

st.info(
    "This is a rule-based prototype. Its match score measures "
    "overlap with the skills recognized by this app; it does not "
    "predict hiring outcomes."
)

job_description = st.text_area(
    "Paste the internship job description",
    height=180,
    placeholder="Example: We need an intern with Python, SQL, Pandas and Statistics."
)

candidate_input = st.text_input(
    "Enter your skills, separated by commas",
    placeholder="Python, SQL, Git"
)

if st.button("Analyze My Skills", type="primary"):
    if not job_description.strip() or not candidate_input.strip():
        st.warning("Please enter both the job description and your skills.")
    else:
        required = extract_skills(job_description)
        candidate = [
            item.strip()
            for item in candidate_input.split(",")
            if item.strip()
        ]

        if not required:
            st.warning(
                "No recognized skills found. Try including skills such as "
                "Python, SQL, Pandas or Excel."
            )
        else:
            score, matched, missing = analyze_skills(required, candidate)

            st.divider()
            st.header("Your Results")

            col1, col2, col3 = st.columns(3)
            col1.metric("Skill Match", f"{score}%")
            col2.metric("Matched Skills", len(matched))
            col3.metric("Skills to Learn", len(missing))

            st.subheader("Skills Found in the Job Description")
            st.write(", ".join(required))

            st.subheader("Your Matched Skills")
            if matched:
                st.success(", ".join(matched))
            else:
                st.write("No matching skills found.")

            st.subheader("Missing Skills")
            if missing:
                st.warning(", ".join(missing))
            else:
                st.success("You have all recognized required skills!")

            result_df = pd.DataFrame({
                "Skill": matched + missing,
                "Status": ["Matched"] * len(matched)
                          + ["Missing"] * len(missing)
            })

            st.subheader("Skill Gap Summary")
            st.dataframe(result_df, use_container_width=True, hide_index=True)

            st.caption(
                "Limitations: only the predefined skill list is recognized. "
                "The score gives equal weight to every detected skill."
            )
