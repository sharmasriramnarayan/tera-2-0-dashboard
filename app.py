
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="TERA 2.0 | Midnight Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# TERA 2.0 — MIDNIGHT INTELLIGENCE
# =========================================================

BG = "#07111F"
PANEL = "#0D1B2A"
BORDER = "#20384C"
WHITE = "#F1F8FF"
MUTED = "#91A8BC"
CYAN = "#43F5C5"
BLUE = "#52B7FF"
RED = "#FF5470"
ORANGE = "#FF9F43"
AMBER = "#FFD166"
GREEN = "#43F5C5"

RISK_COLORS = {
    "CRITICAL": RED,
    "HIGH": ORANGE,
    "MODERATE": AMBER,
    "LOWER": GREEN,
}

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
        "Inspect firebreaks and access routes",
        "Review dry vegetation and ignition precautions",
        "Check response teams and evacuation routes",
    ],
    "Residential Area": [
        "Review evacuation routes and public alerts",
        "Check emergency access and vulnerable households",
        "Review community preparedness plans",
    ],
    "Hospital": [
        "Verify backup power and emergency supplies",
        "Review patient evacuation procedures",
        "Keep emergency access routes clear",
    ],
    "Smart Farm": [
        "Inspect irrigation and water storage",
        "Review crop and weather vulnerabilities",
        "Review water conservation measures",
    ],
    "River & Dam": [
        "Review water-level monitoring procedures",
        "Check downstream warning arrangements",
        "Review drainage and evacuation plans",
    ],
    "Industrial Zone": [
        "Review hazardous-material storage procedures",
        "Check shutdown and spill-response plans",
        "Review worker alerts and emergency access",
    ],
}

