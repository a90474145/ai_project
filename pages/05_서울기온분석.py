import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="Seoul Temperature Analysis", layout="wide")

st.title("Seoul Temperature Analysis")

# 데이터 불러오기
@st.cache_data

def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 컬럼 이름 변경
    df.columns = ["date", "station", "avg_temp", "min_temp", "max_temp"]

    # 날짜 변환
    df["date"] = pd.to_datetime(df["date"])

    # 연, 월, 일 컬럼 생성
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    return df


df = load_data()

# 월, 일 선택
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox("Select Month", sorted(df["month"].unique()))

with col2:
    selected_day = st.selectbox("Select Day", list(range(1, 32)))

# 데이터 필터링
filtered_df = df[
    (df["month"] == selected_month) &
    (df["day"] == selected_day)
].copy()

# 존재하지 않는 날짜 처리
if filtered_df.empty:
    st.warning("No data available for this date.")

else:
    filtered_df = filtered_df.sort_values("year")

    # 그래프 생성
    fig = go.Figure()

    # 최고기온
    fig.add_trace(
        go.Scatter(
            x=filtered_df["year"],
            y=filtered_df["max_temp"],
            mode="lines",
            name="Max Temperature",
            line=dict(color="hotpink", width=3),
            hovertemplate="Year: %{x}<br>Max Temp: %{y}°C<extra></extra>"
        )
    )

    # 최저기온
    fig.add_trace(
        go.Scatter(
            x=filtered_df["year"],
            y=filtered_df["min_temp"],
            mode="lines",
            name="Min Temperature",
            line=dict(color="lightblue", width=3),
            hovertemplate="Year: %{x}<br>Min Temp: %{y}°C<extra></extra>"
        )
    )

    # 레이아웃 설정
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
        filtered_df[["year", "min_temp", "max_temp"]].reset_index(drop=True),
        use_container_width=True
    )
