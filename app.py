
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ============================================================
# TERA 2.0 — ENVIRONMENTAL INTELLIGENCE DASHBOARD
# ============================================================

st.set_page_config(
    page_title="TERA 2.0 | Environmental Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- DARK FOREST THEME ---------------------

BG = "#101713"
PANEL = "#18221C"
PANEL_ALT = "#202D25"
BORDER = "#35463A"
TEXT = "#E5E9DF"
MUTED = "#A8B5A6"
ACCENT = "#A6C4A8"
GREEN = "#8FAF95"
AMBER = "#C8AD78"
RED = "#C98580"
LOW = "#769B7A"

PLOT_BG = PANEL
GRID = "#2B392F"

# -------------------- GLOBAL CSS -----------------------------

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {{
        color-scheme: dark;
    }}

    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{
        font-family: 'Manrope', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    [data-testid="stHeader"] {{
        background: {BG};
    }}

    [data-testid="stAppViewContainer"] > .main {{
        background: {BG};
    }}

    .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }}

    h1, h2, h3, h4, p, label, li {{
        color: {TEXT};
    }}

    h1 {{
        letter-spacing: -1.3px;
        font-weight: 800;
    }}

    h2, h3 {{
        letter-spacing: -0.4px;
        font-weight: 700;
    }}

    [data-testid="stCaptionContainer"] p,
    .muted {{
        color: {MUTED} !important;
    }}

    hr {{
        border-color: {BORDER};
    }}

    /* Hero section */

    .hero {{
        background: linear-gradient(120deg, #1D2A21, #17221B 70%, #202D25);
        border: 1px solid {BORDER};
        border-radius: 20px;
        padding: 25px 28px;
        margin-bottom: 20px;
    }}

    .eyebrow {{
        color: {ACCENT};
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 9px;
    }}

    .hero-title {{
        font-size: clamp(28px, 4vw, 43px);
        line-height: 1.13;
        font-weight: 800;
        color: {TEXT};
        margin: 0 0 10px 0;
    }}

    .hero-subtitle {{
        color: {MUTED};
        font-size: 14px;
        line-height: 1.7;
        margin: 0;
        max-width: 850px;
    }}

    /* Metric cards */

    .metric-card {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 17px 18px;
        min-height: 118px;
    }}

    .metric-label {{
        color: {MUTED};
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}

    .metric-value {{
        color: {TEXT};
        font-size: 30px;
        font-weight: 800;
        line-height: 1.5;
    }}

    .metric-note {{
        color: {MUTED};
        font-size: 11px;
    }}

    /* Information panels */

    .panel {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 12px;
    }}

    .panel-title {{
        color: {TEXT};
        font-weight: 800;
        font-size: 15px;
        margin-bottom: 7px;
    }}

    .panel-text {{
        color: {MUTED};
        font-size: 13px;
        line-height: 1.7;
    }}

    .priority-pill {{
        display: inline-block;
        padding: 5px 11px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.4px;
        border: 1px solid {BORDER};
    }}

    .critical {{
        color: {RED};
        background: #30201F;
    }}

    .high {{
        color: {AMBER};
        background: #30291D;
    }}

    .moderate {{
        color: {ACCENT};
        background: #202C24;
    }}

    .lower {{
        color: {GREEN};
        background: #1D2A20;
    }}

    /* Tabs */

    [data-testid="stTabs"] {{
        margin-top: 10px;
    }}

    [data-testid="stTabs"] button {{
        color: {MUTED} !important;
        font-weight: 700 !important;
        border-radius: 9px 9px 0 0;
    }}

    [data-testid="stTabs"] button[aria-selected="true"] {{
        color: {ACCENT} !important;
        border-bottom-color: {ACCENT} !important;
    }}

    [data-testid="stTabContent"] {{
        padding-top: 18px;
    }}

    /* Inputs */

    [data-testid="stSelectbox"] label,
    [data-testid="stSlider"] label {{
        color: {TEXT} !important;
        font-weight: 600;
    }}

    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        background-color: {PANEL_ALT} !important;
        color: {TEXT} !important;
        border-color: {BORDER} !important;
        border-radius: 10px !important;
    }}

    [data-baseweb="popover"],
    [data-baseweb="menu"] {{
        background-color: {PANEL_ALT} !important;
    }}

    [role="option"] {{
        background-color: {PANEL_ALT} !important;
        color: {TEXT} !important;
    }}

    [role="option"]:hover {{
        background-color: #304236 !important;
    }}

    [data-testid="stSlider"] [data-baseweb="slider"] {{
        color: {ACCENT};
    }}

    [data-testid="stSlider"] [role="slider"] {{
        background-color: {ACCENT} !important;
        border-color: {ACCENT} !important;
    }}

    /* Buttons */

    .stButton > button {{
        background: {PANEL_ALT};
        color: {TEXT};
        border: 1px solid {BORDER};
        border-radius: 10px;
        font-weight: 700;
    }}

    .stButton > button:hover {{
        background: #2A3B30;
        color: {TEXT};
        border-color: {ACCENT};
    }}

    /* Dark static tables */

    [data-testid="stTable"] {{
        background: {PANEL} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
        overflow: hidden;
    }}

    [data-testid="stTable"] table {{
        background: {PANEL} !important;
        color: {TEXT} !important;
        border-collapse: collapse !important;
        width: 100%;
    }}

    [data-testid="stTable"] thead tr th {{
        background: #26362B !important;
        color: {ACCENT} !important;
        border-bottom: 1px solid {BORDER} !important;
        padding: 11px !important;
        font-size: 12px !important;
    }}

    [data-testid="stTable"] tbody tr td {{
        background: {PANEL} !important;
        color: {TEXT} !important;
        border-bottom: 1px solid #2B392F !important;
        padding: 10px !important;
        font-size: 12px !important;
    }}

    [data-testid="stTable"] tbody tr:nth-child(even) td {{
        background: #1B271F !important;
    }}

    /* Keep the interactive data grid dark too */

    [data-testid="stDataFrame"] {{
        background: {PANEL} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }}

    [data-testid="stDataFrame"] iframe {{
        background: {PANEL} !important;
        color-scheme: dark;
    }}

    [data-testid="stDataFrame"] [role="grid"] {{
        background: {PANEL} !important;
        color: {TEXT} !important;
    }}

    /* Alerts and expanders */

    [data-testid="stAlert"] {{
        background: {PANEL_ALT} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
        color: {TEXT} !important;
    }}

    [data-testid="stExpander"] {{
        background: {PANEL} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
    }}

    [data-testid="stExpander"] summary {{
        color: {TEXT} !important;
    }}

    /* Footer */

    .footer {{
        color: {MUTED};
        text-align: center;
        font-size: 11px;
        padding: 20px 0 4px 0;
        border-top: 1px solid {BORDER};
        margin-top: 25px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- PROJECT DATA --------------------------

FACTORS = ["Hazard", "Vulnerability", "Population", "Exposure", "Urgency"]

WEIGHTS = {
    "Hazard": 0.30,
    "Vulnerability": 0.25,
    "Population": 0.20,
    "Exposure": 0.15,
    "Urgency": 0.10,
}

ZONES = {
    "Forest": [72, 65, 35, 95, 75],
    "Residential Area": [80, 85, 95, 45, 90],
    "Hospital": [75, 90, 90, 30, 95],
    "Smart Farm": [60, 65, 45, 75, 60],
    "River & Dam": [85, 75, 70, 85, 85],
    "Industrial Zone": [82, 70, 75, 65, 80],
}

ACTIONS = {
    "Forest": [
        "Monitor signs of forest fires and unusual heat.",
        "Identify vulnerable wildlife and forest patches.",
        "Maintain firebreaks and safe access routes.",
        "Plan rapid communication with forest personnel.",
    ],
    "Residential Area": [
        "Identify densely populated and vulnerable neighborhoods.",
        "Prepare evacuation routes and public warning messages.",
        "Keep emergency contacts and shelters accessible.",
        "Coordinate with local disaster response teams.",
    ],
    "Hospital": [
        "Protect uninterrupted emergency and medical services.",
        "Check backup power, water, and essential supplies.",
        "Keep patient evacuation and ambulance routes clear.",
        "Prepare a continuity plan for critical care.",
    ],
    "Smart Farm": [
        "Monitor crop stress, soil moisture, and water availability.",
        "Plan efficient irrigation and water conservation.",
        "Protect crops against relevant weather hazards.",
        "Use sustainable farming and soil-management practices.",
    ],
    "River & Dam": [
        "Monitor water levels and official warning bulletins.",
        "Identify low-lying areas that may require evacuation.",
        "Keep drainage and emergency access routes clear.",
        "Coordinate warnings with downstream communities.",
    ],
    "Industrial Zone": [
        "Inspect hazardous-material storage and safety procedures.",
        "Check emergency shutdown and containment plans.",
        "Maintain fire safety and worker evacuation routes.",
        "Prepare pollution-control and incident-response measures.",
    ],
}

# -------------------- CALCULATION FUNCTIONS -----------------

def calculate_risk(values):
    return round(
        sum(values[i] * WEIGHTS[FACTORS[i]] for i in range(len(FACTORS))),
        1
    )


def classify_risk(score):
    if score >= 80:
        return "Critical"
    elif score >= 65:
        return "High"
    elif score >= 45:
        return "Moderate"
    return "Lower"


def priority_color(priority):
    return {
        "Critical": RED,
        "High": AMBER,
        "Moderate": ACCENT,
        "Lower": GREEN,
    }.get(priority, ACCENT)


def priority_class(priority):
    return {
        "Critical": "critical",
        "High": "high",
        "Moderate": "moderate",
        "Lower": "lower",
    }.get(priority, "moderate")


def build_dataframe():
    rows = []

    for zone, values in ZONES.items():
        score = calculate_risk(values)
        rows.append({
            "Zone": zone,
            "Risk Score": score,
            "Priority": classify_risk(score),
            "Hazard": values[0],
            "Vulnerability": values[1],
            "Population": values[2],
            "Exposure": values[3],
            "Urgency": values[4],
        })

    return pd.DataFrame(rows).sort_values(
        "Risk Score", ascending=False
    ).reset_index(drop=True)


def make_plot_layout(fig, height=350):
    fig.update_layout(
        height=height,
        paper_bgcolor=PLOT_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(
            family="Manrope, sans-serif",
            color=TEXT,
            size=11
        ),
        margin=dict(l=12, r=12, t=35, b=12),
        xaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID,
            tickfont=dict(color=MUTED),
            title_font=dict(color=MUTED),
        ),
        yaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID,
            tickfont=dict(color=MUTED),
            title_font=dict(color=MUTED),
        ),
        legend=dict(
            font=dict(color=TEXT),
            bgcolor="rgba(0,0,0,0)"
        ),
        hoverlabel=dict(
            bgcolor=PANEL_ALT,
            font_color=TEXT,
            bordercolor=BORDER
        ),
    )
    return fig