# ---------------------- STYLE ----------------------------

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {{
    background:
      radial-gradient(ellipse at 90% 0%, rgba(67,245,197,.08), transparent 35%),
      radial-gradient(ellipse at 0% 40%, rgba(82,183,255,.06), transparent 30%),
      {BG};
    color: {WHITE};
    font-family: Inter, sans-serif;
}}
[data-testid="stHeader"] {{ background: rgba(7,17,31,.9); }}
[data-testid="stSidebar"] {{
    background: #091523;
    border-right: 1px solid {BORDER};
}}
[data-testid="stSidebar"] * {{ color: #DCEAF5; }}
h1, h2, h3 {{
    color: {WHITE} !important;
    font-family: 'Space Grotesk', sans-serif !important;
}}
p, label {{ color: {MUTED}; }}
.hero {{
    background: linear-gradient(120deg, #0D1D2D, #102D40 60%, #0B3A3A);
    border: 1px solid #245165;
    border-radius: 22px;
    padding: 30px;
    margin-bottom: 20px;
    box-shadow: 0 12px 35px rgba(0,0,0,.16);
}}
.eyebrow {{
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 3px;
    color: {CYAN};
}}
.hero-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(38px, 6vw, 65px);
    font-weight: 700;
    line-height: 1.05;
    margin: 13px 0;
    color: white;
}}
.hero-title span {{ color: {CYAN}; }}
.hero-copy {{
    max-width: 680px;
    color: #B9CEDD;
    font-size: 14px;
    line-height: 1.8;
}}
.pill {{
    display: inline-block;
    padding: 7px 11px;
    border: 1px solid #28675E;
    border-radius: 6px;
    background: rgba(67,245,197,.07);
    color: {CYAN};
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    margin-top: 14px;
}}
.kicker {{
    color: {CYAN};
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2.2px;
    margin-top: 13px;
}}
.metric-card {{
    background: linear-gradient(145deg, {PANEL}, #0A1725);
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 17px;
    min-height: 105px;
}}
.metric-label {{
    color: {MUTED};
    font-size: 10px;
    letter-spacing: 1.4px;
    font-weight: 800;
}}
.metric-value {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 30px;
    font-weight: 800;
    margin-top: 9px;
}}
.panel {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 19px;
    margin: 8px 0 15px;
}}
.note {{
    background: #102C32;
    border: 1px solid #24584F;
    border-left: 4px solid {CYAN};
    border-radius: 8px;
    padding: 12px 15px;
    color: #C0DED9;
    font-size: 12px;
    line-height: 1.7;
}}
div.stButton > button {{
    background: {CYAN};
    color: #041711;
    border: 1px solid {CYAN};
    border-radius: 8px;
    min-height: 42px;
    font-weight: 800;
}}
div.stButton > button:hover {{
    background: #B1FFE8;
    color: #041711;
}}
[data-testid="stMetric"] {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 14px;
}}
[data-testid="stMetricLabel"] {{ color: {MUTED}; }}
[data-testid="stMetricValue"] {{ color: {WHITE}; }}
[data-baseweb="select"] > div,
[data-baseweb="input"] > div {{
    background: #102437;
    border-color: {BORDER};
}}
hr {{ border-color: {BORDER}; }}
footer, #MainMenu {{ visibility: hidden; }}
</style>
""", unsafe_allow_html=True)


# ---------------------- HELPERS --------------------------

def score(values):
    return round(
        sum(values[i] * WEIGHTS[FACTORS[i]]
            for i in range(len(FACTORS))),
        1,
    )


def band(value):
    if value >= 80:
        return "CRITICAL"
    if value >= 65:
        return "HIGH"
    if value >= 45:
        return "MODERATE"
    return "LOWER"


def section(kicker, title, caption=None):
    st.markdown(f'<div class="kicker">{kicker}</div>',
                unsafe_allow_html=True)
    st.subheader(title)
    if caption:
        st.caption(caption)


def metric_card(label, value, color):
    st.markdown(f"""
    <div class="metric-card" style="border-top:3px solid {color}">
      <div class="metric-label">{label}</div>
      <div class="metric-value" style="color:{color}">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def risk_bar(label, value, color):
    value = max(0, min(100, float(value)))
    st.markdown(f"""
    <div style="margin:13px 0">
      <div style="display:flex;justify-content:space-between;
                  margin-bottom:6px;gap:10px">
        <span style="font-size:12px;color:#D8E7F2">{label}</span>
        <b style="font-size:12px;color:{color}">{value:.1f}</b>
      </div>
      <div style="height:7px;background:#203447;border-radius:10px;
                  overflow:hidden">
        <div style="width:{value}%;height:7px;background:{color};
                    border-radius:10px"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def style_chart(fig, height=340):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=WHITE, family="Inter"),
        margin=dict(l=15, r=15, t=35, b=15),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color=WHITE),
        ),
        hoverlabel=dict(
            bgcolor="#102437",
            font_color=WHITE,
        ),
    )
    return fig


# ---------------------- SIDEBAR --------------------------

st.sidebar.markdown(f"""
<div style="padding:10px 3px 18px">
  <div style="font-family:'Space Grotesk',sans-serif;
              font-size:28px;font-weight:800;color:white">
    TERA<span style="color:{CYAN}">.2</span>
  </div>
  <div style="font-size:10px;letter-spacing:2px;
              font-weight:800;color:{CYAN}">
    MIDNIGHT INTELLIGENCE
  </div>
  <div style="font-size:10px;color:{MUTED};margin-top:8px">
    ENVIRONMENTAL RISK SYSTEM
  </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Command Centre",
        "Zone Intelligence",
        "Risk Simulator",
        "Response Planner",
        "Methodology & AI",
    ],
)
st.sidebar.markdown("---")
st.sidebar.success("SCORING ENGINE READY")
st.sidebar.caption("Illustrative demonstration data")
st.sidebar.caption("No live sensors connected")


# ---------------------- CALCULATIONS ---------------------

results = []
for zone, values in ZONES.items():
    value = score(values)
    results.append({
        "Zone": zone,
        "Score": value,
        "Band": band(value),
        "Values": values,
    })

results.sort(key=lambda item: item["Score"], reverse=True)

