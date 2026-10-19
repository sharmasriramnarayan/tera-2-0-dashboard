
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TERA 2.0 | Environmental Intelligence",
    page_icon="🌿",
    layout="wide"
)

# --------------------------------------------------
# TERA MIDNIGHT FOREST THEME
# --------------------------------------------------

BG = "#101713"
PANEL = "#18221C"
PANEL_ALT = "#202D25"
BORDER = "#35463A"
TEXT = "#E5E9DF"
MUTED = "#A8B5A6"
ACCENT = "#A6C4A8"
ACCENT_DARK = "#587C61"
AMBER = "#D8B982"
RED = "#D58F89"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --background: #101713;
    --panel: #18221C;
    --border: #35463A;
    --text: #E5E9DF;
    --muted: #A8B5A6;
    --accent: #A6C4A8;
}

.stApp {
    background: #101713;
    color: #E5E9DF;
    font-family: 'Manrope', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(16, 23, 19, 0.95);
}

[data-testid="stSidebar"] {
    background: #151E18;
    border-right: 1px solid #35463A;
}

.block-container {
    max-width: 1380px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #E5E9DF !important;
    letter-spacing: -0.5px;
}

p, li, label, .stMarkdown {
    color: #D1D9CF;
}

.hero {
    background: linear-gradient(125deg, #202F25, #18221C);
    border: 1px solid #35463A;
    border-radius: 20px;
    padding: 28px 32px;
    margin-bottom: 22px;
}

.eyebrow {
    color: #A6C4A8;
    font-size: 11px;
    letter-spacing: 2.5px;
    font-weight: 800;
}

.hero-title {
    color: #E5E9DF;
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    line-height: 1.15;
    margin: 14px 0;
}

.hero-accent {
    color: #A6C4A8;
}

.hero-description {
    color: #B7C3B5;
    font-size: 15px;
    line-height: 1.8;
    max-width: 760px;
}

.metric-card {
    background: #18221C;
    border: 1px solid #35463A;
    border-radius: 15px;
    padding: 17px 19px;
    min-height: 100px;
}

.metric-label {
    color: #A8B5A6;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    font-weight: 700;
}

.metric-value {
    color: #D5E2D3;
    font-size: 25px;
    font-weight: 800;
    margin-top: 8px;
    overflow-wrap: anywhere;
}

.section-note {
    color: #A8B5A6;
    font-size: 13px;
    line-height: 1.7;
}

div[data-baseweb="tab-list"] {
    background: #151E18;
    border: 1px solid #35463A;
    border-radius: 13px;
    padding: 5px;
    gap: 5px;
}

button[data-baseweb="tab"] {
    background: transparent;
    border-radius: 9px;
    color: #B7C3B5;
    padding: 10px 14px;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: #29382C;
    color: #E5E9DF;
}

button[data-baseweb="tab"] p {
    color: inherit !important;
    font-weight: 600;
}

div[data-baseweb="select"] > div {
    background: #202D25;
    border: 1px solid #46594A;
    border-radius: 10px;
    color: #E5E9DF;
}

div[data-baseweb="select"] span {
    color: #E5E9DF;
}

div[data-baseweb="popover"] {
    background: #202D25;
}

div[role="listbox"] {
    background: #202D25;
}

div[role="option"] {
    color: #E5E9DF;
}

div[role="option"]:hover {
    background: #35463A;
}

.stSlider [data-baseweb="slider"] div {
    transition: none;
}

.stSlider [data-testid="stTickBar"] {
    background: #35463A;
}

.stSlider [role="slider"] {
    background: #A6C4A8;
    border-color: #A6C4A8;
    box-shadow: none;
}

.stSlider [data-testid="stSlider"] p {
    color: #D1D9CF;
}

div[data-testid="stMetric"] {
    background: #18221C;
    border: 1px solid #35463A;
    padding: 15px 17px;
    border-radius: 14px;
}

div[data-testid="stMetricLabel"] {
    color: #A8B5A6;
}

div[data-testid="stMetricValue"] {
    color: #D5E2D3;
}

div[data-testid="stMetricDelta"] {
    color: #B7C3B5;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #35463A;
    border-radius: 12px;
    overflow: hidden;
}

.stAlert {
    background: #202D25;
    border: 1px solid #46594A;
    border-radius: 12px;
}

.stAlert p {
    color: #E5E9DF !important;
}

.stButton button {
    background: #29382C;
    color: #E5E9DF;
    border: 1px solid #46594A;
    border-radius: 10px;
}

.stButton button:hover {
    background: #35463A;
    border-color: #718B74;
    color: #FFFFFF;
}

hr {
    border-color: #35463A;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

.footnote {
    color: #8F9D90;
    font-size: 11px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">
        TERA 2.0 &nbsp; / &nbsp; ENVIRONMENTAL INTELLIGENCE
    </div>
    <div class="hero-title">
        See the risk.<br>
        <span class="hero-accent">Prioritise the response.</span>
    </div>
    <div class="hero-description">
        A transparent environmental risk-prioritisation prototype.
        Compare six zones, explore hypothetical scenarios, and
        review possible preparedness actions.
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA AND SCORING
# --------------------------------------------------

zones = {
    "Forest": [72, 65, 35, 95, 75],
    "Residential Area": [80, 85, 95, 45, 90],
    "Hospital": [75, 90, 90, 30, 95],
    "Smart Farm": [60, 65, 45, 75, 60],
    "River & Dam": [85, 75, 70, 85, 85],
    "Industrial Zone": [82, 70, 75, 65, 80],
}

factor_names = [
    "Hazard Severity",
    "Vulnerability",
    "Population Impact",
    "Ecological Value",
    "Urgency",
]

weights = [0.30, 0.25, 0.20, 0.15, 0.10]

def calculate_risk(values):
    return round(
        sum(v * w for v, w in zip(values, weights)), 2
    )

def classify_risk(score):
    if score >= 80:
        return "CRITICAL"
    elif score >= 65:
        return "HIGH"
    elif score >= 45:
        return "MODERATE"
    return "LOWER"

def risk_colour(priority):
    return {
        "CRITICAL": "#D58F89",
        "HIGH": "#D8B982",
        "MODERATE": "#A6C4A8",
        "LOWER": "#8EA99A",
    }.get(priority, "#A8B5A6")

rows = []

for name, values in zones.items():
    score = calculate_risk(values)
    rows.append({
        "Zone": name,
        "Risk score": score,
        "Priority": classify_risk(score),
    })

df = pd.DataFrame(rows).sort_values(
    "Risk score", ascending=False
).reset_index(drop=True)

# --------------------------------------------------
# FOUR TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "◈  Command Centre",
    "⌁  Risk Simulator",
    "◎  Response Planner",
    "✳  Methodology & AI",
])

# --------------------------------------------------
# TAB 1: COMMAND CENTRE
# --------------------------------------------------

with tab1:
    st.subheader("Environmental Overview")
    st.markdown(
        '<div class="section-note">'
        'A comparative view of the current illustrative '
        'risk-priority scores.</div>',
        unsafe_allow_html=True
    )
    st.write("")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Zones Assessed</div>
            <div class="metric-value">06</div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">Highest Priority Zone</div>
            <div class="metric-value" style="font-size:21px">
            {df.iloc[0]["Zone"]}</div></div>""",
            unsafe_allow_html=True
        )

    with c:
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">Highest Index</div>
            <div class="metric-value">
            {df.iloc[0]["Risk score"]:.1f}
            <span style="font-size:13px;color:#A8B5A6">
            / 100</span></div></div>""",
            unsafe_allow_html=True
        )

    st.write("")
    st.subheader("Risk-Priority Ranking")

    chart_df = df.sort_values("Risk score", ascending=True)

    fig = px.bar(
        chart_df,
        x="Risk score",
        y="Zone",
        orientation="h",
        color="Priority",
        color_discrete_map={
            "CRITICAL": "#D58F89",
            "HIGH": "#D8B982",
            "MODERATE": "#A6C4A8",
            "LOWER": "#8EA99A",
        },
        category_orders={
            "Priority": [
                "CRITICAL", "HIGH", "MODERATE", "LOWER"
            ]
        },
        hover_data={"Risk score": ":.1f"},
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Manrope, sans-serif",
            color="#D1D9CF",
            size=12
        ),
        legend_title_text="Priority",
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#B7C3B5")
        ),
        xaxis=dict(
            title="Risk-priority index",
            range=[0, 100],
            gridcolor="#29372D",
            zerolinecolor="#35463A"
        ),
        yaxis=dict(
            title="",
            gridcolor="rgba(0,0,0,0)"
        ),
        margin=dict(l=5, r=15, t=15, b=10),
        height=350,
        bargap=0.38,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    st.subheader("Zone Assessment")

    display_df = df.copy()
    display_df["Risk score"] = display_df["Risk score"].map(
        lambda x: f"{x:.1f} / 100"
    )

    st.dataframe(
        display_df,
        hide_index=True,
        use_container_width=True
    )

