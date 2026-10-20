
import streamlit as st

st.set_page_config(
    page_title="TERA 2.0 | Environmental Intelligence",
    page_icon="🌍",
    layout="wide",
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

# Demonstration values only — not live measurements.
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
        "Inspect firebreaks and forest access routes",
        "Review dry vegetation and ignition precautions",
        "Check response teams and evacuation routes",
    ],
    "Residential Area": [
        "Review evacuation routes and public alert procedures",
        "Check emergency access and vulnerable households",
        "Review local preparedness plans",
    ],
    "Hospital": [
        "Verify backup power and emergency supplies",
        "Review patient evacuation and continuity plans",
        "Keep emergency access routes clear",
    ],
    "Smart Farm": [
        "Inspect irrigation and water-storage systems",
        "Review crop and weather-related vulnerabilities",
        "Review water conservation measures",
    ],
    "River & Dam": [
        "Review water-level monitoring procedures",
        "Check downstream communication and evacuation plans",
        "Review drainage and emergency arrangements",
    ],
    "Industrial Zone": [
        "Review hazardous-material storage procedures",
        "Check emergency shutdown and spill-response plans",
        "Review worker alerts and emergency access",
    ],
}


def calculate_score(values):
    return round(
        sum(
            values[i] * WEIGHTS[FACTORS[i]]
            for i in range(len(FACTORS))
        ),
        1,
    )


def classify_risk(value):
    if value >= 80:
        return "CRITICAL"
    if value >= 65:
        return "HIGH"
    if value >= 45:
        return "MODERATE"
    return "LOWER"


