import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🇰🇷 외국인이 좋아하는 서울 주요 관광지 TOP10")

st.markdown(
    """
서울의 인기 관광지를 지도에서 클릭해보세요.  
클릭하면 아래에 가까운 지하철역과 주변 놀거리가 표시됩니다.
"""
)

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "fun": "한복체험, 북촌한옥마을 산책, 전통카페 방문"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.982193,
        "subway": "명동역(4호선)",
        "fun": "K-뷰티 쇼핑, 길거리 음식, 야간 쇼핑"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "fun": "서울 야경 감상, 케이블카, 사랑의 자물쇠"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "subway": "안국역(3호선)",
        "fun": "전통 한옥 골목 산책, 공방 체험, 카페 투어"
    },
    {
        "name": "홍대거리",
        "lat": 37.556336,
        "lon": 126.922031,
        "subway": "홍대입구역(2호선)",
        "fun": "버스킹 공연, 맛집 탐방, 클럽 문화"
    },
    {
        "name": "강남",
        "lat": 37.497952,
        "lon": 127.027619,
        "subway": "강남역(2호선)",
        "fun": "쇼핑, K-POP 체험, 트렌디 카페"
    },
    {
        "name": "롯데월드",
        "lat": 37.511115,
        "lon": 127.098167,
        "subway": "잠실역(2호선)",
        "fun": "놀이기구, 실내 아이스링크, 석촌호수 산책"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "subway": "동대문역사문화공원역",
        "fun": "야경 사진, 전시회 관람, 야시장"
    },
    {
        "name": "한강공원",
        "lat": 37.528726,
        "lon": 126.932243,
        "subway": "여의나루역(5호선)",
        "fun": "치맥, 자전거 라이딩, 한강 유람선"
    },
    {
        "name": "익선동",
        "lat": 37.574341,
        "lon": 126.989572,
        "subway": "종로3가역",
        "fun": "감성 카페, 한옥 맛집, 포토존 투어"
    },
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    popup_html = f"""
    <b>{place['name']}</b><br>
    클릭 후 아래 정보를 확인하세요.
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(
    m,
    width=1000,
    height=600
)

st.divider()

# 클릭 이벤트 처리
clicked = map_data.get("last_object_clicked")

if clicked:
    lat = clicked["lat"]
    lon = clicked["lng"]

    selected_place = None

    for place in places:
        if abs(place["lat"] - lat) < 0.0001 and abs(place["lon"] - lon) < 0.0001:
            selected_place = place
            break

    if selected_place:
        st.subheader(f"📍 {selected_place['name']}")

        st.success(
            f"🚇 가까운 지하철역: {selected_place['subway']} | "
            f"🎉 놀거리: {selected_place['fun']}"
        )

else:
    st.info("지도에서 관광지를 클릭해보세요.")
