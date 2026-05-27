import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# Page Setting
# ---------------------------------
st.set_page_config(
    page_title="Seoul Population",
    layout="wide"
)

st.title("Seoul Population Dashboard")

# ---------------------------------
# CSV Load
# ---------------------------------
encodings = ["cp949", "euc-kr", "utf-8"]

df = None

for enc in encodings:
    try:
        df = pd.read_csv("population.csv", encoding=enc)
        break
    except:
        pass

if df is None:
    st.error("Cannot read CSV file.")
    st.stop()

# ---------------------------------
# District Column
# ---------------------------------
district_col = df.columns[0]

# ---------------------------------
# Age Columns
# ---------------------------------
age_columns = []

for col in df.columns:

    col_str = str(col)

    if "세" in col_str:
        age_columns.append(col)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.header("Menu")

graph_type = st.sidebar.radio(
    "Select Graph",
    [
        "District Graph",
        "Age Group TOP10"
    ]
)

# =================================
# 1. District Graph
# =================================
if graph_type == "District Graph":

    districts = df[district_col].tolist()

    selected_district = st.selectbox(
        "Select District",
        districts
    )

    selected_row = df[df[district_col] == selected_district]

    ages = []
    populations = []

    for col in age_columns:

        try:
            value = str(
                selected_row[col].values[0]
            ).replace(",", "")

            age_text = str(col).replace("세", "")

            ages.append(age_text)
            populations.append(int(value))

        except:
            pass

    graph_df = pd.DataFrame({
        "age": ages,
        "population": populations
    })

    # ---------------------------------
    # Plotly Graph
    # ---------------------------------
    fig = px.line(
        graph_df,
        x="age",
        y="population",
        markers=True
    )

    # Background Color
    fig.update_layout(
        plot_bgcolor="lightgray",
        paper_bgcolor="lightgray",

        # title 제거
        title=None,

        xaxis_title="age",
        yaxis_title="population"
    )

    # Line Color
    fig.update_traces(
        line=dict(color="red", width=3)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =================================
# 2. Age Group TOP10
# =================================
else:

    age_group = st.selectbox(
        "Select Age Group",
        [
            "0~9",
            "10~19",
            "20~29",
            "30~39",
            "40~49",
            "50~59",
            "60~69",
            "70~79",
            "80~89",
            "90+"
        ]
    )

    age_mapping = {
        "0~9": list(range(0, 10)),
        "10~19": list(range(10, 20)),
        "20~29": list(range(20, 30)),
        "30~39": list(range(30, 40)),
        "40~49": list(range(40, 50)),
        "50~59": list(range(50, 60)),
        "60~69": list(range(60, 70)),
        "70~79": list(range(70, 80)),
        "80~89": list(range(80, 90)),
        "90+": list(range(90, 100))
    }

    selected_ages = age_mapping[age_group]

    result = []

    for idx, row in df.iterrows():

        total = 0

        for age in selected_ages:

            age_text = f"{age}세"

            for col in df.columns:

                if age_text in str(col):

                    try:
                        value = str(row[col]).replace(",", "")
                        total += int(value)

                    except:
                        pass

        result.append(
            [row[district_col], total]
        )

    result_df = pd.DataFrame(
        result,
        columns=["district", "population"]
    )

    result_df = result_df.sort_values(
        by="population",
        ascending=False
    ).head(10)

    # ---------------------------------
    # Plotly Graph
    # ---------------------------------
    fig = px.line(
        result_df,
        x="district",
        y="population",
        markers=True
    )

    # Background Color
    fig.update_layout(
        plot_bgcolor="lightgray",
        paper_bgcolor="lightgray",

        # title 제거
        title=None,

        xaxis_title="district",
        yaxis_title="population"
    )

    # Line Color
    fig.update_traces(
        line=dict(color="red", width=3)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
