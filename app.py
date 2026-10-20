
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from io import StringIO

st.set_page_config(
    page_title="TERA 2.0 | Midnight Intelligence Edition",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# TERA 2.0 — MIDNIGHT INTELLIGENCE EDITION
# ==========================================================

BG = "#070D18"
PANEL = "#101B2B"
BORDER = "#26374D"
WHITE = "#F4F8FF"
MUTED = "#9BAFC5"
CYAN = "#42F5C5"
BLUE = "#59B8FF"
PURPLE = "#A78BFA"
RED = "#FF5874"
ORANGE = "#FFAA55"
YELLOW = "#FFE082"

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
        "Review firebreaks and access routes",
        "Inspect dry vegetation and fire precautions",
        "Review emergency access and warning plans",
    ],
    "Residential Area": [
        "Review evacuation routes and public alerts",
        "Check access for emergency services",
        "Review community preparedness",
    ],
    "Hospital": [
        "Review backup power and emergency supplies",
        "Check patient evacuation procedures",
        "Keep emergency access routes clear",
    ],
    "Smart Farm": [
        "Review irrigation and water storage",
        "Inspect crop and weather vulnerabilities",
        "Review water conservation measures",
    ],
    "River & Dam": [
        "Review water-level monitoring procedures",
        "Check downstream warning arrangements",
        "Review drainage and evacuation plans",
    ],
    "Industrial Zone": [
        "Review hazardous-material safety procedures",
        "Check shutdown and spill-response plans",
        "Review worker alerts and emergency access",
    ],
}

RISK_COLORS = {
    "CRITICAL": RED,
    "HIGH": ORANGE,
    "MODERATE": YELLOW,
    "LOWER": CYAN,
}

