import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Seoul Public WiFi Analysis",
    layout="wide"
)

st.title("📶 Seoul Public WiFi Analysis")

# CSV 읽기
@st.cache_data
def load_data():
    return pd.read_csv("seoul.csv", encoding="utf-8")

df = load_data()

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", f"{len(df):,}")

with col2:
    st.metric("Districts", df["설치시군구명"].nunique())

with col3:
    st.metric("Facility Types", df["설치시설구분명"].nunique())

st.divider()

# -------------------------------
# District Analysis
# -------------------------------

st.header("District Analysis")

district_counts = (
    df["설치시군구명"]
    .value_counts()
    .reset_index()
)

district_counts.columns = ["District", "Count"]

fig1 = px.bar(
    district_counts,
    x="District",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Turbo"
)

fig1.update_layout(
    xaxis_title="District",
    yaxis_title="WiFi Count",
    showlegend=False
)

fig1.update_traces(
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

# -------------------------------
# Facility Type Analysis
# -------------------------------

st.header("Facility Type Analysis")

facility_counts = (
    df["설치시설구분명"]
    .value_counts()
    .reset_index()
)

facility_counts.columns = ["Facility Type", "Count"]

fig2 = px.bar(
    facility_counts,
    x="Facility Type",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Viridis"
)

fig2.update_layout(
    xaxis_title="Facility Type",
    yaxis_title="WiFi Count",
    showlegend=False
)

fig2.update_traces(
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# -------------------------------
# Yearly Trend
# -------------------------------

st.header("Installation Trend by Year")

df["설치연월"] = df["설치연월"].astype(str)

df["Year"] = df["설치연월"].str[:4]

year_counts = (
    df["Year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_counts.columns = ["Year", "Count"]

fig3 = px.bar(
    year_counts,
    x="Year",
    y="Count",
    color="Count",
    text="Count",
    color_continuous_scale="Plasma"
)

fig3.update_layout(
    xaxis_title="Year",
    yaxis_title="Installation Count",
    showlegend=False
)

fig3.update_traces(
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# -------------------------------
# District Filter
# -------------------------------

st.header("District Detail Analysis")

selected_district = st.selectbox(
    "Select District",
    sorted(df["설치시군구명"].dropna().unique())
)

filtered = df[df["설치시군구명"] == selected_district]

detail = (
    filtered["설치시설구분명"]
    .value_counts()
    .reset_index()
)

detail.columns = ["Facility Type", "Count"]

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
    showlegend=False
)

fig4.update_traces(
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
)

st.plotly_chart(fig4, use_container_width=True)

st.success("Interactive analysis completed.")