counts = {
    level: sum(item["Band"] == level for item in results)
    for level in ["CRITICAL", "HIGH", "MODERATE", "LOWER"]
}

top = results[0]
average = round(sum(item["Score"] for item in results) / len(results), 1)

# ---------------------- HERO -----------------------------

st.markdown(f"""
<div class="hero">
  <div class="eyebrow">ENVIRONMENTAL INTELLIGENCE / COMMAND INTERFACE</div>
  <div class="hero-title">MIDNIGHT <span>INTELLIGENCE</span></div>
  <div class="hero-copy">
    See the signals. Explore the risks. Prioritise the response.
    An interactive environmental risk analysis prototype.
  </div>
  <div class="pill">● TERA 2.0 &nbsp; / &nbsp; INTERACTIVE DEMONSTRATION</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# COMMAND CENTRE
# =========================================================

if page == "Command Centre":

    section("01 / OVERVIEW", "Environmental Command Centre",
            "One glance. Six zones. A transparent priority model.")

    cols = st.columns(4)
    cards = [
        ("ZONES ANALYSED", "06", CYAN),
        ("CRITICAL", str(counts["CRITICAL"]), RED),
        ("HIGH PRIORITY", str(counts["HIGH"]), ORANGE),
        ("MEAN INDEX", str(average), BLUE),
    ]

    for col, (label, value, color) in zip(cols, cards):
        with col:
            metric_card(label, value, color)

    st.markdown("")
    left, right = st.columns([1.05, 1])

    with left:
        section("02 / RISK DISTRIBUTION", "Priority Mix")
        pie_labels = [name.title() for name in counts.keys()]
        pie_values = list(counts.values())
        pie_colors = [RISK_COLORS[name] for name in counts.keys()]

        fig = go.Figure(data=[go.Pie(
            labels=pie_labels,
            values=pie_values,
            hole=0.68,
            sort=False,
            marker=dict(
                colors=pie_colors,
                line=dict(color=BG, width=4),
            ),
            textinfo="percent",
            textfont=dict(size=13, color=WHITE),
            hovertemplate="%{label}<br>%{value} zone(s)<br>%{percent}<extra></extra>",
        )])
        fig.update_layout(
            annotations=[dict(
                text=f"<b>{len(results)}</b><br><span style='font-size:11px'>ZONES</span>",
                x=.5, y=.5, showarrow=False,
                font=dict(size=25, color=WHITE),
            )],
        )
        st.plotly_chart(style_chart(fig, 340), use_container_width=True)

    with right:
        section("03 / COMPARATIVE VIEW", "Zone Risk Scores")
        fig = go.Figure()
        ordered = list(reversed(results))
        fig.add_trace(go.Bar(
            x=[item["Score"] for item in ordered],
            y=[item["Zone"] for item in ordered],
            orientation="h",
            marker=dict(
                color=[RISK_COLORS[item["Band"]] for item in ordered],
                line=dict(color=BG, width=1),
            ),
            text=[str(item["Score"]) for item in ordered],
            textposition="outside",
            hovertemplate="%{y}<br>Index: %{x}<extra></extra>",
        ))
        fig.update_xaxes(
            range=[0, 112],
            title="Weighted priority index",
            gridcolor="#203447",
        )
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(style_chart(fig, 340), use_container_width=True)

    section("04 / PRIORITY ENGINE", "Zone Ranking")

    for rank, item in enumerate(results, start=1):
        color = RISK_COLORS[item["Band"]]
        with st.container(border=True):
            c1, c2, c3 = st.columns([.55, 4.5, 1.3])
            with c1:
                st.markdown(
                    f"<h3 style='color:{CYAN};margin-top:8px'>{rank:02}</h3>",
                    unsafe_allow_html=True,
                )
            with c2:
                st.markdown(f"**{item['Zone']}**")
                risk_bar("PRIORITY INDEX", item["Score"], color)
            with c3:
                st.markdown(
                    f"<div style='margin-top:12px;color:{color};"
                    f"font-weight:800;font-size:11px'>{item['Band']}</div>",
                    unsafe_allow_html=True,
                )
                st.caption(f"{item['Score']} / 100")

    top_color = RISK_COLORS[top["Band"]]
    st.markdown(f"""
    <div class="panel" style="border-left:4px solid {top_color}">
      <div class="kicker">MODEL INSIGHT / HIGHEST CURRENT SCORE</div>
      <h2 style="margin:10px 0;color:{WHITE}">{top['Zone']}</h2>
      <div style="font-size:27px;font-weight:800;color:{top_color}">
        {top['Score']} <span style="font-size:13px;color:{MUTED}">
        / 100 · {top['Band']}</span>
      </div>
      <p>Suggested focus for review under the current model assumptions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="note">
      <b>MODEL TRANSPARENCY</b><br>
      Scores are illustrative weighted priority indices. They are not
      disaster probabilities, verified forecasts, or live measurements.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ZONE INTELLIGENCE
# =========================================================

elif page == "Zone Intelligence":

    section("02 / EXPLORER", "Zone Intelligence",
            "Select a zone to inspect its indicator profile.")

    selected_zone = st.selectbox("SELECT A ZONE", list(ZONES.keys()))
    values = ZONES[selected_zone]
    current_score = score(values)
    current_band = band(current_score)
    color = RISK_COLORS[current_band]

    c1, c2, c3 = st.columns(3)
    with c1:
        metric_card("SELECTED ZONE", selected_zone, CYAN)
    with c2:
        metric_card("PRIORITY INDEX", str(current_score), color)
    with c3:
        metric_card("CLASSIFICATION", current_band, color)

    left, right = st.columns([1.1, 1])

    with left:
        section("INDICATOR PROFILE", "Environmental Factor Radar")
        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(
            r=values + [values[0]],
            theta=FACTORS + [FACTORS[0]],
            fill="toself",
            fillcolor="rgba(67,245,197,0.17)",
            line=dict(color=CYAN, width=3),
            name=selected_zone,
            hovertemplate="%{theta}: %{r}<extra></extra>",
        ))
        radar.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor="#294156",
                    linecolor="#294156",
                    tickfont=dict(color=MUTED, size=9),
                ),
                angularaxis=dict(
                    gridcolor="#294156",
                    linecolor="#294156",
                    tickfont=dict(color=WHITE, size=10),
                ),
            ),
            showlegend=False,
        )
        st.plotly_chart(style_chart(radar, 390), use_container_width=True)

    with right:
        section("WEIGHT CONTRIBUTION", "Factor Breakdown")
        contributions = [
            round(values[i] * WEIGHTS[factor], 2)
            for i, factor in enumerate(FACTORS)
        ]
        fig = go.Figure(go.Bar(
            x=contributions,
            y=FACTORS,
            orientation="h",
            marker_color=[CYAN, BLUE, "#8B7CFF", ORANGE, AMBER],
            hovertemplate="%{y}<br>Weighted contribution: %{x}<extra></extra>",
        ))
        fig.update_xaxes(title="Contribution to index", gridcolor="#203447")
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(style_chart(fig, 390), use_container_width=True)

    section("INTERPRETATION", "What the indicators show")
    for i, factor in enumerate(FACTORS):
        risk_bar(
            f"{factor.upper()} · WEIGHT {WEIGHTS[factor] * 100:.0f}%",
            values[i],
            [CYAN, BLUE, "#8B7CFF", ORANGE, AMBER][i],
        )

    st.info(
        "Indicator values are manually supplied demonstration inputs. "
        "They do not represent measured conditions in this zone."
    )


