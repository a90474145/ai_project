import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# 페이지 설정
# ---------------------------------
st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

st.title("서울시 행정구별 인구수")

# ---------------------------------
# 한글 폰트 설정
# ---------------------------------
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# ---------------------------------
# CSV 파일 읽기
# ---------------------------------
encodings = ["cp949", "euc-kr", "utf-8"]

df = None

for enc in encodings:
    try:
        df = pd.read_csv("population.csv", encoding=enc)
        st.success(f"성공한 인코딩: {enc}")
        break
    except:
        pass

if df is None:
    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()

# ---------------------------------
# 행정구 컬럼
# ---------------------------------
district_col = df.columns[0]

# ---------------------------------
# 나이 컬럼 찾기
# ---------------------------------
age_columns = []

for col in df.columns:

    col_str = str(col)

    if "세" in col_str:
        age_columns.append(col)

# ---------------------------------
# 사이드바
# ---------------------------------
st.sidebar.header("메뉴")

graph_type = st.sidebar.radio(
    "그래프 선택",
    [
        "행정구별 그래프",
        "10살 간격 TOP10 그래프"
    ]
)

# =================================
# 1. 행정구별 그래프
# =================================
if graph_type == "행정구별 그래프":

    districts = df[district_col].tolist()

    selected_district = st.selectbox(
        "행정구를 선택하세요",
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

            ages.append(col)
            populations.append(int(value))

        except:
            pass

    # ---------------------------------
    # 그래프
    # ---------------------------------
    fig, ax = plt.subplots(figsize=(16, 6))

    # 회색 배경
    fig.patch.set_facecolor("lightgray")
    ax.set_facecolor("lightgray")

    # 빨간색 꺾은선
    ax.plot(
        ages,
        populations,
        color="red",
        linewidth=2,
        marker="o"
    )

    # 제목
    ax.set_title(
        "서울시 행정구별 인구수",
        fontsize=18
    )

    # 축 이름
    ax.set_xlabel("age", fontsize=12)
    ax.set_ylabel("population", fontsize=12)

    # x축 회전
    plt.xticks(rotation=90)

    # 여백 자동 조정
    plt.tight_layout()

    # 출력
    st.pyplot(fig)

# =================================
# 2. 10살 간격 TOP10 그래프
# =================================
else:

    age_group = st.selectbox(
        "10살 간격 나이대를 선택하세요",
        [
            "0~9세",
            "10~19세",
            "20~29세",
            "30~39세",
            "40~49세",
            "50~59세",
            "60~69세",
            "70~79세",
            "80~89세",
            "90세 이상"
        ]
    )

    # ---------------------------------
    # 나이대 매핑
    # ---------------------------------
    age_mapping = {
        "0~9세": list(range(0, 10)),
        "10~19세": list(range(10, 20)),
        "20~29세": list(range(20, 30)),
        "30~39세": list(range(30, 40)),
        "40~49세": list(range(40, 50)),
        "50~59세": list(range(50, 60)),
        "60~69세": list(range(60, 70)),
        "70~79세": list(range(70, 80)),
        "80~89세": list(range(80, 90)),
        "90세 이상": list(range(90, 100))
    }

    selected_ages = age_mapping[age_group]

    # ---------------------------------
    # 각 행정구 인구 계산
    # ---------------------------------
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
        columns=["행정구", "인구수"]
    )

    # ---------------------------------
    # 상위 10개
    # ---------------------------------
    result_df = result_df.sort_values(
        by="인구수",
        ascending=False
    ).head(10)

    # ---------------------------------
    # 그래프
    # ---------------------------------
    fig, ax = plt.subplots(figsize=(14, 6))

    # 회색 배경
    fig.patch.set_facecolor("lightgray")
    ax.set_facecolor("lightgray")

    # 빨간색 꺾은선
    ax.plot(
        result_df["행정구"],
        result_df["인구수"],
        color="red",
        linewidth=3,
        marker="o"
    )

    # 제목
    ax.set_title(
        "서울시 행정구별 인구수",
        fontsize=18
    )

    # 축 이름
    ax.set_xlabel("age", fontsize=12)
    ax.set_ylabel("population", fontsize=12)

    # x축 회전
    plt.xticks(rotation=45)

    # 여백 자동 조정
    plt.tight_layout()

    # 출력
    st.pyplot(fig)
