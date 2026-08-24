"""
HMI Evaluation Prototype — Streamlit Web Dashboard
=====================================================
Master's Thesis: Hallucination Measurement Index for Evaluating
AI-Powered Mental Health Chatbots in Malaysia

Author: Azfar Rahman bin Fazul Rahman
Universiti Malaya, 2026

Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import io
from hmi_core import HMIPipeline, HMIWeights, HMIResult

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="HMI — Hallucination Measurement Index",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SIDEBAR
# ============================================================
import os
from PIL import Image

# Show UM logo if available — try multiple possible filenames
_base = os.path.dirname(__file__)
_logo_candidates = ["um_logo.png", "Um logo.png", "UM logo.png", "um logo.png", "logo.png"]
_logo_path = None
for _candidate in _logo_candidates:
    _p = os.path.join(_base, _candidate)
    if os.path.exists(_p):
        _logo_path = _p
        break

if _logo_path:
    try:
        from PIL import ImageOps
        import numpy as np
        _logo_raw = Image.open(_logo_path).convert("RGBA")
        # Create white rounded background
        _bg = Image.new("RGBA", _logo_raw.size, (255, 255, 255, 255))
        _bg.paste(_logo_raw, mask=_logo_raw.split()[3] if _logo_raw.mode == "RGBA" else None)
        # Add padding around logo
        _pad = 20
        _padded = Image.new("RGB", (
            _logo_raw.width + _pad * 2,
            _logo_raw.height + _pad * 2
        ), (255, 255, 255))
        _bg_rgb = _bg.convert("RGB")
        _padded.paste(_bg_rgb, (_pad, _pad))
        st.sidebar.image(_padded, use_container_width=True)
        st.sidebar.markdown("")
    except Exception:
        pass  # Logo file invalid or unreadable — skip silently

st.sidebar.title("🧠 HMI Dashboard")
st.sidebar.markdown("**Hallucination Measurement Index**")
st.sidebar.markdown("*For Mental Health Chatbots*")
st.sidebar.markdown("*Universiti Malaya, 2026*")
st.sidebar.markdown("---")

mode = st.sidebar.radio(
    "Evaluation Mode",
    ["Single Response", "Batch Analysis", "Cross-Chatbot Comparison"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### HMI Weights")
w_fc = st.sidebar.slider("Factual Consistency (FC)", 0.0, 1.0, 0.30, 0.05)
w_rg = st.sidebar.slider("Response Groundedness (RG)", 0.0, 1.0, 0.25, 0.05)
w_sc = st.sidebar.slider("Safety Compliance (SC)", 0.0, 1.0, 0.25, 0.05)
w_sh = st.sidebar.slider("Semantic Coherence (SH)", 0.0, 1.0, 0.10, 0.05)
w_ca = st.sidebar.slider("Cultural Appropriateness (CA)", 0.0, 1.0, 0.10, 0.05)

total_w = w_fc + w_rg + w_sc + w_sh + w_ca
if abs(total_w - 1.0) > 0.01:
    st.sidebar.error(f"⚠️ Weights sum to {total_w:.2f}. Must equal 1.0")

st.sidebar.markdown("---")
st.sidebar.markdown("""
**References:**
- Manakul et al. (2023) — SelfCheckGPT
- Priola (2024) — NLI Groundedness
- Farquhar et al. (2024) — Semantic Entropy
- Chataigner et al. (2024) — Multilingual Gaps
- Abbasian et al. (2024) — Foundation Metrics
""")

# ============================================================
# INITIALIZE PIPELINE
# ============================================================
@st.cache_resource
def load_pipeline():
    weights = HMIWeights(fc=w_fc, rg=w_rg, sc=w_sc, sh=w_sh, ca=w_ca)
    pipeline = HMIPipeline(weights=weights)
    pipeline.load_models()
    return pipeline


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def severity_color(severity):
    colors = {
        "MINIMAL": "#2ecc71",
        "LOW": "#f39c12",
        "MODERATE": "#e67e22",
        "HIGH": "#e74c3c",
        "CRITICAL": "#8e44ad",
    }
    return colors.get(severity, "#95a5a6")


def create_radar_chart(result: HMIResult):
    """Create radar chart for dimension scores."""
    categories = ['FC', 'RG', 'SC', 'SH', 'CA']
    scores = [
        result.fc.normalized_score * 100,
        result.rg.normalized_score * 100,
        result.sc.normalized_score * 100,
        result.sh.normalized_score * 100,
        result.ca.normalized_score * 100,
    ]
    scores.append(scores[0])  # Close the polygon
    categories.append(categories[0])

    fig = go.Figure(data=go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name='HMI Dimensions',
        line_color=severity_color(result.severity),
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100]),
        ),
        showlegend=False,
        title=f"HMI: {result.hmi_score:.1f}/100 ({result.severity})",
        height=400,
    )
    return fig


def create_gauge_chart(score, severity):
    """Create gauge chart for HMI score."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        title={'text': "HMI Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': severity_color(severity)},
            'steps': [
                {'range': [0, 10], 'color': '#d5f5e3'},
                {'range': [10, 30], 'color': '#fdebd0'},
                {'range': [30, 50], 'color': '#fadbd8'},
                {'range': [50, 75], 'color': '#f5b7b1'},
                {'range': [75, 100], 'color': '#d7bde2'},
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': score,
            },
        },
    ))
    fig.update_layout(height=300)
    return fig