# =========================================================
# RISK SIMULATOR
# =========================================================

elif page == "Risk Simulator":

    section("03 / INTERACTIVE LAB", "Risk Simulator",
            "Move a slider and watch the score and charts update.")

    st.markdown("""
    <div class="note">
      <b>YOUR CONTROLS. YOUR SCENARIO.</b><br>
      Explore how changing an input affects the weighted index.
    </div>
    """, unsafe_allow_html=True)

    selected_zone = st.selectbox("CHOOSE ZONE", list(ZONES.keys()))
    original = ZONES[selected_zone]
    simulated = []

    left, right = st.columns(2)
    for i, factor in enumerate(FACTORS):
        target = left if i % 2 == 0 else right
        with target:
            value = st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(original[i]),
                key=f"sim_{selected_zone}_{factor}",
            )
            st.caption(f"MODEL WEIGHT: {WEIGHTS[factor] * 100:.0f}%")
            simulated.append(value)

    base = score(original)
    new_score = score(simulated)
    change = round(new_score - base, 1)
    new_band = band(new_score)
    color = RISK_COLORS[new_band]

    st.markdown("---")
    section("SIMULATION OUTPUT", "Instant Model Response")

    a, b, c = st.columns(3)
    a.metric("BASELINE INDEX", f"{base}/100")
    b.metric("SIMULATED INDEX", f"{new_score}/100", delta=f"{change:+.1f}")
    with c:
        metric_card("NEW PRIORITY BAND", new_band, color)

    left, right = st.columns(2)
    with left:
        section("BEFORE VS AFTER", "Score Comparison")
        fig = go.Figure(go.Bar(
            x=["Baseline", "Simulation"],
            y=[base, new_score],
            marker_color=[BLUE, color],
            text=[base, new_score],
            textposition="outside",
        ))
        fig.update_yaxes(range=[0, 112], title="Index", gridcolor="#203447")
        st.plotly_chart(style_chart(fig, 320), use_container_width=True)

    with right:
        section("INPUT CHANGES", "Factor Profile")
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=original + [original[0]],
            theta=FACTORS + [FACTORS[0]],
            name="Baseline",
            line=dict(color=BLUE, dash="dash", width=2),
        ))
        fig.add_trace(go.Scatterpolar(
            r=simulated + [simulated[0]],
            theta=FACTORS + [FACTORS[0]],
            name="Simulation",
            fill="toself",
            fillcolor="rgba(67,245,197,.10)",
            line=dict(color=CYAN, width=3),
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(range=[0, 100], gridcolor="#294156"),
                angularaxis=dict(gridcolor="#294156"),
            ),
        )
        st.plotly_chart(style_chart(fig, 320), use_container_width=True)

    if new_score >= 80:
        st.error("CRITICAL BAND — review preparedness and mitigation priorities.")
    elif new_score >= 65:
        st.warning("HIGH PRIORITY — review preventive measures and readiness.")
    elif new_score >= 45:
        st.info("MODERATE PRIORITY — continue monitoring and preventive review.")
    else:
        st.success("LOWER PRIORITY BAND — maintain appropriate routine preparedness.")

    st.caption(
        "The simulation is mathematical, not predictive. It uses illustrative "
        "values and does not assess actual environmental conditions."
    )


