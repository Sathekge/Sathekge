from config.scoring import (
    CATEGORY_WEIGHTS,
    MAX_SCORE_PER_QUESTION,
    PILLAR_WEIGHTS,
    SCORE_LABELS,
)


def score_category(responses, questions, category):
    cat_questions = [q for q in questions if q["category"] == category]
    if not cat_questions:
        return None

    total_weighted = 0.0
    total_weight = 0.0
    for q in cat_questions:
        if q["id"] in responses:
            total_weighted += responses[q["id"]] * q["weight"]
            total_weight += q["weight"]

    if total_weight == 0:
        return None
    return (total_weighted / (total_weight * MAX_SCORE_PER_QUESTION)) * 100


def score_pillar(responses, questions, pillar_name):
    categories = CATEGORY_WEIGHTS.get(pillar_name, {})
    category_scores = {}
    weighted_sum = 0.0
    weight_sum = 0.0

    for cat, weight in categories.items():
        s = score_category(responses, questions, cat)
        if s is not None:
            category_scores[cat] = s
            weighted_sum += s * weight
            weight_sum += weight

    if weight_sum == 0:
        return None, category_scores

    pillar_score = weighted_sum / weight_sum
    return pillar_score, category_scores


def score_overall(pillar_scores):
    weighted_sum = 0.0
    weight_sum = 0.0
    for pillar, score in pillar_scores.items():
        if score is not None:
            w = PILLAR_WEIGHTS.get(pillar, 0)
            weighted_sum += score * w
            weight_sum += w
    if weight_sum == 0:
        return None
    return weighted_sum / weight_sum


def get_score_label(score):
    if score is None:
        return "N/A", "#95a5a6"
    for threshold, label, color in SCORE_LABELS:
        if score <= threshold:
            return label, color
    return "Excellent", "#27ae60"


def compute_all(responses, all_questions):
    from data.questions import (
        ENVIRONMENTAL_QUESTIONS,
        GOVERNANCE_QUESTIONS,
        SOCIAL_QUESTIONS,
    )

    pillars = {}
    pillar_map = {
        "environmental": ENVIRONMENTAL_QUESTIONS,
        "social": SOCIAL_QUESTIONS,
        "governance": GOVERNANCE_QUESTIONS,
    }

    pillar_scores = {}
    for name, questions in pillar_map.items():
        p_score, cat_scores = score_pillar(responses, questions, name)
        pillar_scores[name] = p_score
        pillars[name] = {"score": p_score, "categories": cat_scores}

    overall = score_overall(pillar_scores)
    label, color = get_score_label(overall)

    return {
        "overall": overall,
        "overall_label": label,
        "overall_color": color,
        "pillars": pillars,
    }
