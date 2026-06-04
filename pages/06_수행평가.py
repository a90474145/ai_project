import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Seoul Public WiFi Analysis",
    layout="wide"
)

st.title("📶 Seoul Public WiFi Analysis")

# -----------------------
# Load Data
# -----------------------

@st.cache_data
def load_data():

    current_file = Path(__file__)

    project_root = current_file.parent.parent

    csv_path = project_root / "seoul.csv"

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp949",
        "euc-kr"
    ]

    for enc in encodings:
        try:
            return pd.read_csv(csv_path, encoding=enc)
        except:
            pass

    raise Exception("Cannot read seoul.csv")

df = load_data()

# -----------------------
# Overview
# -----------------------

st.header("Dataset Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Records",
        f"{len(df):,}"
    )

with c2:
    st.metric(
        "Districts",
        df["설치시군구명"].nunique()
    )

with c3:
    st.metric(
        "Facility Types",
        df["설치시설구분명"].nunique()
    )

st.divider()

# -----------------------
# District Analysis
# -----------------------

st.header("WiFi Installations by District")

district = (
    df["설치시군구명"]
    .value_counts()
    .reset_index()
)

district.columns = [
    "District",
    "Count"
]

fig1 = px.bar(
    district,
    x="District",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Turbo"
)

fig1.update_layout(
    xaxis_title="District",
    yaxis_title="Count",
    title=None
)

fig1.update_traces(
    textposition="outside",
    hovertemplate=
    "<b>%{x}</b><br>Count: %{y:,}<extra></extra>"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# -----------------------
# Facility Analysis
# -----------------------

st.header("WiFi Installations by Facility Type")

facility = (
    df["설치시설구분명"]
    .value_counts()
    .reset_index()
)

facility.columns = [
    "Facility Type",
    "Count"
]

fig2 = px.bar(
    facility,
    x="Facility Type",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Viridis"
)

fig2.update_layout(
    xaxis_title="Facility Type",
    yaxis_title="Count",
    title=None
)

fig2.update_traces(
    textposition="outside",
    hovertemplate=
    "<b>%{x}</b><br>Count: %{y:,}<extra></extra>"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# -----------------------
# Year Analysis
# -----------------------

st.header("Installation Trend")

df["설치연월"] = df["설치연월"].astype(str)

df["Year"] = df["설치연월"].str[:4]

yearly = (
    df["Year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

yearly.columns = [
    "Year",
    "Count"
]

fig3 = px.bar(
    yearly,
    x="Year",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Plasma"
)

fig3.update_layout(
    xaxis_title="Year",
    yaxis_title="Installations",
    title=None
)

fig3.update_traces(
    textposition="outside",
    hovertemplate=
    "<b>%{x}</b><br>Count: %{y:,}<extra></extra>"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# -----------------------
# District Filter
# -----------------------

st.header("District Detail")

selected = st.selectbox(
    "Select District",
    sorted(df["설치시군구명"].dropna().unique())
)

filtered = df[
    df["설치시군구명"] == selected
]

detail = (
    filtered["설치시설구분명"]
    .value_counts()
    .reset_index()
)

detail.columns = [
    "Facility Type",
    "Count"
]

fig4 = px.bar(
    detail,
    x="Facility Type",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Rainbow"
)

fig4.update_layout(
    xaxis_title="Facility Type",
    yaxis_title="Count",
    title=None
)

fig4.update_traces(
    textposition="outside",
    hovertemplate=
    "<b>%{x}</b><br>Count: %{y:,}<extra></extra>"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)
