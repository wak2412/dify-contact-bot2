import streamlit as st
import requests

API_KEY = "app-5nIMDwep1eheYJWDYh9W6itN"
URL = "https://api.dify.ai/v1/chat-messages"

st.title("問い合わせBot")

mode = st.selectbox(
    "モード選択",
    ["メール作業モード", "メール添削モード", "質問回答モード"]
)

query = ""

if mode == "メール作成モード":
    inquiry = st.text_area("お問い合わせ内容")
    history = st.text_area("過去のやり取り")
    query = f"""
    問い合わせ内容:
    {inquiry}

    過去のやり取り:
    {history}
    """

elif mode == "メール添削モード":
    mail = st.text_area("添削対象メール")
    direction = st.text_input("添削の方向性")

    query = f"""
    添削対象メール:
    {mail}

    添削の方向性:
    {direction}
    """

elif mode == "質問回答モード":
    question = st.text_area("質問内容")
    query = question

if st.button("送信"):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "user": "user123"
    }

    response = requests.post(URL, headers=headers, json=data)

    result = response.json()

    st.write(result["answer"])