def metric_card(label, value, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_priority(priority):
    css_class = priority_class(priority)
    st.markdown(
        f'<span class="priority-pill {css_class}">{priority.upper()} PRIORITY</span>',
        unsafe_allow_html=True
    )


# -------------------- HEADER --------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">TERA 2.0 · Environmental Intelligence</div>
        <div class="hero-title">See the risk.<br>Prioritise the response.</div>
        <p class="hero-subtitle">
            A weighted environmental risk-prioritisation system that compares
            different zones, identifies priority areas, and supports structured
            response planning.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- MAIN DATA -----------------------------

risk_df = build_dataframe()
highest = risk_df.iloc[0]
average_score = round(risk_df["Risk Score"].mean(), 1)
critical_count = int((risk_df["Priority"] == "Critical").sum())
high_count = int((risk_df["Priority"] == "High").sum())

# -------------------- NAVIGATION ----------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "◈ Command Centre",
    "⌁ Risk Simulator",
    "✚ Response Planner",
    "ⓘ Methodology & AI"
])

# ============================================================
# TAB 1 — COMMAND CENTRE
# ============================================================

with tab1:
    st.subheader("Environmental Risk Overview")
    st.caption(
        "Compare the model's current illustrative scores across six environmental zones."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Zones analysed", "06", "Environmental locations")

    with c2:
        metric_card(
            "Highest score",
            f"{highest['Risk Score']:.1f}",
            str(highest["Zone"])
        )

    with c3:
        metric_card(
            "Critical zones",
            f"{critical_count:02d}",
            "Score of 80 or above"
        )

    with c4:
        metric_card(
            "Average score",
            f"{average_score:.1f}",
            "Across all six zones"
        )

    st.write("")
    left, right = st.columns([1.45, 1])

    with left:
        st.markdown("### Risk Priority Ranking")
        st.caption("Higher scores indicate higher model-assessed priority.")

        bar_colors = [
            priority_color(p) for p in risk_df["Priority"]
        ]

        fig = go.Figure(
            go.Bar(
                x=risk_df["Risk Score"],
                y=risk_df["Zone"],
                orientation="h",
                marker=dict(
                    color=bar_colors,
                    line=dict(color=BORDER, width=0.7)
                ),
                text=[f"{s:.1f}" for s in risk_df["Risk Score"]],
                textposition="outside",
                textfont=dict(color=TEXT, size=11),
                hovertemplate=(
                    "<b>%{y}</b><br>Risk score: %{x:.1f}<extra></extra>"
                ),
            )
        )

        fig.update_yaxes(autorange="reversed")
        fig.update_xaxes(
            range=[0, 110],
            title="Weighted risk-priority score",
            dtick=20
        )
        make_plot_layout(fig, 365)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown("### Priority Distribution")

        counts = (
            risk_df["Priority"]
            .value_counts()
            .reindex(["Critical", "High", "Moderate", "Lower"], fill_value=0)
        )

        pie_colors = [RED, AMBER, ACCENT, GREEN]

        fig2 = go.Figure(
            go.Pie(
                labels=counts.index,
                values=counts.values,
                hole=0.67,
                marker=dict(
                    colors=pie_colors,
                    line=dict(color=PANEL, width=3)
                ),
                textinfo="label+value",
                textfont=dict(color=TEXT, size=11),
                hovertemplate="%{label}: %{value} zone(s)<extra></extra>",
            )
        )

        fig2.update_layout(
            annotations=[dict(
                text=f"{len(ZONES)}<br>Zones",
                x=0.5,
                y=0.5,
                font=dict(size=20, color=TEXT, family="Manrope"),
                showarrow=False
            )]
        )
        make_plot_layout(fig2, 300)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Current model leader</div>
                <div style="font-size:21px;font-weight:800;color:{TEXT};margin:8px 0;">
                    {highest['Zone']}
                </div>
                <div style="font-size:13px;color:{MUTED};margin-bottom:10px;">
                    Score: {highest['Risk Score']:.1f} / 100
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Zone Assessment Table")
    st.caption("Rankings are recalculated from the model's weighted input values.")

    display_df = risk_df[
        ["Zone", "Risk Score", "Priority", "Hazard",
         "Vulnerability", "Population", "Exposure", "Urgency"]
    ].copy()

    display_df["Risk Score"] = display_df["Risk Score"].map(
        lambda x: f"{x:.1f}"
    )

    # Static table gives us more reliable dark styling than the white canvas grid.
    st.table(display_df)

    with st.expander("How should these scores be interpreted?"):
        st.write(
            "The scores are comparative priority indices generated from the "
            "factor values and weights shown in this demonstration. They are "
            "not probabilities of disasters, official alerts, or validated "
            "real-world forecasts."
        )

# ============================================================
# TAB 2 — RISK SIMULATOR
# ============================================================

with tab2:
    st.subheader("Risk Scenario Simulator")
    st.caption(
        "Adjust the five factors to explore how changing conditions affect the model score."
    )

    selected_zone = st.selectbox(
        "Choose an environmental zone",
        list(ZONES.keys()),
        key="sim_zone"
    )

    baseline = ZONES[selected_zone]

    st.markdown("#### Adjust the scenario")
    st.caption("Use the sliders to set each factor from 0 to 100.")

    left, right = st.columns(2)
    values = []

    for i, factor in enumerate(FACTORS):
        column = left if i % 2 == 0 else right

        with column:
            val = st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(baseline[i]),
                key=f"slider_{selected_zone}_{factor}",
                help=f"Contribution weight: {WEIGHTS[factor] * 100:.0f}%"
            )
            values.append(val)

    simulated_score = calculate_risk(values)
    simulated_priority = classify_risk(simulated_score)
    base_score = calculate_risk(baseline)
    difference = round(simulated_score - base_score, 1)

    st.write("")
    res1, res2, res3 = st.columns(3)

    with res1:
        metric_card(
            "Simulated score",
            f"{simulated_score:.1f}",
            "Out of 100"
        )

    with res2:
        metric_card(
            "Baseline score",
            f"{base_score:.1f}",
            "Original illustrative inputs"
        )

    with res3:
        difference_text = f"{difference:+.1f}"
        metric_card(
            "Score change",
            difference_text,
            "Compared with baseline"
        )

    show_priority(simulated_priority)
    st.write("")

    st.markdown("### Factor Contributions")
    contributions = [
        values[i] * WEIGHTS[FACTORS[i]] for i in range(len(FACTORS))
    ]

    contrib_df = pd.DataFrame({
        "Factor": FACTORS,
        "Weighted contribution": contributions,
        "Weight (%)": [WEIGHTS[f] * 100 for f in FACTORS],
    }).sort_values("Weighted contribution", ascending=True)

    fig3 = go.Figure(
        go.Bar(
            x=contrib_df["Weighted contribution"],
            y=contrib_df["Factor"],
            orientation="h",
            marker=dict(
                color=GREEN,
                line=dict(color=BORDER, width=0.7)
            ),
            text=[
                f"{v:.1f}" for v in contrib_df["Weighted contribution"]
            ],
            textposition="outside",
            textfont=dict(color=TEXT, size=11),
            hovertemplate=(
                "<b>%{y}</b><br>Weighted contribution: %{x:.1f}<extra></extra>"
            )
        )
    )

    fig3.update_xaxes(title="Contribution to total score", rangemode="tozero")
    make_plot_layout(fig3, 300)
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("### Factor Breakdown")
    breakdown = pd.DataFrame({
        "Factor": FACTORS,
        "Input value": values,
        "Weight": [f"{WEIGHTS[f] * 100:.0f}%" for f in FACTORS],
        "Weighted contribution": [round(x, 2) for x in contributions],
    })
    st.table(breakdown)

    st.info(
        "This simulator demonstrates how the chosen inputs affect a weighted "
        "index. Changing a slider changes the scenario, not the real-world "
        "conditions of the selected location."
    )

