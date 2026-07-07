PILLAR_WEIGHTS = {
    "environmental": 0.20,
    "social": 0.35,
    "governance": 0.45,
}

CATEGORY_WEIGHTS = {
    "environmental": {
        "financed_emissions": 0.30,
        "responsible_investment": 0.30,
        "operational_footprint": 0.20,
        "climate_risk_portfolio": 0.20,
    },
    "social": {
        "fair_customer_treatment": 0.25,
        "data_privacy_protection": 0.25,
        "talent_development": 0.20,
        "diversity_inclusion": 0.15,
        "community_investment": 0.15,
    },
    "governance": {
        "ethics_aml_compliance": 0.25,
        "board_composition": 0.20,
        "product_governance": 0.20,
        "risk_management": 0.20,
        "transparency_disclosure": 0.15,
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
    "financed_emissions": "Financed Emissions",
    "responsible_investment": "Responsible Investment",
    "operational_footprint": "Operational Footprint",
    "climate_risk_portfolio": "Climate Risk in Portfolio",
    "fair_customer_treatment": "Fair Customer Treatment",
    "data_privacy_protection": "Data Privacy & Protection",
    "talent_development": "Talent & Wellbeing",
    "diversity_inclusion": "Diversity & Inclusion",
    "community_investment": "Community Investment",
    "ethics_aml_compliance": "Ethics, AML & Compliance",
    "board_composition": "Board Composition",
    "product_governance": "Product Governance",
    "risk_management": "Risk Management",
    "transparency_disclosure": "Transparency & Disclosure",
}

PILLAR_DISPLAY_NAMES = {
    "environmental": "Environmental",
    "social": "Social",
    "governance": "Governance",
}
