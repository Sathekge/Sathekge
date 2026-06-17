import streamlit as st

from data.questions import ALL_QUESTIONS, ENVIRONMENTAL_QUESTIONS, GOVERNANCE_QUESTIONS, SOCIAL_QUESTIONS

st.set_page_config(
    page_title="ESG Diagnostic Tool",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "responses" not in st.session_state:
    st.session_state["responses"] = {}


def _completion_pct(questions):
    answered = sum(1 for q in questions if q["id"] in st.session_state["responses"])
    return (answered / len(questions) * 100) if questions else 0


# Sidebar progress
with st.sidebar:
    st.title("Progress")
    env_pct = _completion_pct(ENVIRONMENTAL_QUESTIONS)
    soc_pct = _completion_pct(SOCIAL_QUESTIONS)
    gov_pct = _completion_pct(GOVERNANCE_QUESTIONS)
    overall_pct = _completion_pct(ALL_QUESTIONS)

    st.metric("Overall", f"{overall_pct:.0f}%")
    st.progress(overall_pct / 100)

    st.caption("Environmental")
    st.progress(env_pct / 100)
    st.caption("Social")
    st.progress(soc_pct / 100)
    st.caption("Governance")
    st.progress(gov_pct / 100)

    st.divider()
    if st.button("Reset All Responses"):
        st.session_state["responses"] = {}
        st.rerun()

# Main landing page
st.title("ESG Diagnostic Tool")
st.markdown("""
Welcome to the **ESG Automated Diagnostic Tool**. This tool assesses your organization's
performance across three pillars:

- **Environmental** — Carbon emissions, energy, waste, water, and environmental policy
- **Social** — Labor practices, diversity, community, health & safety, and human rights
- **Governance** — Board composition, ethics, transparency, risk management, and shareholder rights

### How to use

1. Navigate to each pillar page using the sidebar
2. Answer the diagnostic questions for each category
3. Visit the **Dashboard** to view your scores, charts, and recommendations
4. Download a **PDF report** summarizing your ESG performance

Use the sidebar to track your progress across all sections.
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"**Environmental**\n\n{env_pct:.0f}% complete")
with col2:
    st.info(f"**Social**\n\n{soc_pct:.0f}% complete")
with col3:
    st.info(f"**Governance**\n\n{gov_pct:.0f}% complete")