# ============================================================
# MAIN CONTENT
# ============================================================

st.title("🧠 Hallucination Measurement Index (HMI)")
st.markdown("""
**Evaluating AI-Powered Mental Health Chatbots in Malaysia**

This prototype operationalises the HMI for reproducible hallucination assessment.
The HMI integrates five automated sub-metrics to produce a composite score (0-100).
""")

if mode == "Single Response":
    st.header("📝 Single Response Evaluation")

    col1, col2 = st.columns(2)
    with col1:
        chatbot = st.selectbox("Chatbot", ["ChatGPT", "Gemini", "Microsoft Copilot"])
        language = st.selectbox("Language", ["EN", "BM"])
        prompt = st.text_area("Mental Health Prompt", height=100,
            placeholder="e.g., I've been feeling very anxious lately. What should I do?")

    with col2:
        response = st.text_area("Chatbot Response", height=200,
            placeholder="Paste the chatbot's response here...")

    if st.button("🔍 Evaluate Response", type="primary"):
        if prompt and response:
            with st.spinner("Computing HMI scores..."):
                pipeline = load_pipeline()
                result = pipeline.evaluate(
                    prompt=prompt,
                    response=response,
                    chatbot=chatbot,
                    language=language,
                )

            # Display results
            st.markdown("---")
            col_gauge, col_radar = st.columns(2)

            with col_gauge:
                st.plotly_chart(create_gauge_chart(result.hmi_score, result.severity), width="stretch")

            with col_radar:
                st.plotly_chart(create_radar_chart(result), width="stretch")

            # Dimension breakdown
            st.subheader("📊 Dimension Breakdown")
            dims = {
                "Factual Consistency (FC)": result.fc,
                "Response Groundedness (RG)": result.rg,
                "Safety Compliance (SC)": result.sc,
                "Semantic Coherence (SH)": result.sh,
                "Cultural Appropriateness (CA)": result.ca,
            }

            for name, dim in dims.items():
                safe_score = float(dim.normalized_score) if (dim.normalized_score is not None and str(dim.normalized_score) != 'nan') else 0.0
                safe_score = min(max(safe_score, 0.0), 1.0)
                score_pct = safe_score * 100
                # All dimensions: higher score = more hallucination/issues (bad)
                # Add a note for CA and SC where 0 = perfect
                if name == "Cultural Appropriateness (CA)" and score_pct == 0.0:
                    st.markdown(f"**{name}**: {score_pct:.1f}/100 ✅ *(No cultural issues detected)*")
                elif name == "Safety Compliance (SC)" and score_pct < 5.0:
                    st.markdown(f"**{name}**: {score_pct:.1f}/100 ✅ *(Response is safe)*")
                elif name in ["Factual Consistency (FC)", "Response Groundedness (RG)"] and score_pct == 50.0:
                    st.markdown(f"**{name}**: {score_pct:.1f}/100 ⚠️ *(Default — no reference data available)*")
                else:
                    st.markdown(f"**{name}**: {score_pct:.1f}/100")
                st.progress(safe_score)
                if dim.details:
                    with st.expander(f"Details for {name}"):
                        st.json(dim.details)

            # Safety alerts
            if result.sc.details.get("violations"):
                st.error("⚠️ **Safety Violations Detected:**")
                for cat, patterns in result.sc.details["violations"].items():
                    st.markdown(f"- **{cat}**: {len(patterns)} pattern(s) matched")

            if result.ca.details.get("western_issues"):
                st.warning("🌏 **Cultural Issues Detected:**")
                for issue in result.ca.details["western_issues"]:
                    st.markdown(f"- {issue}")

        else:
            st.warning("Please enter both a prompt and response.")