# ============================================================
# TAB 3 — RESPONSE PLANNER
# ============================================================

with tab3:
    st.subheader("Environmental Response Planner")
    st.caption(
        "Use the model's priority classification to organise possible response actions."
    )

    selected_response_zone = st.selectbox(
        "Select a zone for response planning",
        list(ZONES.keys()),
        key="response_zone"
    )

    response_values = ZONES[selected_response_zone]
    response_score = calculate_risk(response_values)
    response_priority = classify_risk(response_score)

    col1, col2 = st.columns([1, 1.4])

    with col1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="eyebrow">Zone assessment</div>
                <div style="font-size:23px;font-weight:800;color:{TEXT};margin:10px 0;">
                    {selected_response_zone}
                </div>
                <div style="font-size:35px;font-weight:800;color:{priority_color(response_priority)};">
                    {response_score:.1f}<span style="font-size:13px;color:{MUTED};"> / 100</span>
                </div>
                <div style="margin-top:12px;">
                    <span class="priority-pill {priority_class(response_priority)}">
                        {response_priority.upper()} PRIORITY
                    </span>
                </div>
                <p class="panel-text" style="margin-top:14px;">
                    The priority level is determined by the score thresholds
                    defined in the TERA demonstration model.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("### Suggested response actions")

        for index, action in enumerate(ACTIONS[selected_response_zone], start=1):
            st.markdown(
                f"""
                <div class="panel" style="padding:13px 15px;">
                    <span style="color:{ACCENT};font-weight:800;margin-right:10px;">
                        {index:02d}
                    </span>
                    <span style="color:{TEXT};font-size:13px;">
                        {action}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Response planning principles")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">01 · Assess</div>
                <div class="panel-text">
                    Review the hazard, exposure, vulnerability, population,
                    and urgency inputs before taking action.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with p2:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">02 · Prioritise</div>
                <div class="panel-text">
                    Use the score to support discussion about where limited
                    response resources may be needed first.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with p3:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">03 · Verify</div>
                <div class="panel-text">
                    Confirm conditions with official warnings, local experts,
                    and reliable observations before making real decisions.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.warning(
        "These are educational planning suggestions, not live emergency "
        "instructions. Follow official authorities during an actual emergency."
    )

# ============================================================
# TAB 4 — METHODOLOGY & AI
# ============================================================

with tab4:
    st.subheader("Methodology & Model Transparency")
    st.caption(
        "A transparent weighted scoring method makes the demonstration easier to inspect and explain."
    )

    st.markdown("### Weighted risk-priority formula")

    st.latex(
        r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U"
    )

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">What the formula means</div>
            <div class="panel-text">
                Each factor receives a score from 0 to 100. The model multiplies
                each factor by its assigned weight and adds the contributions.
                Hazard has the largest weight at 30%, while urgency contributes
                10%. The final weighted score ranges from 0 to 100.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Factor weights")

    weights_df = pd.DataFrame({
        "Factor": FACTORS,
        "Weight": [f"{WEIGHTS[f] * 100:.0f}%" for f in FACTORS],
        "Purpose": [
            "Represents the assessed intensity of a hazard.",
            "Represents how susceptible a zone may be to harm.",
            "Represents the population-related dimension of the assessment.",
            "Represents the assessed degree of exposure.",
            "Represents the urgency assigned in the scenario.",
        ]
    })

    st.table(weights_df)

    st.markdown("### Priority thresholds")

    thresholds_df = pd.DataFrame({
        "Priority": ["Critical", "High", "Moderate", "Lower"],
        "Score range": ["80–100", "65–79.9", "45–64.9", "Below 45"],
        "Interpretation": [
            "Highest model-assessed priority",
            "Elevated model-assessed priority",
            "Intermediate model-assessed priority",
            "Lower model-assessed priority",
        ]
    })

    st.table(thresholds_df)

    st.markdown("### Technology stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Python</div>
                <div class="panel-text">
                    Performs the weighted calculations and applies the priority rules.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tech2:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Pandas</div>
                <div class="panel-text">
                    Organises zone inputs, calculates rankings, and structures tabular data.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tech3:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Streamlit + Plotly</div>
                <div class="panel-text">
                    Streamlit provides the interactive interface; Plotly visualises the results.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Scientific limitations")

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">What TERA currently does</div>
            <div class="panel-text">
                Calculates and compares illustrative environmental risk-priority
                scores using predefined inputs and transparent weights.
            </div>
            <br>
            <div class="panel-title">What TERA does not currently do</div>
            <div class="panel-text">
                It does not receive live sensor data, verify current environmental
                conditions, or predict the probability of a real disaster.
                The example values and weights are demonstration assumptions,
                not scientifically validated local measurements.
            </div>
            <br>
            <div class="panel-title">How the model could be improved</div>
            <div class="panel-text">
                Future versions could incorporate reliable official datasets,
                expert-reviewed weights, measured local indicators, validation
                against past events, and uncertainty analysis.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- FOOTER --------------------------------

st.markdown(
    """
    <div class="footer">
        TERA 2.0 · Technology for Environmental Risk Analysis<br>
        An educational decision-support prototype · Scores are illustrative, not live forecasts
    </div>
    """,
    unsafe_allow_html=True
)
