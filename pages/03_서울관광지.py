import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지", layout="wide")

st.title("🇰🇷 서울 인기 관광지 TOP10")

places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "fun": "한복체험, 북촌 산책"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.982193,
        "subway": "명동역(4호선)",
        "fun": "쇼핑, 길거리 음식"
    },
    {
        "name": "홍대",
        "lat": 37.556336,
        "lon": 126.922031,
        "subway": "홍대입구역(2호선)",
        "fun": "버스킹, 맛집"
    },
    {
        "name": "강남",
        "lat": 37.497952,
        "lon": 127.027619,
        "subway": "강남역(2호선)",
        "fun": "카페, 쇼핑"
    },
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in places:
    folium.Marker(
        [place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=place["name"]
    ).add_to(m)

# 지도 표시
map_data = st_folium(
    m,
    width=1000,
    height=600
)

# 클릭 정보
clicked = map_data.get("last_object_clicked")

if clicked:
    lat = clicked["lat"]
    lng = clicked["lng"]

    for place in places:
        if (
            abs(place["lat"] - lat) < 0.0001
            and abs(place["lon"] - lng) < 0.0001
        ):
            st.success(
                f"🚇 가까운 역: {place['subway']} | 🎉 놀거리: {place['fun']}"
            )