# --------------------- VISUAL DESIGN -----------------------

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {{
    background:
      radial-gradient(ellipse at 90% 0%, #12352F 0%, transparent 28%),
      radial-gradient(ellipse at 0% 35%, #172342 0%, transparent 30%),
      {BG};
    color: {WHITE};
    font-family: Inter, sans-serif;
}}
[data-testid="stHeader"] {{background:rgba(7,13,24,.85);}}
[data-testid="stSidebar"] {{
    background:#0A1321;
    border-right:1px solid {BORDER};
}}
[data-testid="stSidebar"] * {{color:{WHITE};}}
h1,h2,h3 {{
    color:{WHITE} !important;
    font-family:'Space Grotesk',sans-serif !important;
}}
p,label {{color:{MUTED};}}
.hero {{
    background:linear-gradient(120deg,#101B2B,#102A3A 60%,#103A35);
    border:1px solid #28564F;
    border-radius:22px;
    padding:30px;
    margin-bottom:22px;
    box-shadow:0 15px 55px rgba(0,0,0,.24);
}}
.eyebrow {{
    color:{CYAN};
    font-size:10px;
    letter-spacing:3px;
    font-weight:800;
}}
.hero-title {{
    font-family:'Space Grotesk',sans-serif;
    font-size:clamp(34px,5.5vw,65px);
    line-height:1.05;
    font-weight:700;
    margin:14px 0;
    color:#FFFFFF;
}}
.hero-title span {{color:{CYAN};}}
.hero-copy {{
    color:#C1D0E0;
    max-width:700px;
    line-height:1.8;
    font-size:14px;
}}
.edition {{
    display:inline-block;
    margin-top:15px;
    border:1px solid #357B6C;
    background:#102F2C;
    border-radius:7px;
    padding:8px 12px;
    color:{CYAN};
    font-size:10px;
    letter-spacing:2px;
    font-weight:800;
}}
.kicker {{
    font-size:10px;
    color:{CYAN};
    letter-spacing:2.5px;
    font-weight:800;
    margin-top:12px;
}}
.metric-card {{
    background:linear-gradient(145deg,#132137,#0D1726);
    border:1px solid {BORDER};
    border-radius:15px;
    padding:17px;
    min-height:105px;
}}
.metric-label {{
    color:{MUTED};
    font-size:10px;
    font-weight:800;
    letter-spacing:1.3px;
}}
.metric-value {{
    font-family:'Space Grotesk',sans-serif;
    font-size:29px;
    font-weight:700;
    margin-top:9px;
    overflow-wrap:anywhere;
}}
.panel {{
    background:{PANEL};
    border:1px solid {BORDER};
    border-radius:14px;
    padding:18px;
    margin:8px 0 16px;
}}
.note {{
    background:#10282B;
    border:1px solid #28554E;
    border-left:4px solid {CYAN};
    padding:13px 16px;
    border-radius:8px;
    font-size:12px;
    line-height:1.8;
    color:#C4E2DB;
}}
div.stButton > button {{
    background:{CYAN};
    color:#061610;
    border:1px solid {CYAN};
    border-radius:9px;
    min-height:42px;
    font-weight:800;
}}
div.stButton > button:hover {{
    background:#C1FFED;
    color:#061610;
    border-color:#C1FFED;
}}
[data-testid="stMetric"] {{
    background:{PANEL};
    border:1px solid {BORDER};
    border-radius:12px;
    padding:13px;
}}
[data-testid="stMetricLabel"] {{color:{MUTED};}}
[data-testid="stMetricValue"] {{color:{WHITE};}}
[data-baseweb="select"] > div,
[data-baseweb="input"] > div {{
    background:#122137;
    border-color:{BORDER};
}}
hr {{border-color:{BORDER};}}
footer,#MainMenu {{visibility:hidden;}}
</style>
""", unsafe_allow_html=True)


# --------------------- MODEL FUNCTIONS ---------------------

def calculate_score(values):
    return round(
        sum(values[i] * WEIGHTS[FACTORS[i]] for i in range(5)),
        1,
    )


def classify(value):
    if value >= 80:
        return "CRITICAL"
    if value >= 65:
        return "HIGH"
    if value >= 45:
        return "MODERATE"
    return "LOWER"


def get_results():
    output = []
    for zone, values in ZONES.items():
        s = calculate_score(values)
        output.append({
            "Zone": zone,
            "Score": s,
            "Band": classify(s),
            **{FACTORS[i]: values[i] for i in range(5)},
        })
    return pd.DataFrame(output).sort_values(
        "Score", ascending=False
    ).reset_index(drop=True)


def heading(kicker, title, caption=None):
    st.markdown(
        f'<div class="kicker">{kicker}</div>',
        unsafe_allow_html=True,
    )
    st.subheader(title)
    if caption:
        st.caption(caption)


def metric_card(label, value, color=CYAN):
    st.markdown(f"""
    <div class="metric-card" style="border-top:3px solid {color}">
      <div class="metric-label">{label}</div>
      <div class="metric-value" style="color:{color}">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def make_chart(fig, height=350):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=WHITE, family="Inter"),
        margin=dict(l=15, r=20, t=35, b=15),
        hoverlabel=dict(
            bgcolor="#17263A",
            font_color=WHITE,
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color=WHITE),
        ),
    )
    return fig


def risk_bar(label, value, color):
    value = max(0, min(100, float(value)))
    st.markdown(f"""
    <div style="margin:13px 0">
      <div style="display:flex;justify-content:space-between;
                  margin-bottom:6px">
        <span style="color:#D6E2EF;font-size:12px">{label}</span>
        <b style="color:{color};font-size:12px">{value:.1f}</b>
      </div>
      <div style="height:7px;background:#26374D;border-radius:8px">
        <div style="width:{value}%;height:7px;background:{color};
                    border-radius:8px"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# --------------------- SIDEBAR ----------------------------

st.sidebar.markdown(f"""
<div style="padding:10px 2px 18px">
  <div style="font-size:30px;font-weight:800;
              font-family:'Space Grotesk',sans-serif">
    TERA<span style="color:{CYAN}">.2</span>
  </div>
  <div style="font-size:10px;letter-spacing:2px;
              color:{CYAN};font-weight:800">
    MIDNIGHT INTELLIGENCE
  </div>
  <div style="font-size:10px;color:{MUTED};margin-top:7px">
    SIGNATURE EDITION
  </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "COMMAND NAVIGATION",
    [
        "Command Centre",
        "Zone Intelligence",
        "Compare Zones",
        "Scenario Lab",
        "Mission Control",
        "Methodology",
    ],
)
st.sidebar.markdown("---")
st.sidebar.markdown("**SYSTEM STATUS**")
st.sidebar.success("Weighted scoring engine ready")
st.sidebar.caption("Demo dataset · No live sensors")
st.sidebar.caption("Student environmental prototype")

# --------------------- HERO BANNER -------------------------

st.markdown(f"""
<div class="hero">
  <div class="eyebrow">TERA 2.0 / ENVIRONMENTAL INTELLIGENCE</div>
  <div class="hero-title">MIDNIGHT <span>INTELLIGENCE</span></div>
  <div class="hero-copy">
    See the signals. Understand the risks. Prioritise the response.
    Explore an interactive environmental risk analysis prototype
    designed to turn indicators into structured preparedness discussions.
  </div>
  <div class="edition">✦ THE SIGNATURE EDITION ✦</div>
</div>
""", unsafe_allow_html=True)

df = get_results()
counts = df["Band"].value_counts().reindex(
    ["CRITICAL", "HIGH", "MODERATE", "LOWER"], fill_value=0
)
average = round(df["Score"].mean(), 1)
top = df.iloc[0]

# ==========================================================
# 1. COMMAND CENTRE
# ==========================================================

if page == "Command Centre":

    heading(
        "01 / GLOBAL OVERVIEW",
        "Environmental Command Centre",
        "Six zones · Five weighted indicators · One transparent model",
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("ZONES ANALYSED", "06", CYAN)
    with c2:
        metric_card("CRITICAL BAND", str(counts["CRITICAL"]), RED)
    with c3:
        metric_card("HIGH BAND", str(counts["HIGH"]), ORANGE)
    with c4:
        metric_card("MEAN INDEX", str(average), BLUE)

    st.write("")
    left, right = st.columns([1, 1.15])

    with left:
        heading("02 / DISTRIBUTION", "Risk Classification Mix")
        fig = go.Figure(go.Pie(
            labels=[x.title() for x in counts.index],
            values=counts.values,
            hole=0.68,
            sort=False,
            marker=dict(
                colors=[RISK_COLORS[x] for x in counts.index],
                line=dict(color=BG, width=4),
            ),
            textinfo="percent",
            hovertemplate="%{label}<br>%{value} zone(s)<br>%{percent}<extra></extra>",
        ))
        fig.update_layout(
            annotations=[dict(
                text=f"<b>{len(df)}</b><br><span style='font-size:11px'>ZONES</span>",
                x=.5, y=.5, showarrow=False,
                font=dict(size=25, color=WHITE),
            )]
        )
        st.plotly_chart(make_chart(fig, 340), use_container_width=True)

    with right:
        heading("03 / RANKING", "Environmental Priority Index")
        fig = go.Figure(go.Bar(
            x=df["Score"],
            y=df["Zone"],
            orientation="h",
            marker_color=[RISK_COLORS[x] for x in df["Band"]],
            text=df["Score"],
            textposition="outside",
            hovertemplate="%{y}<br>Index: %{x}<extra></extra>",
        ))
        fig.update_layout(yaxis=dict(autorange="reversed"))
        fig.update_xaxes(range=[0, 112], gridcolor=BORDER, title="Weighted index")
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(make_chart(fig, 340), use_container_width=True)

    heading("04 / MODEL INSIGHT", "Priority Spotlight")

    color = RISK_COLORS[top["Band"]]
    st.markdown(f"""
    <div class="panel" style="border-left:4px solid {color}">
      <div class="kicker">HIGHEST SCORE IN CURRENT DEMONSTRATION</div>
      <h2 style="margin:10px 0">{top['Zone']}</h2>
      <div style="font-size:30px;font-weight:800;color:{color}">
        {top['Score']} <span style="font-size:13px;color:{MUTED}">
        / 100 · {top['Band']}</span>
      </div>
      <p>This identifies the highest score under the current inputs and
      weights. It does not establish that this zone is experiencing an
      actual emergency.</p>
    </div>
    """, unsafe_allow_html=True)

    heading("05 / ALL ZONES", "Explore the Rankings")
    selected = st.selectbox(
        "Choose a zone to inspect",
        df["Zone"].tolist(),
        key="command_zone",
    )
    selected_row = df[df["Zone"] == selected].iloc[0]
    st.write(
        f"**{selected}** — index **{selected_row['Score']}**, "
        f"classification **{selected_row['Band']}**."
    )
    if st.button("OPEN ZONE INTELLIGENCE"):
        st.session_state["selected_zone"] = selected
        st.session_state["jump_zone"] = True
        st.info("Choose Zone Intelligence from the sidebar to explore this zone.")

    st.markdown("""
    <div class="note">
      <b>SCIENTIFIC NOTE</b><br>
      These are illustrative weighted priority indices, not real-time
      environmental measurements, disaster probabilities, or validated forecasts.
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# 2. ZONE INTELLIGENCE
# ==========================================================

elif page == "Zone Intelligence":

    heading(
        "02 / DEEP DIVE",
        "Zone Intelligence",
        "Inspect the factor profile and understand what contributes to a score.",
    )

    default_zone = st.session_state.get("selected_zone", "Forest")
    zone_list = list(ZONES.keys())
    index = zone_list.index(default_zone) if default_zone in zone_list else 0

    zone = st.selectbox("SELECT ENVIRONMENTAL ZONE", zone_list, index=index)
    vals = ZONES[zone]
    s = calculate_score(vals)
    level = classify(s)
    color = RISK_COLORS[level]

    a, b, c = st.columns(3)
    with a:
        metric_card("SELECTED ZONE", zone, CYAN)
    with b:
        metric_card("WEIGHTED INDEX", str(s), color)
    with c:
        metric_card("CLASSIFICATION", level, color)

    left, right = st.columns(2)

    with left:
        heading("FACTOR SIGNATURE", "Radar Profile")
        fig = go.Figure(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=FACTORS + [FACTORS[0]],
            fill="toself",
            fillcolor="rgba(66,245,197,.15)",
            line=dict(color=CYAN, width=3),
            name=zone,
            hovertemplate="%{theta}: %{r}<extra></extra>",
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True, range=[0, 100],
                    gridcolor=BORDER, tickfont=dict(color=MUTED),
                ),
                angularaxis=dict(
                    gridcolor=BORDER, tickfont=dict(color=WHITE),
                ),
            ),
            showlegend=False,
        )
        st.plotly_chart(make_chart(fig, 390), use_container_width=True)

    with right:
        heading("WEIGHTED CONTRIBUTION", "What Drives the Score?")
        contribution = [vals[i] * WEIGHTS[FACTORS[i]] for i in range(5)]
        fig = go.Figure(go.Bar(
            x=contribution,
            y=FACTORS,
            orientation="h",
            marker_color=[CYAN, BLUE, PURPLE, ORANGE, YELLOW],
            hovertemplate="%{y}<br>Contribution: %{x:.2f}<extra></extra>",
        ))
        fig.update_xaxes(title="Weighted contribution", gridcolor=BORDER)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(make_chart(fig, 390), use_container_width=True)

    heading("INDICATOR READOUT", "Factor-by-Factor Breakdown")
    for i, factor in enumerate(FACTORS):
        risk_bar(
            f"{factor.upper()} · WEIGHT {WEIGHTS[factor]*100:.0f}%",
            vals[i],
            [CYAN, BLUE, PURPLE, ORANGE, YELLOW][i],
        )

    st.caption(
        "All factor values are illustrative inputs. A high factor score "
        "does not independently prove that a hazard is occurring."
    )


# ==========================================================
# 3. COMPARE ZONES
# ==========================================================

elif page == "Compare Zones":

    heading(
        "03 / COMPARISON STUDIO",
        "Compare Two Zones",
        "Explore differences between environmental profiles.",
    )

    col1, col2 = st.columns(2)
    with col1:
        zone_a = st.selectbox("ZONE A", list(ZONES.keys()), index=0)
    with col2:
        zone_b = st.selectbox("ZONE B", list(ZONES.keys()), index=1)

    if zone_a == zone_b:
        st.warning("Select two different zones to make a comparison.")
    else:
        vals_a = ZONES[zone_a]
        vals_b = ZONES[zone_b]
        score_a = calculate_score(vals_a)
        score_b = calculate_score(vals_b)

        left, right = st.columns(2)
        with left:
            metric_card(zone_a.upper(), f"{score_a} / 100", RISK_COLORS[classify(score_a)])
        with right:
            metric_card(zone_b.upper(), f"{score_b} / 100", RISK_COLORS[classify(score_b)])

        heading("PROFILE OVERLAY", "Radar Comparison")
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=vals_a + [vals_a[0]],
            theta=FACTORS + [FACTORS[0]],
            fill="toself",
            name=zone_a,
            line=dict(color=CYAN, width=3),
            fillcolor="rgba(66,245,197,.09)",
        ))
        fig.add_trace(go.Scatterpolar(
            r=vals_b + [vals_b[0]],
            theta=FACTORS + [FACTORS[0]],
            fill="toself",
            name=zone_b,
            line=dict(color=PURPLE, width=3),
            fillcolor="rgba(167,139,250,.09)",
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(range=[0, 100], gridcolor=BORDER),
                angularaxis=dict(gridcolor=BORDER),
            )
        )
        st.plotly_chart(make_chart(fig, 430), use_container_width=True)

        heading("FACTOR DIFFERENCES", "Indicator Comparison")
        comparison = pd.DataFrame({
            "Factor": FACTORS,
            zone_a: vals_a,
            zone_b: vals_b,
        })
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name=zone_a, x=FACTORS, y=vals_a, marker_color=CYAN
        ))
        fig.add_trace(go.Bar(
            name=zone_b, x=FACTORS, y=vals_b, marker_color=PURPLE
        ))
        fig.update_layout(barmode="group")
        fig.update_yaxes(range=[0, 110], gridcolor=BORDER, title="Input value")
        st.plotly_chart(make_chart(fig, 360), use_container_width=True)

        st.dataframe(comparison, hide_index=True, use_container_width=True)

        st.markdown(
            f"**Index difference:** {abs(score_a-score_b):.1f} points. "
            "This is a comparison of model outputs, not a measured difference "
            "in real-world danger."
        )


# ==========================================================
# 4. SCENARIO LAB
# ==========================================================

elif page == "Scenario Lab":

    heading(
        "04 / INTERACTIVE SIMULATION",
        "Scenario Lab",
        "Adjust indicators and instantly explore the effect on the weighted index.",
    )

    zone = st.selectbox("CHOOSE A BASELINE ZONE", list(ZONES.keys()))
    original = ZONES[zone]
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
                key=f"scenario_{zone}_{factor}",
            )
            st.caption(f"Weight: {WEIGHTS[factor]*100:.0f}%")
            simulated.append(value)

    baseline = calculate_score(original)
    result = calculate_score(simulated)
    change = round(result - baseline, 1)
    level = classify(result)
    color = RISK_COLORS[level]

    st.markdown("---")
    a, b, c = st.columns(3)
    with a:
        metric_card("BASELINE INDEX", str(baseline), BLUE)
    with b:
        metric_card("SIMULATED INDEX", str(result), color)
    with c:
        metric_card("SIMULATED BAND", level, color)

    st.metric("Change from baseline", f"{change:+.1f} points")

    left, right = st.columns(2)
    with left:
        heading("OUTPUT", "Baseline vs Scenario")
        fig = go.Figure(go.Bar(
            x=["Baseline", "Scenario"],
            y=[baseline, result],
            marker_color=[BLUE, color],
            text=[baseline, result],
            textposition="outside",
        ))
        fig.update_yaxes(range=[0, 112], gridcolor=BORDER)
        st.plotly_chart(make_chart(fig, 320), use_container_width=True)

    with right:
        heading("INPUT SIGNATURE", "Scenario Radar")
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=original + [original[0]],
            theta=FACTORS + [FACTORS[0]],
            name="Baseline",
            line=dict(color=BLUE, dash="dash"),
        ))
        fig.add_trace(go.Scatterpolar(
            r=simulated + [simulated[0]],
            theta=FACTORS + [FACTORS[0]],
            name="Scenario",
            line=dict(color=CYAN, width=3),
            fill="toself",
            fillcolor="rgba(66,245,197,.10)",
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(range=[0, 100], gridcolor=BORDER),
                angularaxis=dict(gridcolor=BORDER),
            )
        )
        st.plotly_chart(make_chart(fig, 320), use_container_width=True)

    if result >= 80:
        st.error("CRITICAL band: review preparedness and mitigation priorities.")
    elif result >= 65:
        st.warning("HIGH band: review preventive measures and readiness.")
    elif result >= 45:
        st.info("MODERATE band: consider continued monitoring and prevention.")
    else:
        st.success("LOWER band under the current scoring rules.")

    report = pd.DataFrame({
        "Factor": FACTORS,
        "Weight": [WEIGHTS[x] for x in FACTORS],
        "Baseline input": original,
        "Scenario input": simulated,
        "Baseline contribution": [
            original[i] * WEIGHTS[FACTORS[i]] for i in range(5)
        ],
        "Scenario contribution": [
            simulated[i] * WEIGHTS[FACTORS[i]] for i in range(5)
        ],
    })

    st.download_button(
        "⬇ DOWNLOAD SCENARIO CSV",
        data=report.to_csv(index=False).encode("utf-8"),
        file_name="tera_scenario_report.csv",
        mime="text/csv",
    )

    st.caption(
        "This is a mathematical scenario explorer, not a physical simulation "
        "or a validated disaster forecast."
    )


# ==========================================================
# 5. MISSION CONTROL
# ==========================================================

elif page == "Mission Control":

    heading(
        "05 / RESPONSE WORKSPACE",
        "Mission Control",
        "Create a preparedness review checklist for one selected zone.",
    )

    zone = st.selectbox("SELECT ZONE", list(ZONES.keys()))
    values = ZONES[zone]
    s = calculate_score(values)
    level = classify(s)
    color = RISK_COLORS[level]

    metric_card(f"{zone.upper()} · MODEL INDEX", f"{s} · {level}", color)

    st.markdown("### Preparedness Checklist")
    st.caption(
        "These are general discussion prompts, not official emergency instructions."
    )

    checked = []
    for i, action in enumerate(ACTIONS[zone]):
        checked.append(
            st.checkbox(action, key=f"mission_{zone}_{i}")
        )

    notes = st.text_area(
        "Mission notes",
        placeholder="Record observations, ideas, and proposed next steps...",
        height=120,
    )

    completed = sum(checked)
    total = len(checked)
    st.progress(completed / total if total else 0)
    st.caption(f"{completed} of {total} checklist items marked complete")

    if st.button("GENERATE MISSION BRIEF"):
        st.markdown("---")
        st.subheader("Mission Brief")
        st.write(f"**Zone:** {zone}")
        st.write(f"**Illustrative index:** {s}/100")
        st.write(f"**Model classification:** {level}")
        st.write(f"**Checklist reviewed:** {completed}/{total}")

        for action, done in zip(ACTIONS[zone], checked):
            st.write(f"{'✓' if done else '○'} {action}")

        st.write("**Notes:**")
        st.write(notes.strip() or "No notes entered.")

        st.caption(
            "Prepared by the TERA demonstration interface. "
            "This brief is not an official response plan."
        )

        brief = [
            "TERA 2.0 — MIDNIGHT INTELLIGENCE EDITION",
            "MISSION BRIEF",
            f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"Zone: {zone}",
            f"Illustrative index: {s}/100",
            f"Model band: {level}",
            f"Checklist: {completed}/{total}",
            "",
            "CHECKLIST:",
        ]
        brief.extend([
            f"[{'x' if done else ' '}] {action}"
            for action, done in zip(ACTIONS[zone], checked)
        ])
        brief.extend(["", "NOTES:", notes or "No notes entered."])
        brief.extend([
            "",
            "Disclaimer: illustrative student prototype, not an official plan.",
        ])

        st.download_button(
            "⬇ DOWNLOAD MISSION BRIEF",
            data="\n".join(brief),
            file_name="tera_mission_brief.txt",
            mime="text/plain",
        )


# ==========================================================
# 6. METHODOLOGY
# ==========================================================

elif page == "Methodology":

    heading(
        "06 / SCIENTIFIC TRANSPARENCY",
        "Methodology & Responsible AI",
        "A strong environmental technology project should explain both its strengths and its limitations.",
    )

    st.markdown("### Weighted Priority Formula")
    st.latex(r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U")

    st.markdown(
        "Each factor is entered on a 0–100 scale. The weighted contributions "
        "are added to calculate a priority index."
    )

    info = [
        ("Hazard", 30, "Illustrative hazard-severity input."),
        ("Vulnerability", 25, "Illustrative susceptibility to harm."),
        ("Population", 20, "Illustrative population-related input."),
        ("Exposure", 15, "Illustrative exposure-related input."),
        ("Urgency", 10, "Illustrative urgency-related input."),
    ]

    for name, weight, desc in info:
        with st.container(border=True):
            a, b = st.columns([1.3, 4])
            with a:
                st.markdown(f"**{name} · {weight}%**")
            with b:
                st.caption(desc)

    st.markdown("### Classification Thresholds")
    for name, threshold in [
        ("CRITICAL", "80–100"),
        ("HIGH", "65–79.9"),
        ("MODERATE", "45–64.9"),
        ("LOWER", "Below 45"),
    ]:
        color = RISK_COLORS[name]
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;
                    padding:12px;margin:7px 0;background:{PANEL};
                    border:1px solid {BORDER};border-left:4px solid {color};
                    border-radius:8px">
          <b style="color:{color}">{name}</b>
          <b style="color:{WHITE}">{threshold}</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### System Workflow")
    for number, title, description in [
        ("01", "INPUT", "Provide factor values."),
        ("02", "CALCULATE", "Apply the weighted formula."),
        ("03", "CLASSIFY", "Assign a model priority band."),
        ("04", "EXPLORE", "Compare zones and test scenarios."),
        ("05", "REVIEW", "Discuss preparedness actions."),
        ("06", "VALIDATE", "Check data quality and assumptions before real use."),
    ]:
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

    st.markdown("### What the Current Prototype Does Not Do")
    st.warning(
        "This version uses illustrative, manually entered data and a fixed "
        "weighted scoring rule. It does not currently connect to live sensors, "
        "satellite feeds, weather APIs, or train a machine-learning model. "
        "Its score is not a disaster probability or verified forecast. "
        "Weights and thresholds are demonstration assumptions and would need "
        "expert justification, validated data, calibration, and field testing "
        "before real-world use."
    )

    st.markdown("### Current Zone Dataset")
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.download_button(
        "⬇ EXPORT ZONE DATA",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="tera_zone_dataset.csv",
        mime="text/csv",
    )


# ----------------------- FOOTER ---------------------------

st.markdown("---")
st.markdown(f"""
<div style="text-align:center;padding:18px 0">
  <div style="font-family:'Space Grotesk',sans-serif;
              font-size:25px;font-weight:800;color:white">
    TERA<span style="color:{CYAN}"> 2.0</span>
  </div>
  <div style="font-size:10px;letter-spacing:2px;color:{CYAN};
              margin-top:7px">
    MIDNIGHT INTELLIGENCE EDITION
  </div>
  <div style="font-size:10px;color:{MUTED};margin-top:12px">
    TECHNOLOGY FOR ENVIRONMENTAL RISK ANALYSIS
  </div>
  <div style="font-size:10px;color:{MUTED};margin-top:6px">
    Student prototype · Illustrative data · Transparent scoring
  </div>
</div>
""", unsafe_allow_html=True)
