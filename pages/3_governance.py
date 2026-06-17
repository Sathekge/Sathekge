import streamlit as st

from config.scoring import CATEGORY_DISPLAY_NAMES
from data.questions import GOVERNANCE_QUESTIONS

st.title("Governance Assessment")
st.markdown("Evaluate your organization's governance practices across five key categories.")

if "responses" not in st.session_state:
    st.session_state["responses"] = {}

categories_seen = []
for q in GOVERNANCE_QUESTIONS:
    cat = q["category"]
    if cat not in categories_seen:
        categories_seen.append(cat)
        st.subheader(CATEGORY_DISPLAY_NAMES.get(cat, cat))

    options = q["options"]
    labels = [o["label"] for o in options]
    current = st.session_state["responses"].get(q["id"])
    current_idx = None
    if current is not None:
        for i, o in enumerate(options):
            if o["value"] == current:
                current_idx = i
                break

    selection = st.radio(
        q["text"],
        labels,
        index=current_idx,
        key=f"radio_{q['id']}",
    )

    if selection is not None:
        val = next(o["value"] for o in options if o["label"] == selection)
        st.session_state["responses"][q["id"]] = val

answered = sum(1 for q in GOVERNANCE_QUESTIONS if q["id"] in st.session_state["responses"])
total = len(GOVERNANCE_QUESTIONS)
st.progress(answered / total)
st.caption(f"{answered}/{total} questions answered")
