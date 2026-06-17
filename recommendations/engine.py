RECOMMENDATIONS = {
    "carbon_emissions": {
        "low": [
            "Begin measuring your organization's carbon footprint using the GHG Protocol framework.",
            "Establish a baseline for Scope 1 and Scope 2 emissions.",
        ],
        "medium": [
            "Set science-based emissions reduction targets aligned with the Paris Agreement.",
            "Develop a roadmap to reduce emissions across operations and supply chain.",
        ],
        "high": [
            "Pursue net-zero commitments with verified offset programs.",
            "Engage supply chain partners in collaborative emissions reduction initiatives.",
        ],
    },
    "energy_usage": {
        "low": [
            "Implement energy monitoring systems to track consumption across facilities.",
            "Conduct an energy audit to identify efficiency improvement opportunities.",
        ],
        "medium": [
            "Set renewable energy procurement targets (e.g., RE100 commitment).",
            "Invest in on-site renewable energy generation where feasible.",
        ],
        "high": [
            "Achieve 100% renewable energy for operations.",
            "Share energy efficiency best practices with industry peers.",
        ],
    },
    "waste_management": {
        "low": [
            "Implement waste tracking and categorization across all operations.",
            "Establish basic recycling programs at all facilities.",
        ],
        "medium": [
            "Set waste reduction targets and implement circular economy principles.",
            "Partner with waste management providers for improved diversion rates.",
        ],
        "high": [
            "Pursue zero-waste-to-landfill certification.",
            "Develop product take-back or closed-loop recycling programs.",
        ],
    },
    "water_usage": {
        "low": [
            "Install water metering and monitoring systems across operations.",
            "Identify water-intensive processes and assess reduction opportunities.",
        ],
        "medium": [
            "Set water reduction targets especially in water-stressed regions.",
            "Implement water recycling and reuse systems.",
        ],
        "high": [
            "Achieve water-positive status through restoration and replenishment projects.",
            "Lead industry collaboration on water stewardship.",
        ],
    },
    "environmental_policy": {
        "low": [
            "Develop a formal environmental policy and communicate it to all stakeholders.",
            "Consider implementing an Environmental Management System (ISO 14001).",
        ],
        "medium": [
            "Achieve ISO 14001 certification and integrate environmental criteria into procurement.",
            "Publish an annual environmental performance report.",
        ],
        "high": [
            "Align reporting with TCFD and other leading frameworks.",
            "Integrate environmental performance into executive compensation.",
        ],
    },
    "labor_practices": {
        "low": [
            "Review and align labor practices with ILO core conventions.",
            "Establish minimum wage standards above local legal requirements.",
        ],
        "medium": [
            "Implement comprehensive employee development and training programs.",
            "Conduct regular employee satisfaction surveys with published results.",
        ],
        "high": [
            "Become an employer of choice with industry-leading benefits and flexibility.",
            "Extend fair labor standards to all supply chain tiers.",
        ],
    },
    "diversity_inclusion": {
        "low": [
            "Develop and publish a formal Diversity, Equity & Inclusion policy.",
            "Begin tracking workforce diversity metrics across all levels.",
        ],
        "medium": [
            "Set measurable diversity targets for leadership and board positions.",
            "Implement unconscious bias training and inclusive hiring practices.",
        ],
        "high": [
            "Publish pay equity audits and close identified gaps.",
            "Serve as an industry advocate for diversity and inclusion standards.",
        ],
    },
    "community_engagement": {
        "low": [
            "Identify key community stakeholders and establish engagement channels.",
            "Develop a community investment or CSR strategy.",
        ],
        "medium": [
            "Implement structured community programs aligned with core business capabilities.",
            "Measure and report social impact of community initiatives.",
        ],
        "high": [
            "Scale successful programs and share impact methodologies publicly.",
            "Co-create community development strategies with local stakeholders.",
        ],
    },
    "health_safety": {
        "low": [
            "Implement a formal occupational health and safety management system.",
            "Begin tracking and reporting workplace injury and incident rates.",
        ],
        "medium": [
            "Achieve ISO 45001 certification and implement proactive safety programs.",
            "Introduce mental health and wellbeing support for all employees.",
        ],
        "high": [
            "Achieve industry-leading safety performance with zero-harm targets.",
            "Extend health and safety standards throughout the supply chain.",
        ],
    },
    "human_rights": {
        "low": [
            "Develop a human rights policy aligned with the UN Guiding Principles.",
            "Conduct an initial human rights risk assessment of operations.",
        ],
        "medium": [
            "Implement human rights due diligence processes across the supply chain.",
            "Establish accessible grievance mechanisms for affected stakeholders.",
        ],
        "high": [
            "Publicly report on human rights due diligence findings and remediation actions.",
            "Advocate for human rights standards across the industry.",
        ],
    },
    "board_composition": {
        "low": [
            "Increase the proportion of independent directors on the board.",
            "Establish board diversity targets for gender, ethnicity, and expertise.",
        ],
        "medium": [
            "Create a dedicated ESG or sustainability committee at board level.",
            "Implement regular board effectiveness reviews with published results.",
        ],
        "high": [
            "Achieve best-practice board composition with diverse, independent oversight.",
            "Link board evaluation to ESG performance outcomes.",
        ],
    },
    "ethics_compliance": {
        "low": [
            "Develop and distribute a comprehensive code of ethics and conduct.",
            "Implement anti-corruption and anti-bribery policies with training.",
        ],
        "medium": [
            "Establish a whistleblower protection program with anonymous reporting.",
            "Conduct regular ethics training and compliance audits.",
        ],
        "high": [
            "Achieve recognized ethical business certifications.",
            "Lead industry collaboration on ethical business standards.",
        ],
    },
    "transparency": {
        "low": [
            "Begin publishing an annual sustainability or ESG report.",
            "Disclose basic ESG metrics alongside financial reporting.",
        ],
        "medium": [
            "Adopt recognized reporting frameworks (GRI, SASB, TCFD).",
            "Seek external assurance for ESG data and disclosures.",
        ],
        "high": [
            "Achieve best-in-class transparency with integrated reporting.",
            "Link executive compensation to published ESG targets.",
        ],
    },
    "risk_management": {
        "low": [
            "Integrate ESG risks into the enterprise risk management framework.",
            "Conduct an initial climate-related risk assessment.",
        ],
        "medium": [
            "Implement scenario analysis for climate and ESG risks (TCFD-aligned).",
            "Establish a cybersecurity and data privacy governance framework.",
        ],
        "high": [
            "Achieve advanced ESG risk integration with real-time monitoring.",
            "Share risk management methodologies with industry peers.",
        ],
    },
    "shareholder_rights": {
        "low": [
            "Ensure equal voting rights and transparent shareholder communication.",
            "Develop a policy on related-party transactions.",
        ],
        "medium": [
            "Engage shareholders proactively on ESG matters and strategy.",
            "Provide shareholders with advisory votes on ESG policies.",
        ],
        "high": [
            "Achieve leading-practice shareholder engagement and governance standards.",
            "Facilitate shareholder-led ESG proposals and resolutions.",
        ],
    },
}


def _get_tier(score):
    if score is None:
        return "low"
    if score < 40:
        return "low"
    if score < 75:
        return "medium"
    return "high"


def generate_recommendations(scores_data):
    results = []
    for pillar_name, pillar_data in scores_data["pillars"].items():
        for category, cat_score in pillar_data["categories"].items():
            tier = _get_tier(cat_score)
            recs = RECOMMENDATIONS.get(category, {}).get(tier, [])
            priority = "High" if tier == "low" else ("Medium" if tier == "medium" else "Low")
            for text in recs:
                results.append({
                    "pillar": pillar_name,
                    "category": category,
                    "priority": priority,
                    "score": cat_score,
                    "text": text,
                })

    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    results.sort(key=lambda r: priority_order.get(r["priority"], 3))
    return results
