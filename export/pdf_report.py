import tempfile
from datetime import datetime

from fpdf import FPDF

from config.scoring import CATEGORY_DISPLAY_NAMES, PILLAR_DISPLAY_NAMES
from scoring.engine import get_score_label


class ESGReport(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "ESG Diagnostic Report", align="L")
        self.cell(0, 8, datetime.now().strftime("%Y-%m-%d"), align="R", new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def _color_for_score(score):
    _, color = get_score_label(score)
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    return r, g, b


def generate_pdf(scores_data, recommendations, chart_figures=None):
    pdf = ESGReport()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # Title page
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 28)
    pdf.ln(30)
    pdf.cell(0, 15, "ESG Diagnostic Report", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%B %d, %Y')}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)

    overall = scores_data.get("overall")
    label, color = get_score_label(overall)
    r, g, b = _color_for_score(overall)
    pdf.set_font("Helvetica", "B", 48)
    pdf.set_text_color(r, g, b)
    pdf.cell(0, 25, f"{overall:.1f}/100" if overall is not None else "N/A", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, label, align="C", new_x="LMARGIN", new_y="NEXT")

    # Executive summary
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Executive Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 11)
    pdf.set_fill_color(52, 73, 94)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(80, 10, "Pillar", border=1, fill=True)
    pdf.cell(40, 10, "Score", border=1, fill=True)
    pdf.cell(50, 10, "Rating", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 11)
    for pillar_key in ["environmental", "social", "governance"]:
        pillar = scores_data["pillars"].get(pillar_key, {})
        s = pillar.get("score")
        lbl, _ = get_score_label(s)
        r, g, b = _color_for_score(s)

        pdf.set_text_color(0, 0, 0)
        pdf.cell(80, 10, PILLAR_DISPLAY_NAMES.get(pillar_key, pillar_key), border=1)
        pdf.set_text_color(r, g, b)
        pdf.cell(40, 10, f"{s:.1f}" if s is not None else "N/A", border=1)
        pdf.cell(50, 10, lbl, border=1, new_x="LMARGIN", new_y="NEXT")

    # Embed charts if available
    if chart_figures:
        for name, fig in chart_figures.items():
            try:
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                    fig.write_image(tmp.name, width=700, height=400, scale=2)
                    pdf.add_page()
                    pdf.set_text_color(0, 0, 0)
                    pdf.set_font("Helvetica", "B", 16)
                    pdf.cell(0, 12, name, new_x="LMARGIN", new_y="NEXT")
                    pdf.ln(3)
                    pdf.image(tmp.name, x=15, w=180)
            except Exception:
                pass

    # Pillar details
    for pillar_key in ["environmental", "social", "governance"]:
        pillar = scores_data["pillars"].get(pillar_key, {})
        pdf.add_page()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 12, f"{PILLAR_DISPLAY_NAMES.get(pillar_key, pillar_key)} Pillar", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)

        s = pillar.get("score")
        lbl, _ = get_score_label(s)
        r, g, b = _color_for_score(s)
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(r, g, b)
        pdf.cell(0, 10, f"Pillar Score: {s:.1f}/100 - {lbl}" if s is not None else "N/A", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)

        pdf.set_font("Helvetica", "B", 11)
        pdf.set_fill_color(52, 73, 94)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(90, 10, "Category", border=1, fill=True)
        pdf.cell(40, 10, "Score", border=1, fill=True)
        pdf.cell(50, 10, "Rating", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Helvetica", "", 11)
        for cat, cat_score in pillar.get("categories", {}).items():
            lbl, _ = get_score_label(cat_score)
            r, g, b = _color_for_score(cat_score)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(90, 10, CATEGORY_DISPLAY_NAMES.get(cat, cat), border=1)
            pdf.set_text_color(r, g, b)
            pdf.cell(40, 10, f"{cat_score:.1f}" if cat_score is not None else "N/A", border=1)
            pdf.cell(50, 10, lbl, border=1, new_x="LMARGIN", new_y="NEXT")

    # Recommendations
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Recommendations", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    priority_colors = {
        "High": (231, 76, 60),
        "Medium": (230, 126, 34),
        "Low": (39, 174, 96),
    }

    for rec in recommendations:
        if pdf.get_y() > 250:
            pdf.add_page()

        pr, pg, pb = priority_colors.get(rec["priority"], (0, 0, 0))
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(pr, pg, pb)
        pdf.cell(20, 7, f"[{rec['priority']}]")
        pdf.set_text_color(100, 100, 100)
        pdf.set_font("Helvetica", "I", 9)
        pdf.cell(50, 7, CATEGORY_DISPLAY_NAMES.get(rec["category"], rec["category"]))
        pdf.ln(7)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, rec["text"])
        pdf.ln(3)

    return pdf.output()
