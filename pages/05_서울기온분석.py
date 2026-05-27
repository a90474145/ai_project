import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Seoul Temperature Analysis", layout="wide")

st.title("Seoul Temperature Analysis")

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 컬럼 이름 변경
    df.columns = ["date", "station", "avg_temp", "min_temp", "max_temp"]

    # 날짜 변환
    df["date"] = pd.to_datetime(df["date"])

    # 연도/월/일 추출
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    return df

df = load_data()

# 월/일 선택
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "Select Month",
        sorted(df["month"].unique())
    )

with col2:
    selected_day = st.selectbox(
        "Select Day",
        sorted(
            df[df["month"] == selected_month]["day"].unique()
        )
    )

# 선택된 날짜 필터링
filtered = df[
    (df["month"] == selected_month) &
    (df["day"] == selected_day)
].sort_values("year")

st.subheader(
    f"Temperature Trend on {selected_month}/{selected_day}"
)

# Plotly 그래프
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=filtered["year"],
        y=filtered["max_temp"],
        mode="lines+markers",
        name="Max Temperature",
        line=dict(color="hotpink", width=3),
        marker=dict(size=6),
        hovertemplate=
        "Year: %{x}<br>" +
        "Max Temp: %{y}°C<extra></extra>"
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=filtered["year"],
        y=filtered["min_temp"],
        mode="lines+markers",
        name="Min Temperature",
        line=dict(color="lightblue", width=3),
        marker=dict(size=6),
        hovertemplate=
        "Year: %{x}<br>" +
        "Min Temp: %{y}°C<extra></extra>"
    )
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Temperature (°C)",
    hovermode="x unified",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블
st.subheader("Filtered Data")
st.dataframe(
    filtered[
        ["year", "min_temp", "max_temp"]
    ].reset_index(drop=True),
    use_container_width=True
)