# =========================================================
# RESPONSE PLANNER
# =========================================================

elif page == "Response Planner":

    section("04 / ACTION WORKSPACE", "Response Planning Desk",
            "Turn the model result into a structured preparedness discussion.")

    selected_zone = st.selectbox(
        "SELECT ZONE",
        [item["Zone"] for item in results],
        key="planner_zone",
    )
    item = next(x for x in results if x["Zone"] == selected_zone)
    color = RISK_COLORS[item["Band"]]

    metric_card(
        f"{selected_zone.upper()} / MODEL INDEX",
        f"{item['Score']} · {item['Band']}",
        color,
    )

    st.markdown("### Preparedness Checklist")
    st.caption("General planning suggestions; not official emergency instructions.")

    for i, action in enumerate(ACTIONS[selected_zone]):
        st.checkbox(action, key=f"check_{selected_zone}_{i}")

    notes = st.text_area(
        "Planning notes",
        placeholder="Observations, responsible persons, next steps...",
        height=120,
    )

    if st.button("GENERATE PLANNING SUMMARY"):
        st.markdown("---")
        st.subheader("Planning Summary")
        st.write(f"**Zone:** {selected_zone}")
        st.write(f"**Model index:** {item['Score']}/100")
        st.write(f"**Band:** {item['Band']}")

        for i, action in enumerate(ACTIONS[selected_zone]):
            done = st.session_state.get(
                f"check_{selected_zone}_{i}", False
            )
            st.write(f"{'✓ REVIEWED' if done else '○ PENDING'} — {action}")

        st.write("**Notes:**", notes.strip() or "No notes entered.")
        st.caption("Planning aid only; not an operational response plan.")


