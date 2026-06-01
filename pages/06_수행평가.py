import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Seoul Public WiFi Analysis",
    layout="wide"
)

st.title("📶 Seoul Public WiFi Analysis")

uploaded_file = st.file_uploader(
    "Upload Seoul WiFi CSV",
    type=["csv"]
)

if uploaded_file is not None:

    @st.cache_data
    def load_data(file):

        encodings = [
            "utf-8",
            "utf-8-sig",
            "cp949",
            "euc-kr"
        ]

        for enc in encodings:
            try:
                file.seek(0)
                return pd.read_csv(file, encoding=enc)
            except:
                continue

        raise Exception("Unable to read CSV file.")

    df = load_data(uploaded_file)

    st.success("Data loaded successfully!")

    # ------------------
    # Dataset Overview
    # ------------------

    st.subheader("Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Records", f"{len(df):,}")

    c2.metric(
        "Districts",
        df["설치시군구명"].nunique()
    )

    c3.metric(
        "Facility Types",
        df["설치시설구분명"].nunique()
    )

    st.divider()

    # ------------------
    # District Analysis
    # ------------------

    district = (
        df["설치시군구명"]
        .value_counts()
        .reset_index()
    )

    district.columns = ["District", "Count"]

    fig1 = px.bar(
        district,
        x="District",
        y="Count",
        color="Count",
        text="Count",
        color_continuous_scale="Turbo"
    )

    fig1.update_traces(
        hovertemplate=
        "<b>%{x}</b><br>Count: %{y}<extra></extra>"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.divider()

    # ------------------
    # Facility Analysis
    # ------------------

    facility = (
        df["설치시설구분명"]
        .value_counts()
        .reset_index()
    )

    facility.columns = ["Facility", "Count"]

    fig2 = px.bar(
        facility,
        x="Facility",
        y="Count",
        color="Count",
        text="Count",
        color_continuous_scale="Viridis"
    )

    fig2.update_traces(
        hovertemplate=
        "<b>%{x}</b><br>Count: %{y}<extra></extra>"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    # ------------------
    # Year Analysis
    # ------------------

    if "설치연월" in df.columns:

        df["Year"] = (
            df["설치연월"]
            .astype(str)
            .str[:4]
        )

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

        fig3.update_traces(
            hovertemplate=
            "<b>%{x}</b><br>Count: %{y}<extra></extra>"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

else:
    st.info("Please upload a CSV file.")
