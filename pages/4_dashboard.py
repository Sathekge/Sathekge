import streamlit as st

from charts.plots import (
    category_breakdown_chart,
    overall_gauge,
    pillar_bar_chart,
    radar_chart,
)
from config.scoring import CATEGORY_DISPLAY_NAMES, PILLAR_DISPLAY_NAMES
from data.questions import ALL_QUESTIONS
from export.pdf_report import generate_pdf
from recommendations.engine import generate_recommendations
from scoring.engine import compute_all, get_score_label

st.title("ESG Dashboard")

if "responses" not in st.session_state:
    st.session_state["responses"] = {}

responses = st.session_state["responses"]
answered = len(responses)
total = len(ALL_QUESTIONS)

if answered == 0:
    st.warning("No questions answered yet. Please complete the assessment sections first.")
    st.stop()

st.caption(f"{answered}/{total} questions answered ({answered/total*100:.0f}%)")

scores = compute_all(responses, ALL_QUESTIONS)

# Overall score gauge
st.plotly_chart(overall_gauge(scores["overall"]), use_container_width=True)

# Pillar scores
col1, col2, col3 = st.columns(3)
for col, key in zip([col1, col2, col3], ["environmental", "social", "governance"]):
    pillar = scores["pillars"][key]
    s = pillar["score"]
    label, color = get_score_label(s)
    with col:
        st.markdown(f"### {PILLAR_DISPLAY_NAMES[key]}")
        if s is not None:
            st.markdown(f"<h2 style='color:{color}'>{s:.1f}</h2>", unsafe_allow_html=True)
            st.caption(label)
        else:
            st.markdown("*No data*")

st.divider()

# Pillar bar chart
st.plotly_chart(pillar_bar_chart(scores["pillars"]), use_container_width=True)

# Radar chart
st.plotly_chart(radar_chart(scores), use_container_width=True)

# Category breakdowns
st.subheader("Category Breakdowns")
for pillar_key in ["environmental", "social", "governance"]:
    with st.expander(f"{PILLAR_DISPLAY_NAMES[pillar_key]} Categories"):
        cats = scores["pillars"][pillar_key]["categories"]
        if cats:
            st.plotly_chart(
                category_breakdown_chart(cats, pillar_key),
                use_container_width=True,
            )
            for cat, s in cats.items():
                label, color = get_score_label(s)
                st.markdown(
                    f"- **{CATEGORY_DISPLAY_NAMES.get(cat, cat)}**: "
                    f"<span style='color:{color}'>{s:.1f} — {label}</span>",
                    unsafe_allow_html=True,
                )
        else:
            st.info("No data for this pillar yet.")

# Recommendations
st.divider()
st.subheader("Recommendations")
recs = generate_recommendations(scores)

if not recs:
    st.success("Complete the assessment to receive tailored recommendations.")
else:
    high = [r for r in recs if r["priority"] == "High"]
    medium = [r for r in recs if r["priority"] == "Medium"]
    low = [r for r in recs if r["priority"] == "Low"]

    if high:
        st.markdown("#### High Priority")
        for r in high:
            st.error(f"**{CATEGORY_DISPLAY_NAMES.get(r['category'], r['category'])}**: {r['text']}")
    if medium:
        st.markdown("#### Medium Priority")
        for r in medium:
            st.warning(f"**{CATEGORY_DISPLAY_NAMES.get(r['category'], r['category'])}**: {r['text']}")
    if low:
        st.markdown("#### Low Priority")
        for r in low:
            st.success(f"**{CATEGORY_DISPLAY_NAMES.get(r['category'], r['category'])}**: {r['text']}")

# PDF Export
st.divider()
st.subheader("Export Report")

chart_figs = {
    "Overall ESG Score": overall_gauge(scores["overall"]),
    "Pillar Scores": pillar_bar_chart(scores["pillars"]),
    "ESG Category Radar": radar_chart(scores),
}

try:
    pdf_bytes = generate_pdf(scores, recs, chart_figs)
    st.download_button(
        label="Download PDF Report",
        data=pdf_bytes,
        file_name="esg_diagnostic_report.pdf",
        mime="application/pdf",
    )
except Exception as e:
    st.warning(f"PDF generation requires kaleido for chart images. Text-only PDF available.")
    pdf_bytes = generate_pdf(scores, recs, chart_figures=None)
    st.download_button(
        label="Download PDF Report (without charts)",
        data=pdf_bytes,
        file_name="esg_diagnostic_report.pdf",
        mime="application/pdf",
    )
