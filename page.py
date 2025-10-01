# this is test page

import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────────

st.set_page_config(page_title="다이렉트 굿앤굿어린이종합보험Q(태아)", layout="wide")

# CSS 커스텀
st.markdown("""
    <style>
    .segmented-control {
        display: flex;
        border-radius: 25px;
        background-color: #f5f5f5;
        padding: 5px;
        width: fit-content;
        margin: auto;
    }
    .segment {
        padding: 8px 20px;
        border-radius: 20px;
        margin: 0 2px;
        cursor: pointer;
        font-weight: 600;
        color: #666;
        background-color: transparent;
        transition: all 0.3s ease;
    }
    .segment.selected {
        background-color: white;
        color: black;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# 선택 상태 유지
if "selected" not in st.session_state:
    st.session_state.selected = "태아"

options = ["태아", "어린이 (0~15세)"]

# 커스텀 UI 출력
cols = st.columns(len(options))
for i, option in enumerate(options):
    if cols[i].button(option, key=option):
        st.session_state.selected = option

# 선택된 값 스타일링
st.markdown(f"""
<div class="segmented-control">
    {''.join([f'<div class="segment {"selected" if st.session_state.selected == opt else ""}">{opt}</div>' for opt in options])}
</div>
""", unsafe_allow_html=True)

st.write("현재 선택:", st.session_state.selected)