# =========================================================
# METHODOLOGY
# =========================================================

elif page == "Methodology & AI":

    section("05 / TRANSPARENCY", "Methodology & AI",
            "A transparent formula is part of responsible environmental technology.")

    st.markdown("### Weighted Priority Formula")
    st.latex(r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U")

    factor_info = [
        ("Hazard", 30, "Illustrative hazard-severity indicator."),
        ("Vulnerability", 25, "Illustrative susceptibility to harm."),
        ("Population", 20, "Illustrative concentration of people potentially affected."),
        ("Exposure", 15, "Illustrative extent of people or assets in harm's way."),
        ("Urgency", 10, "Illustrative need for timely review."),
    ]

    for name, weight, description in factor_info:
        with st.container(border=True):
            a, b = st.columns([1.4, 4])
            with a:
                st.markdown(f"**{name} · {weight}%**")
            with b:
                st.caption(description)

    st.markdown("### Risk Classification")
    for level, interval in [
        ("CRITICAL", "80–100"),
        ("HIGH", "65–79.9"),
        ("MODERATE", "45–64.9"),
        ("LOWER", "Below 45"),
    ]:
        color = RISK_COLORS[level]
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;
                    padding:12px;margin:7px 0;background:{PANEL};
                    border:1px solid {BORDER};border-left:4px solid {color};
                    border-radius:8px">
          <b style="color:{color}">{level}</b>
          <b style="color:{WHITE}">{interval}</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### How TERA Works")
    steps = [
        ("01", "INPUT", "Supply illustrative indicators."),
        ("02", "CALCULATE", "Apply the weighted formula."),
        ("03", "CLASSIFY", "Assign a priority category."),
        ("04", "PLAN", "Explore preparedness actions."),
        ("05", "VERIFY", "Validate data and assumptions with experts."),
    ]
    for number, title, description in steps:
        with st.container(border=True):
            a, b = st.columns([.6, 5])
            with a:
                st.markdown(
                    f"<h3 style='color:{CYAN}'>{number}</h3>",
                    unsafe_allow_html=True,
                )
            with b:
                st.markdown(f"**{title}**")
                st.caption(description)

    st.warning(
        "Scientific limitation: this prototype uses illustrative manually "
        "entered data and a rule-based weighted formula. It does not currently "
        "train a machine-learning model, connect to live sensors, ingest live "
        "satellite data, or predict disasters. The score is not a probability. "
        "Real-world deployment requires validated data, justified weights, "
        "expert review, calibration, and field testing."
    )


# ---------------------- FOOTER ---------------------------

st.markdown("---")
st.markdown(f"""
<div style="text-align:center;padding:18px 0">
  <div style="font-family:'Space Grotesk',sans-serif;font-size:23px;
              font-weight:800;color:white">
    TERA<span style="color:{CYAN}"> 2.0</span>
  </div>
  <div style="font-size:10px;letter-spacing:2px;color:{MUTED};
              margin-top:7px">
    TECHNOLOGY FOR ENVIRONMENTAL RISK ANALYSIS
  </div>
  <div style="font-size:10px;color:{MUTED};margin-top:12px">
    MIDNIGHT INTELLIGENCE / STUDENT PROTOTYPE
  </div>
</div>
""", unsafe_allow_html=True)