def risk_bar(label, value, color=CYAN):
    value = max(0, min(100, float(value)))
    st.markdown(
        f"""
        <div style="margin:13px 0">
          <div style="display:flex;justify-content:space-between;
                      margin-bottom:7px;gap:12px">
            <span style="font-size:12px;font-weight:700;color:#D8E7F2">
              {label}
            </span>
            <span style="font-weight:800;color:{color}">
              {value:.1f}
            </span>
          </div>
          <div style="height:7px;background:#203447;border-radius:12px;
                      overflow:hidden">
            <div style="height:7px;width:{value}%;background:{color};
                        border-radius:12px"></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def risk_badge(level):
    color = RISK_COLORS[level]
    backgrounds = {
        "CRITICAL": "#321522",
        "HIGH": "#342316",
        "MODERATE": "#332C17",
        "LOWER": "#10302A",
    }
    background = backgrounds[level]
    st.markdown(
        f'<span style="display:inline-block;padding:6px 9px;'
        f'border-radius:5px;font-size:10px;font-weight:800;'
        f'letter-spacing:1px;color:{color};background:{background};'
        f'border:1px solid {color}55">{level}</span>',
        unsafe_allow_html=True,
    )


def section(kicker, title, description=None):
    st.markdown(
        f'<div style="color:{CYAN};font-size:10px;letter-spacing:2.4px;'
        f'font-weight:800;margin-top:12px">{kicker}</div>',
        unsafe_allow_html=True,
    )
    st.subheader(title)
    if description:
        st.caption(description)


# -------------------- VISUAL DESIGN --------------------

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    .stApp {{
        background:
          radial-gradient(ellipse at 85% 0%,
          rgba(20,105,130,.15), transparent 38%), {BG};
        color: {WHITE};
    }}
    [data-testid="stHeader"] {{
        background: rgba(7,17,31,.93);
    }}
    [data-testid="stSidebar"] {{
        background: #091523;
        border-right: 1px solid {BORDER};
    }}
    [data-testid="stSidebar"] * {{
        color: #DCEAF5;
    }}
    h1, h2, h3 {{
        color: {WHITE} !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }}
    p, li, label {{
        color: {MUTED};
    }}
    .hero {{
        background: linear-gradient(115deg,
          #0D1D2D 0%, #102D40 62%, #0B3A3A 100%);
        border: 1px solid #245165;
        border-radius: 22px;
        padding: 32px;
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
    }}
    .eyebrow {{
        color: {CYAN};
        font-size: 11px;
        letter-spacing: 3px;
        font-weight: 800;
    }}
    .hero-title {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(42px, 6vw, 67px);
        font-weight: 700;
        line-height: 1;
        margin: 15px 0 12px;
        color: white;
    }}
    .hero-title span {{
        color: {CYAN};
    }}
    .hero-copy {{
        color: #B9CEDD;
        font-size: 15px;
        line-height: 1.8;
        max-width: 690px;
    }}
    .hero-pill {{
        display: inline-block;
        border: 1px solid #28675E;
        background: rgba(67,245,197,.08);
        color: {CYAN};
        padding: 7px 11px;
        border-radius: 6px;
        font-size: 10px;
        letter-spacing: 1.5px;
        font-weight: 800;
        margin-top: 17px;
    }}
    .metric-card {{
        background: linear-gradient(145deg, {PANEL}, #0A1725);
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 19px;
        min-height: 108px;
    }}
    .metric-label {{
        font-size: 10px;
        color: {MUTED};
        font-weight: 800;
        letter-spacing: 1.5px;
    }}
    .metric-value {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 32px;
        font-weight: 800;
        margin-top: 9px;
    }}
    .panel {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 21px;
        margin: 8px 0 16px;
    }}
    .note {{
        background: #102C32;
        border: 1px solid #24584F;
        border-left: 4px solid {CYAN};
        padding: 13px 15px;
        border-radius: 8px;
        color: #C0DED9;
        font-size: 12px;
        line-height: 1.75;
        margin: 12px 0;
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
        border-color: #B1FFE8;
    }}
    [data-testid="stMetric"] {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 15px;
    }}
    [data-testid="stMetricLabel"] {{
        color: {MUTED};
    }}
    [data-testid="stMetricValue"] {{
        color: {WHITE};
        font-weight: 800;
    }}
    [data-baseweb="select"] > div,
    [data-baseweb="input"] > div {{
        background: #102437;
        border-color: {BORDER};
    }}
    hr {{
        border-color: {BORDER};
    }}
    footer, #MainMenu {{
        visibility: hidden;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------- SIDEBAR --------------------

st.sidebar.markdown(
    f"""
    <div style="padding:12px 3px 18px">
      <div style="font-family:'Space Grotesk',sans-serif;
                  font-size:27px;font-weight:800;color:white">
        TERA<span style="color:{CYAN}">.2</span>
      </div>
      <div style="font-size:10px;font-weight:800;letter-spacing:2px;
                  color:{CYAN};margin-top:4px">
        MIDNIGHT INTELLIGENCE
      </div>
      <div style="font-size:11px;color:{MUTED};margin-top:9px">
        ENVIRONMENTAL RISK SYSTEM
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "COMMAND NAVIGATION",
    [
        "Command Centre",
        "Risk Simulator",
        "Response Planner",
        "Methodology & AI",
    ],
)
st.sidebar.markdown("---")
st.sidebar.markdown("### SYSTEM STATUS")
st.sidebar.success("SCORING ENGINE READY")
st.sidebar.caption("DEMONSTRATION DATASET")
st.sidebar.caption("No live sensors connected")


# -------------------- COMPUTE ALL ZONES --------------------

results = []
for zone, values in ZONES.items():
    zone_score = calculate_score(values)
    results.append({
        "Zone": zone,
        "Score": zone_score,
        "Band": classify_risk(zone_score),
        "Values": values,
    })

results.sort(key=lambda item: item["Score"], reverse=True)

critical_count = sum(item["Band"] == "CRITICAL" for item in results)
high_count = sum(item["Band"] == "HIGH" for item in results)
average_score = round(
    sum(item["Score"] for item in results) / len(results), 1
)
top = results[0]


# -------------------- HERO HEADER --------------------

