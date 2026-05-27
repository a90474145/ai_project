import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Seoul Temperature Analysis",
    layout="wide"
)

st.title("Seoul Temperature Analysis")

# 데이터 불러오기
@st.cache_data
def load_data():

    # cp949 먼저 시도
    try:
        df = pd.read_csv("seoul.csv", encoding="cp949")
    except:
        # 실패하면 utf-8 시도
        df = pd.read_csv("seoul.csv", encoding="utf-8")

    # 컬럼 이름 변경
    df.columns = [
        "date",
        "station",
        "avg_temp",
        "min_temp",
        "max_temp"
    ]

    # 공백 제거
    df["date"] = df["date"].astype(str).str.strip()

    # 날짜 변환
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # 날짜 변환 실패한 행 제거
    df = df.dropna(subset=["date"])

    # 숫자형 변환
    df["min_temp"] = pd.to_numeric(
        df["min_temp"],
        errors="coerce"
    )

    df["max_temp"] = pd.to_numeric(
        df["max_temp"],
        errors="coerce"
    )

    # 연도/월/일 추출
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    return df


df = load_data()

# 월 선택
month_list = sorted(df["month"].dropna().unique())

selected_month = st.selectbox(
    "Select Month",
    month_list
)

# 선택된 월에 존재하는 일만 표시
day_list = sorted(
    df[df["month"] == selected_month]["day"]
    .dropna()
    .unique()
)

selected_day = st.selectbox(
    "Select Day",
    day_list
)

# 데이터 필터링
filtered = df[
    (df["month"] == selected_month) &
    (df["day"] == selected_day)
].sort_values("year")

st.subheader(
    f"Temperature Trend on {selected_month}/{selected_day}"
)

# 그래프 생성
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=filtered["year"],
        y=filtered["max_temp"],
        mode="lines+markers",
        name="Max Temperature",
        line=dict(
            color="hotpink",
            width=3
        ),
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
        line=dict(
            color="lightblue",
            width=3
        ),
        marker=dict(size=6),
        hovertemplate=
        "Year: %{x}<br>" +
        "Min Temp: %{y}°C<extra></extra>"
    )
)

# 레이아웃 설정
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Temperature (°C)",
    hovermode="x unified",
    template="plotly_white",
    height=650
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# 데이터 테이블
st.subheader("Filtered Data")

st.dataframe(
    filtered[
        [
            "year",
            "min_temp",
            "max_temp"
        ]
    ].reset_index(drop=True),
    use_container_width=True
)
