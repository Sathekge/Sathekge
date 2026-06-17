PILLAR_WEIGHTS = {
    "environmental": 0.35,
    "social": 0.35,
    "governance": 0.30,
}

CATEGORY_WEIGHTS = {
    "environmental": {
        "carbon_emissions": 0.25,
        "energy_usage": 0.20,
        "waste_management": 0.20,
        "water_usage": 0.15,
        "environmental_policy": 0.20,
    },
    "social": {
        "labor_practices": 0.25,
        "diversity_inclusion": 0.20,
        "community_engagement": 0.15,
        "health_safety": 0.25,
        "human_rights": 0.15,
    },
    "governance": {
        "board_composition": 0.20,
        "ethics_compliance": 0.25,
        "transparency": 0.20,
        "risk_management": 0.20,
        "shareholder_rights": 0.15,
    },
}

MAX_SCORE_PER_QUESTION = 4

SCORE_LABELS = [
    (40, "Poor", "#e74c3c"),
    (60, "Below Average", "#e67e22"),
    (75, "Average", "#f1c40f"),
    (90, "Good", "#2ecc71"),
    (100, "Excellent", "#27ae60"),
]

CATEGORY_DISPLAY_NAMES = {
    "carbon_emissions": "Carbon Emissions",
    "energy_usage": "Energy Usage",
    "waste_management": "Waste Management",
    "water_usage": "Water Usage",
    "environmental_policy": "Environmental Policy",
    "labor_practices": "Labor Practices",
    "diversity_inclusion": "Diversity & Inclusion",
    "community_engagement": "Community Engagement",
    "health_safety": "Health & Safety",
    "human_rights": "Human Rights",
    "board_composition": "Board Composition",
    "ethics_compliance": "Ethics & Compliance",
    "transparency": "Transparency",
    "risk_management": "Risk Management",
    "shareholder_rights": "Shareholder Rights",
}

PILLAR_DISPLAY_NAMES = {
    "environmental": "Environmental",
    "social": "Social",
    "governance": "Governance",
}
