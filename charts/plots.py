import plotly.graph_objects as go

from config.scoring import CATEGORY_DISPLAY_NAMES, PILLAR_DISPLAY_NAMES, SCORE_LABELS


def _score_color(score):
    if score is None:
        return "#95a5a6"
    for threshold, _, color in SCORE_LABELS:
        if score <= threshold:
            return color
    return "#27ae60"


def overall_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score if score is not None else 0,
        title={"text": "Overall ESG Score", "font": {"size": 24}},
        number={"suffix": "/100", "font": {"size": 36}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar": {"color": _score_color(score)},
            "steps": [
                {"range": [0, 40], "color": "#fadbd8"},
                {"range": [40, 60], "color": "#fdebd0"},
                {"range": [60, 75], "color": "#fef9e7"},
                {"range": [75, 90], "color": "#d5f5e3"},
                {"range": [90, 100], "color": "#abebc6"},
            ],
        },
    ))
    fig.update_layout(height=300, margin=dict(t=60, b=20, l=40, r=40))
    return fig


def pillar_bar_chart(pillar_scores):
    names = []
    scores = []
    colors = []
    for key in ["environmental", "social", "governance"]:
        s = pillar_scores.get(key, {}).get("score")
        names.append(PILLAR_DISPLAY_NAMES.get(key, key))
        scores.append(s if s is not None else 0)
        colors.append(_score_color(s))

    fig = go.Figure(go.Bar(
        x=scores,
        y=names,
        orientation="h",
        marker_color=colors,
        text=[f"{s:.1f}" for s in scores],
        textposition="auto",
    ))
    fig.update_layout(
        title="Pillar Scores",
        xaxis=dict(range=[0, 100], title="Score"),
        height=250,
        margin=dict(t=40, b=20, l=100, r=20),
    )
    return fig


def radar_chart(scores_data):
    categories = []
    values = []
    for pillar_name in ["environmental", "social", "governance"]:
        pillar = scores_data["pillars"].get(pillar_name, {})
        for cat, score in pillar.get("categories", {}).items():
            categories.append(CATEGORY_DISPLAY_NAMES.get(cat, cat))
            values.append(score if score is not None else 0)

    if not categories:
        return go.Figure()

    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        marker=dict(color="#3498db"),
        line=dict(color="#2980b9"),
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title="ESG Category Breakdown",
        height=500,
        margin=dict(t=60, b=40, l=80, r=80),
    )
    return fig


def category_breakdown_chart(categories, pillar_name):
    names = []
    scores = []
    colors = []
    for cat, score in categories.items():
        names.append(CATEGORY_DISPLAY_NAMES.get(cat, cat))
        scores.append(score if score is not None else 0)
        colors.append(_score_color(score))

    fig = go.Figure(go.Bar(
        x=scores,
        y=names,
        orientation="h",
        marker_color=colors,
        text=[f"{s:.1f}" for s in scores],
        textposition="auto",
    ))
    fig.update_layout(
        title=f"{PILLAR_DISPLAY_NAMES.get(pillar_name, pillar_name)} — Category Scores",
        xaxis=dict(range=[0, 100], title="Score"),
        height=max(200, len(names) * 50),
        margin=dict(t=40, b=20, l=150, r=20),
    )
    return fig
