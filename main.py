import streamlit as st
import yaml

st.set_page_config(layout="wide")

# YAML 파일을 로드합니다.
with open("position.yaml", "r") as file:
    data = yaml.safe_load(file)

# sidebar ---------------------------------------

st.sidebar.markdown("<h1 style='text-align: center; color: black;'>이동할 경로를 클릭해주세요.</h1>", unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("")

if st.sidebar.button("도서관으로 이동하기"):
    print(f"x 값: {data['도서관']['x']}")
    print(f"y 값: {data['도서관']['y']}")
    print(f"z 값: {data['도서관']['z']}")
    st.experimental_rerun()

if st.sidebar.button("헬스장으로 이동하기"):
    print(f"x 값: {data['임베실']['x']}")
    print(f"y 값: {data['임베실']['y']}")
    print(f"z 값: {data['임베실']['z']}")
    st.experimental_rerun()

# mid ----------------------------------------------

col1, col2 = st.columns([1, 1])  # 2개의 열을 생성합니다.
col3 = st.empty()  # col3는 비어 있는 상태로 생성합니다.

with col1:
    st.title('here is column1')

with col2:
    st.title('here is column2')
    st.checkbox('this is checkbox1 in col2 ')

# '현재 상황'의 타이틀을 넣습니다.
st.title('현재 상황')

# 큰 네모 박스를 생성하여 텍스트를 넣습니다.
st.success('작업이 성공했을때 사용하자')