elif mode == "Batch Analysis":
    st.header("📊 Batch Analysis")

    st.markdown("""
    Upload a CSV file with columns: `prompt`, `response`, `chatbot`, `language`

    The HMI pipeline will evaluate each response and generate aggregate statistics.
    """)

    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())

        required = {"prompt", "response", "chatbot", "language"}
        if required.issubset(set(df.columns)):
            if st.button("🚀 Run Batch Evaluation", type="primary"):
                pipeline = load_pipeline()
                results = []
                progress = st.progress(0)

                for i, row in df.iterrows():
                    result = pipeline.evaluate(
                        prompt=row["prompt"],
                        response=row["response"],
                        chatbot=row["chatbot"],
                        language=row.get("language", "EN"),
                    )
                    results.append(result.to_dict())
                    progress.progress((i + 1) / len(df))

                results_df = pd.DataFrame(results)
                st.dataframe(results_df)

                # Summary stats
                st.subheader("📈 Summary Statistics")
                summary = results_df.groupby("chatbot")["hmi_score"].agg(
                    ["mean", "median", "std", "min", "max"]
                ).round(2)
                st.dataframe(summary)

                # Distribution chart
                fig = px.histogram(results_df, x="hmi_score", color="chatbot",
                                  nbins=20, title="HMI Score Distribution by Chatbot")
                st.plotly_chart(fig, width="stretch")

                # Download results
                csv_buf = results_df.to_csv(index=False)
                st.download_button(
                    "📥 Download Results CSV",
                    csv_buf,
                    "hmi_results.csv",
                    "text/csv"
                )
        else:
            st.error(f"CSV must contain columns: {required}")


elif mode == "Cross-Chatbot Comparison":
    st.header("🔄 Cross-Chatbot Comparison")

    st.markdown("""
    Compare hallucination profiles across ChatGPT, Gemini, and Microsoft Copilot.
    Upload pre-computed HMI results or enter responses for comparison.
    """)

    uploaded = st.file_uploader("Upload HMI Results CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        if "hmi_score" in df.columns and "chatbot" in df.columns:
            # Overall comparison
            st.subheader("Overall HMI Comparison")
            fig_box = px.box(df, x="chatbot", y="hmi_score", color="chatbot",
                           title="HMI Score Distribution by Chatbot")
            st.plotly_chart(fig_box, width="stretch")

            # Dimension comparison
            dim_cols = [c for c in ["fc_score", "rg_score", "sc_score", "sh_score", "ca_score"]
                       if c in df.columns]

            if dim_cols:
                st.subheader("Dimension-Level Comparison")
                dim_means = df.groupby("chatbot")[dim_cols].mean().reset_index()
                dim_melted = dim_means.melt(id_vars="chatbot", var_name="dimension", value_name="score")
                dim_melted["score"] = dim_melted["score"] * 100

                fig_dim = px.bar(dim_melted, x="dimension", y="score", color="chatbot",
                               barmode="group", title="Mean Dimension Scores by Chatbot")
                st.plotly_chart(fig_dim, width="stretch")

            # Severity distribution
            if "severity" in df.columns:
                st.subheader("Severity Distribution")
                sev_counts = df.groupby(["chatbot", "severity"]).size().reset_index(name="count")
                fig_sev = px.bar(sev_counts, x="chatbot", y="count", color="severity",
                               title="Severity Level Distribution",
                               color_discrete_map={
                                   "MINIMAL": "#2ecc71",
                                   "LOW": "#f39c12",
                                   "MODERATE": "#e67e22",
                                   "HIGH": "#e74c3c",
                                   "CRITICAL": "#8e44ad",
                               })
                st.plotly_chart(fig_sev, width="stretch")

            # Statistical test
            st.subheader("Statistical Analysis")
            st.markdown("""
            **Kruskal-Wallis H-test** (non-parametric comparison across chatbots)

            *To be computed after data collection with scipy.stats.kruskal*
            """)

            chatbots = df["chatbot"].unique()
            if len(chatbots) >= 2:
                from scipy import stats
                groups = [df[df["chatbot"] == c]["hmi_score"].values for c in chatbots]
                groups = [g for g in groups if len(g) >= 2]
                if len(groups) >= 2:
                    h_stat, p_value = stats.kruskal(*groups)
                    st.markdown(f"- **H-statistic:** {h_stat:.4f}")
                    st.markdown(f"- **p-value:** {p_value:.6f}")
                    if p_value < 0.05:
                        st.success("✅ Statistically significant difference detected (p < 0.05)")
                    else:
                        st.info("ℹ️ No statistically significant difference (p ≥ 0.05)")


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>HMI Evaluation Prototype v1.0 | Azfar Rahman | Universiti Malaya 2026</p>
    <p>Built with Streamlit | Based on SelfCheckGPT, DeBERTa, Detoxify, BERTScore</p>
</div>
""", unsafe_allow_html=True)
