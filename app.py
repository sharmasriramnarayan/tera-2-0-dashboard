
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TERA 2.0 | Environmental Intelligence",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap');

.stApp {
    background: radial-gradient(
        ellipse at top left,
        #17392e 0%,
        #08120f 48%,
        #050a09 100%
    );
    color: #effcf6;
    font-family: 'Manrope', sans-serif;
}
[data-testid="stSidebar"] {
    background: #091713;
    border-right: 1px solid #24483b;
}
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(120deg, #123329, #0b1915);
    border: 1px solid #315b49;
    border-radius: 22px;
    padding: 30px;
}
.eyebrow {
    color: #7cf7c5;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
}
.metric {
    background: #10221c;
    border: 1px solid #284a3d;
    border-radius: 16px;
    padding: 18px;
}
.metric-label {
    color: #9bb7ac;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.metric-value {
    color: #7cf7c5;
    font-size: 30px;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="eyebrow">ENVIRONMENTAL INTELLIGENCE / 02</div>
    <h1 style="font-size:48px;line-height:1.1;">
        See the risk.<br>
        <span style="color:#7cf7c5;">Prioritise the response.</span>
    </h1>
    <p style="color:#b8d4c9;font-size:17px;">
        TERA turns environmental risk factors into a transparent
        priority index across six connected zones.
    </p>
</div>
""", unsafe_allow_html=True)

zones = {
    "Forest": [72, 65, 35, 95, 75],
    "Residential Area": [80, 85, 95, 45, 90],
    "Hospital": [75, 90, 90, 30, 95],
    "Smart Farm": [60, 65, 45, 75, 60],
    "River & Dam": [85, 75, 70, 85, 85],
    "Industrial Zone": [82, 70, 75, 65, 80],
}

weights = [0.30, 0.25, 0.20, 0.15, 0.10]

def calculate_risk(values):
    return round(sum(v * w for v, w in zip(values, weights)), 2)

def classify_risk(score):
    if score >= 80:
        return "CRITICAL"
    if score >= 65:
        return "HIGH"
    if score >= 45:
        return "MODERATE"
    return "LOWER"

rows = []
for name, values in zones.items():
    rows.append({
        "Zone": name,
        "Risk score": calculate_risk(values),
        "Priority": classify_risk(calculate_risk(values))
    })

df = pd.DataFrame(rows).sort_values(
    "Risk score", ascending=False
)

# CREATE THE FOUR DASHBOARD TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "◈ Command Centre",
    "⌁ Risk Simulator",
    "◎ Response Planner",
    "✳ Methodology & AI"
])

# TAB 1: COMMAND CENTRE
with tab1:
    st.subheader("Environmental Priority Ranking")

    a, b, c = st.columns(3)

    with a:
        st.metric("Zones Assessed", "06")

    with b:
        st.metric("Top Priority", df.iloc[0]["Zone"])

    with c:
        st.metric(
            "Highest Score",
            f'{df.iloc[0]["Risk score"]:.1f}'
        )

    fig = px.bar(
        df.sort_values("Risk score"),
        x="Risk score",
        y="Zone",
        orientation="h",
        color="Risk score",
        color_continuous_scale=[
            "#7cf7c5", "#f3df78",
            "#ff9b70", "#ff6474"
        ],
        range_color=(0, 100)
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#effcf6",
        coloraxis_showscale=False,
        xaxis_title="Risk-priority index",
        yaxis_title="",
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Zone Assessment")
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )


# TAB 2: RISK SIMULATOR
with tab2:
    st.subheader("Test a Hypothetical Scenario")

    selected_zone = st.selectbox(
        "Choose a zone to simulate",
        list(zones.keys()),
        key="simulator_zone"
    )

    st.write(
        "Adjust the five factors to see how "
        "the risk-priority score changes."
    )

    factor_names = [
        "Hazard severity",
        "Vulnerability",
        "Population impact",
        "Ecological value",
        "Urgency"
    ]

    default_values = zones[selected_zone]
    new_values = []

    for name, default in zip(factor_names, default_values):
        value = st.slider(
            name,
            min_value=0,
            max_value=100,
            value=int(default),
            key=f"sim_{selected_zone}_{name}"
        )
        new_values.append(value)

    new_score = calculate_risk(new_values)

    st.metric(
        "Simulated Risk-Priority Index",
        f"{new_score:.1f} / 100",
        classify_risk(new_score)
    )

    st.caption(
        "This score reflects your selected inputs. "
        "It is not a prediction of the probability "
        "of a real disaster."
    )

    contributions = pd.DataFrame({
        "Factor": factor_names,
        "Contribution": [
            value * weight
            for value, weight in zip(new_values, weights)
        ]
    })

    st.subheader("Factor Contributions")
    st.bar_chart(
        contributions.set_index("Factor")
    )


# TAB 3: RESPONSE PLANNER
with tab3:
    st.subheader("Response Planning Concept")

    response_zone = st.selectbox(
        "Select a zone",
        list(zones.keys()),
        key="response_zone"
    )

    actions = {
        "Forest": (
            "Review forest-fire alerts and protect "
            "safe evacuation routes."
        ),
        "Residential Area": (
            "Review flood alerts and identify safe routes."
        ),
        "Hospital": (
            "Review backup-power readiness and "
            "continuity plans."
        ),
        "Smart Farm": (
            "Review water availability and "
            "irrigation efficiency."
        ),
        "River & Dam": (
            "Monitor official water-level advisories."
        ),
        "Industrial Zone": (
            "Follow facility safety procedures and "
            "contact authorised responders."
        )
    }

    st.info(actions[response_zone])

    st.subheader("Zone Priority")
    zone_score = calculate_risk(zones[response_zone])

    st.metric(
        f"{response_zone} Risk-Priority Index",
        f"{zone_score:.1f} / 100",
        classify_risk(zone_score)
    )


# TAB 4: METHODOLOGY & AI
with tab4:
    st.subheader("How TERA Calculates Risk")

    st.write(
        "TERA combines five illustrative factors "
        "into a weighted risk-priority index."
    )

    st.latex(
        r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U"
    )

    st.markdown("""
    **Factor weights**

    - Hazard Severity (H): 30%
    - Vulnerability (V): 25%
    - Population Impact (P): 20%
    - Ecological Value (E): 15%
    - Urgency (U): 10%
    """)

    st.subheader("Priority Thresholds")

    st.markdown("""
    - **CRITICAL:** 80–100
    - **HIGH:** 65–79.99
    - **MODERATE:** 45–64.99
    - **LOWER:** Below 45
    """)

    st.subheader("Scientific Limitations")

    st.write(
        "TERA is an educational risk-prioritisation "
        "prototype. Its built-in values are illustrative, "
        "not live sensor readings. The score is not a "
        "calibrated disaster probability or a validated "
        "real-world forecast. Response decisions should "
        "follow official advisories and authorised agencies."
    )