# --------------------------------------------------
# TAB 2: RISK SIMULATOR
# --------------------------------------------------

with tab2:
    st.subheader("Scenario Laboratory")
    st.markdown(
        '<div class="section-note">'
        'Change one or more factor values to explore a '
        'hypothetical environmental scenario.</div>',
        unsafe_allow_html=True
    )

    selected_zone = st.selectbox(
        "Choose a zone",
        list(zones.keys()),
        key="simulator_zone"
    )

    default_values = zones[selected_zone]
    new_values = []

    st.markdown("#### Adjust Risk Factors")

    for i, (name, default) in enumerate(
        zip(factor_names, default_values)
    ):
        value = st.slider(
            name,
            min_value=0,
            max_value=100,
            value=int(default),
            help="Illustrative factor score from 0 to 100.",
            key=f"factor_{selected_zone}_{i}"
        )
        new_values.append(value)

    new_score = calculate_risk(new_values)
    new_priority = classify_risk(new_score)

    st.write("")

    score_col, priority_col = st.columns(2)

    with score_col:
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">
            Simulated Risk-Priority Index</div>
            <div class="metric-value">
            {new_score:.1f}
            <span style="font-size:13px;color:#A8B5A6">
            / 100</span></div></div>""",
            unsafe_allow_html=True
        )

    with priority_col:
        colour = risk_colour(new_priority)
        st.markdown(
            f"""<div class="metric-card">
            <div class="metric-label">Priority Classification</div>
            <div class="metric-value"
            style="color:{colour};font-size:23px">
            {new_priority}</div></div>""",
            unsafe_allow_html=True
        )

    st.write("")
    st.subheader("Factor Contributions")

    contributions = pd.DataFrame({
        "Factor": factor_names,
        "Contribution": [
            value * weight
            for value, weight in zip(new_values, weights)
        ]
    }).sort_values("Contribution", ascending=True)

    contribution_fig = px.bar(
        contributions,
        x="Contribution",
        y="Factor",
        orientation="h",
        color_discrete_sequence=["#8FAF95"],
        text=contributions["Contribution"].map(
            lambda x: f"{x:.1f}"
        )
    )

    contribution_fig.update_traces(
        textposition="outside",
        textfont=dict(color="#D1D9CF", size=11),
        cliponaxis=False,
        marker_line_width=0
    )

    contribution_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Manrope, sans-serif",
            color="#B7C3B5",
            size=11
        ),
        xaxis=dict(
            title="Weighted contribution to score",
            range=[
                0,
                max(10, contributions["Contribution"].max() * 1.3)
            ],
            gridcolor="#29372D",
            zerolinecolor="#35463A"
        ),
        yaxis=dict(title="", gridcolor="rgba(0,0,0,0)"),
        margin=dict(l=5, r=30, t=10, b=10),
        height=300,
        showlegend=False,
    )

    st.plotly_chart(
        contribution_fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

    st.caption(
        "The index is calculated from your selected inputs "
        "and the stated weights. It is not a real-world "
        "disaster probability."
    )

# --------------------------------------------------
# TAB 3: RESPONSE PLANNER
# --------------------------------------------------

with tab3:
    st.subheader("Response Planning")
    st.markdown(
        '<div class="section-note">'
        'Explore preparedness actions associated with each zone. '
        'These are educational suggestions, not emergency orders.'
        '</div>',
        unsafe_allow_html=True
    )

    actions = {
        "Forest": [
            "Review official forest-fire alerts.",
            "Identify and protect safe evacuation routes.",
            "Coordinate with authorised forest-response teams."
        ],
        "Residential Area": [
            "Review official flood and severe-weather alerts.",
            "Identify safe routes and assembly points.",
            "Consider support for residents who may need assistance."
        ],
        "Hospital": [
            "Review backup-power readiness.",
            "Check continuity plans for essential services.",
            "Follow official emergency coordination procedures."
        ],
        "Smart Farm": [
            "Review water availability.",
            "Consider irrigation efficiency.",
            "Review crop-protection measures for expected conditions."
        ],
        "River & Dam": [
            "Monitor official water-level advisories.",
            "Follow authorised dam and water-management instructions.",
            "Use designated evacuation routes if instructed."
        ],
        "Industrial Zone": [
            "Follow facility safety procedures.",
            "Review relevant containment and shutdown plans.",
            "Contact authorised responders when necessary."
        ]
    }

    response_zone = st.selectbox(
        "Select a zone for its response plan",
        list(zones.keys()),
        key="response_zone"
    )

    response_score = calculate_risk(zones[response_zone])
    response_priority = classify_risk(response_score)
    response_colour = risk_colour(response_priority)

    st.write("")

    st.markdown(
        f"""<div class="metric-card">
        <div class="metric-label">Selected Zone</div>
        <div class="metric-value" style="font-size:23px">
        {response_zone}</div>
        <div style="margin-top:10px;color:{response_colour};
        font-weight:700;font-size:13px">
        {response_priority} &nbsp; · &nbsp;
        {response_score:.1f} / 100</div></div>""",
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown("#### Suggested Preparedness Actions")

    for i, action in enumerate(actions[response_zone], start=1):
        st.markdown(
            f"""<div style="background:#18221C;
            border:1px solid #35463A;border-radius:12px;
            padding:15px 17px;margin-bottom:10px;
            color:#D1D9CF">
            <span style="color:#A6C4A8;font-weight:800">
            {i:02d}</span>
            &nbsp;&nbsp; {action}</div>""",
            unsafe_allow_html=True
        )

# --------------------------------------------------
# TAB 4: METHODOLOGY AND AI
# --------------------------------------------------

with tab4:
    st.subheader("Methodology & Transparency")

    st.markdown(
        '<div class="section-note">'
        'TERA combines five weighted factors into an '
        'illustrative risk-priority index.</div>',
        unsafe_allow_html=True
    )

    st.markdown("#### Scoring Formula")

    st.latex(
        r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U"
    )

    method_df = pd.DataFrame({
        "Factor": factor_names,
        "Symbol": ["H", "V", "P", "E", "U"],
        "Weight": ["30%", "25%", "20%", "15%", "10%"],
    })

    st.dataframe(
        method_df,
        hide_index=True,
        use_container_width=True
    )

    st.markdown("#### Priority Thresholds")

    threshold_df = pd.DataFrame({
        "Classification": [
            "CRITICAL", "HIGH", "MODERATE", "LOWER"
        ],
        "Index Range": [
            "80–100", "65–79.99", "45–64.99", "Below 45"
        ],
    })

    st.dataframe(
        threshold_df,
        hide_index=True,
        use_container_width=True
    )

    st.markdown("#### Scientific Limitations")

    st.info(
        "TERA is an educational risk-prioritisation prototype. "
        "The built-in zone values are illustrative, not live "
        "sensor readings. The weighted index is a designed "
        "comparison score, not a calibrated disaster probability "
        "or validated real-world forecast. It should not replace "
        "official warnings, expert assessment, or authorised "
        "emergency decisions."
    )

    st.markdown("#### How to Interpret the Index")

    st.write(
        "A higher score means that a zone ranks higher under "
        "TERA's chosen inputs and weights. It does not prove "
        "that a disaster will occur there, nor does it establish "
        "the actual probability or severity of a future event."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown("""
<div class="footnote">
TERA 2.0 · TECHNOLOGY FOR ENVIRONMENTAL RISK ANALYSIS<br>
Educational prototype · Illustrative inputs ·
For preparedness awareness, not operational forecasting
</div>
""", unsafe_allow_html=True)