st.markdown(
    f"""
    <div class="hero">
      <div class="eyebrow">
        ENVIRONMENTAL INTELLIGENCE / COMMAND INTERFACE
      </div>
      <div class="hero-title">TERA<span> 2.0</span></div>
      <div class="hero-copy">
        The environment sends signals. TERA helps turn indicators into
        priorities, and priorities into action.
      </div>
      <div class="hero-pill">
        ● MIDNIGHT INTELLIGENCE / STUDENT PROTOTYPE
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 1. COMMAND CENTRE
# =========================================================

if page == "Command Centre":

    section(
        "01 / SITUATIONAL AWARENESS",
        "Environmental Command Centre",
        "A comparative overview of six demonstration zones.",
    )

    columns = st.columns(4)
    metrics = [
        ("ZONES ANALYSED", str(len(results)), CYAN),
        ("CRITICAL", str(critical_count), RED),
        ("HIGH PRIORITY", str(high_count), ORANGE),
        ("MEAN INDEX", str(average_score), BLUE),
    ]

    for column, (label, value, color) in zip(columns, metrics):
        with column:
            st.markdown(
                f"""
                <div class="metric-card" style="border-top:3px solid {color}">
                  <div class="metric-label">{label}</div>
                  <div class="metric-value" style="color:{color}">
                    {value}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section(
        "02 / PRIORITY ENGINE",
        "Zone Risk Ranking",
        "Higher scores mean higher relative priority within this model.",
    )

    for rank, item in enumerate(results, start=1):
        color = RISK_COLORS[item["Band"]]
        with st.container(border=True):
            rank_col, zone_col, status_col = st.columns([0.7, 5, 1.4])

            with rank_col:
                st.markdown(
                    f"<div style='font-size:25px;font-weight:800;"
                    f"color:{CYAN};padding-top:5px'>{rank:02}</div>",
                    unsafe_allow_html=True,
                )

            with zone_col:
                st.markdown(f"**{item['Zone']}**")
                risk_bar("WEIGHTED PRIORITY INDEX", item["Score"], color)

            with status_col:
                st.markdown("<div style='height:10px'></div>",
                            unsafe_allow_html=True)
                risk_badge(item["Band"])
                st.caption(f"{item['Score']} / 100")

    section("03 / MODEL INSIGHT", "Priority Focus")

    # The colour is calculated separately to avoid nested f-string lookups.
    top_color = RISK_COLORS[top["Band"]]
    top_zone = top["Zone"]
    top_score = top["Score"]
    top_band = top["Band"]

    st.markdown(
        f"""
        <div class="panel" style="border-left:4px solid {top_color}">
          <div style="font-size:10px;letter-spacing:2px;color:{CYAN};
                      font-weight:800">HIGHEST MODEL SCORE</div>
          <div style="font-size:29px;font-weight:800;color:{WHITE};
                      margin:10px 0">{top_zone}</div>
          <div style="font-size:25px;font-weight:800;color:{top_color}">
            {top_score}
            <span style="font-size:13px;color:{MUTED}">
              / 100 · {top_band}
            </span>
          </div>
          <div style="font-size:12px;color:{MUTED};margin-top:10px">
            Suggested focus for review under the current model assumptions.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section("04 / DISTRIBUTION", "Priority Band Overview")

    counts = {
        level: sum(item["Band"] == level for item in results)
        for level in ["CRITICAL", "HIGH", "MODERATE", "LOWER"]
    }

    for level, count in counts.items():
        risk_bar(
            f"{level} · {count} ZONE(S)",
            count / len(results) * 100,
            RISK_COLORS[level],
        )

    st.markdown(
        """
        <div class="note">
          <b>MODEL INTEGRITY NOTE</b><br>
          These are illustrative weighted priority indices, not actual
          disaster probabilities, validated forecasts, or live measurements.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 2. RISK SIMULATOR
# =========================================================

elif page == "Risk Simulator":

    section(
        "02 / INTERACTIVE LAB",
        "Risk Simulator",
        "Change an indicator and observe the model response.",
    )

    st.markdown(
        """
        <div class="note">
          <b>SIMULATION MODE</b><br>
          Adjust the five factors. The weighted formula recalculates the
          score as you move each slider.
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_zone = st.selectbox("SELECT ZONE", list(ZONES.keys()))
    original = ZONES[selected_zone]
    simulated = []

    left, right = st.columns(2)

    for index, factor in enumerate(FACTORS):
        target = left if index % 2 == 0 else right

        with target:
            value = st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(original[index]),
                key=f"sim_{selected_zone}_{factor}",
            )
            st.caption(f"WEIGHT · {WEIGHTS[factor] * 100:.0f}%")
            simulated.append(value)

    base_score = calculate_score(original)
    new_score = calculate_score(simulated)
    delta = round(new_score - base_score, 1)
    new_band = classify_risk(new_score)
    new_color = RISK_COLORS[new_band]

    st.markdown("---")
    section("SIMULATION OUTPUT", "Model Response")

    c1, c2, c3 = st.columns(3)
    c1.metric("BASELINE INDEX", f"{base_score}/100")
    c2.metric("SIMULATED INDEX", f"{new_score}/100", delta=f"{delta:+.1f}")

    with c3:
        st.markdown(
            f"""
            <div class="metric-card" style="border-top:3px solid {new_color}">
              <div class="metric-label">PRIORITY BAND</div>
              <div class="metric-value" style="font-size:23px;color:{new_color}">
                {new_band}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Indicator Profile")
    for index, factor in enumerate(FACTORS):
        bar_color = CYAN if simulated[index] == original[index] else BLUE
        risk_bar(
            f"{factor.upper()} · {WEIGHTS[factor] * 100:.0f}% WEIGHT",
            simulated[index],
            bar_color,
        )

    st.markdown("### Interpretation")
    if new_score >= 80:
        st.error("CRITICAL BAND — review preparedness and mitigation priorities.")
    elif new_score >= 65:
        st.warning("HIGH PRIORITY — review preventive measures and readiness.")
    elif new_score >= 45:
        st.info("MODERATE PRIORITY — continue monitoring and preventive review.")
    else:
        st.success("LOWER PRIORITY BAND — maintain routine preparedness.")

    st.caption(
        "This is a mathematical simulation using illustrative inputs. "
        "It does not measure real conditions or predict disaster probability."
    )


# =========================================================
# 3. RESPONSE PLANNER
# =========================================================

elif page == "Response Planner":

    section(
        "03 / ACTION WORKSPACE",
        "Response Planning Desk",
        "Explore possible preparedness actions for a selected zone.",
    )

    ranked_zones = [item["Zone"] for item in results]
    selected_zone = st.selectbox(
        "SELECT ZONE",
        ranked_zones,
        key="planner_zone",
    )

    selected = next(
        item for item in results if item["Zone"] == selected_zone
    )
    selected_color = RISK_COLORS[selected["Band"]]

    st.markdown(
        f"""
        <div class="panel" style="border-left:4px solid {selected_color}">
          <div style="color:{CYAN};font-size:10px;letter-spacing:2px">
            SELECTED ZONE
          </div>
          <div style="font-size:28px;font-weight:800;color:{WHITE};
                      margin:10px 0">{selected_zone}</div>
          <div style="font-size:23px;font-weight:800;color:{selected_color}">
            {selected["Score"]} / 100
          </div>
          <div style="font-size:11px;color:{MUTED};margin-top:5px">
            MODEL BAND · {selected["Band"]}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Preparedness Checklist")
    st.caption(
        "These are general planning suggestions, not official emergency instructions."
    )

    for index, action in enumerate(ACTIONS[selected_zone]):
        st.checkbox(action, key=f"action_{selected_zone}_{index}")

    notes = st.text_area(
        "Planning notes",
        placeholder="Observations, responsible persons, next steps...",
        height=120,
        key="planner_notes",
    )

    if st.button("GENERATE PLANNING SUMMARY"):
        st.markdown("---")
        st.markdown("### Planning Summary")
        st.write(f"**Zone:** {selected_zone}")
        st.write(f"**Model index:** {selected['Score']}/100")
        st.write(f"**Priority band:** {selected['Band']}")

        for index, action in enumerate(ACTIONS[selected_zone]):
            checked = st.session_state.get(
                f"action_{selected_zone}_{index}", False
            )
            status = "✓ REVIEWED" if checked else "○ PENDING"
            st.write(f"{status} — {action}")

        st.write(
            "**Notes:**",
            notes.strip() if notes.strip() else "No notes entered.",
        )
        st.caption(
            "Planning aid only; not an operational emergency response plan."
        )


# =========================================================
# 4. METHODOLOGY & AI
# =========================================================

elif page == "Methodology & AI":

    section(
        "04 / TRANSPARENCY",
        "Methodology & AI",
        "The science behind the environmental priority index.",
    )

    st.markdown(
        """
        <div class="panel">
          <div style="color:#43F5C5;font-size:10px;letter-spacing:2px">
            CORE MODEL
          </div>
          <div style="font-size:13px;color:#91A8BC;margin:8px 0">
            Weighted Environmental Priority Index
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.latex(r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U")

    descriptions = [
        ("HAZARD", "30%", "Illustrative hazard-severity indicator."),
        ("VULNERABILITY", "25%", "Illustrative susceptibility to harm."),
        ("POPULATION", "20%", "Illustrative concentration of people potentially affected."),
        ("EXPOSURE", "15%", "Illustrative extent of people or assets in harm's way."),
        ("URGENCY", "10%", "Illustrative need for timely review."),
    ]

    st.markdown("### Factor Weights")

    for name, weight, description in descriptions:
        with st.container(border=True):
            a, b, c = st.columns([2, 1, 5])
            with a:
                st.markdown(f"**{name}**")
            with b:
                st.markdown(
                    f"<span style='color:{CYAN};font-weight:800'>{weight}</span>",
                    unsafe_allow_html=True,
                )
            with c:
                st.caption(description)

    st.markdown("### Classification Thresholds")

    for level, interval in [
        ("CRITICAL", "80–100"),
        ("HIGH", "65–79.9"),
        ("MODERATE", "45–64.9"),
        ("LOWER", "Below 45"),
    ]:
        color = RISK_COLORS[level]
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;
                        align-items:center;padding:12px 14px;margin:8px 0;
                        background:{PANEL};border:1px solid {BORDER};
                        border-left:4px solid {color};border-radius:8px">
              <span style="font-size:12px;font-weight:800;color:{color}">
                {level}
              </span>
              <span style="font-size:12px;font-weight:700;color:{WHITE}">
                {interval}
              </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### How TERA Works")

    workflow = [
        ("01", "INPUT", "Supply illustrative indicators for each zone."),
        ("02", "CALCULATE", "Apply the transparent weighted formula."),
        ("03", "CLASSIFY", "Assign the score to a priority band."),
        ("04", "PLAN", "Use suggestions to structure human review."),
        ("05", "VERIFY", "Validate data and decisions with domain experts."),
    ]

    for number, title, description in workflow:
        with st.container(border=True):
            a, b = st.columns([0.7, 5])
            with a:
                st.markdown(
                    f"<span style='font-size:22px;font-weight:800;color:{CYAN}'>"
                    f"{number}</span>",
                    unsafe_allow_html=True,
                )
            with b:
                st.markdown(f"**{title}**")
                st.caption(description)

    st.markdown("### Scientific Limitations")
    st.warning(
        "This prototype uses manually supplied illustrative data and a "
        "rule-based weighted formula. It does not currently train a machine "
        "learning model, connect to live sensors, ingest live satellite data, "
        "or predict actual disasters. The index is not a probability. "
        "Real-world use requires validated data, justified weights, expert "
        "review, calibration, and field testing."
    )


# -------------------- FOOTER --------------------

st.markdown("---")
st.markdown(
    f"""
    <div style="text-align:center;padding:20px 0 10px">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:22px;
                  font-weight:800;color:{WHITE}">
        TERA<span style="color:{CYAN}"> 2.0</span>
      </div>
      <div style="font-size:10px;letter-spacing:2px;font-weight:700;
                  color:{MUTED};margin-top:7px">
        TECHNOLOGY FOR ENVIRONMENTAL RISK ANALYSIS
      </div>
      <div style="font-size:10px;color:{MUTED};margin-top:12px">
        MIDNIGHT INTELLIGENCE · STUDENT PROTOTYPE
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
