import streamlit as st

if 'content' not in st.session_state:
    st.session_state.content = "初期内容"

if st.button('リセット'):
    st.session_state.content = ""  # 内容を空に
    st.experimental_rerun()

st.write(st.session_state.content)

# 他のプログラム
# 必要な処理をここに書く
