import streamlit as st

# 교육용 컨텐츠
contents = {
    1: {"title": "1. API 키가 뭔지 먼저 알기", 
        "body": "API 키는 컴퓨터 프로그램이 서로 얘기할 때 쓰는 '비밀 열쇠'입니다.\n"
                "집 문을 열려면 열쇠가 필요하듯, 프로그램이 OpenAI 서버에 요청하려면\n"
                "'나 허락받은 사람이에요!'라는 증명이 필요합니다.\n"
                "그 증명 도구가 API 키입니다."},
    2: {"title": "2. API 키를 어디서 받는지", 
        "body": "1. OpenAI 웹사이트 로그인\n2. 'API Keys' 메뉴에서 'Create new secret key' 클릭\n"
                "3. 발급된 긴 문자열(예: sk-XXXX...)이 API 키입니다.\n\n⚠ 주의:\n"
                "- 다른 사람과 공유하지 마세요.\n- 잃어버리면 새로 발급받아야 합니다."},
    3: {"title": "3. API 키를 어떻게 사용하는지", 
        "body": "파이썬 예시:\n\n"
                "```python\n"
                "import openai\n"
                "openai.api_key = \"발급받은_API_키\"\n"
                "response = openai.ChatCompletion.create(\n"
                "    model=\"gpt-3.5-turbo\",\n"
                "    messages=[{\"role\":\"user\",\"content\":\"안녕\"}]\n"
                ")\n"
                "print(response.choices[0].message.content)\n"
                "```"},
    4: {"title": "4. 사용 순서 정리", 
        "body": "1. API 키 받기\n2. 코드에 키 입력\n3. 프로그램이 서버에 키를 보여줌\n4. 서버가 요청을 처리하고 응답"},
    5: {"title": "5. 기억하기 쉬운 비유", 
        "body": "- OpenAI 서버 = 도서관 사서\n- API 키 = 도서관 회원증\n- 내 프로그램 = 책 빌리러 온 사람\n"
                "회원증 없으면 책 못 빌리고,\n다른 사람 회원증 쓰면 규칙 위반입니다."},
    6: {"title": "API 키 개념 이해하기", 
        "body": "API 키는 비밀 열쇠처럼, 프로그램이 OpenAI에 접근할 수 있게 해주는 인증 도구입니다."},
    7: {"title": "API 키 필요 여부 표", 
        "body": "| 상황 | API 키 필요? | 예제 |\n|------|--------------|------|\n"
                "| OpenAI 공식 챗GPT 웹사이트 | ❌ 필요 없음 | chat.openai.com |\n"
                "| 내가 만든 파이썬 코드 | ✅ 필요함 | 구글 코랩에서 챗봇 |\n"
                "| 내가 만든 웹/앱 | ✅ 필요함 | React 챗봇 |\n"
                "| 노코드 툴 | 보통 ✅ 필요함 | Zapier, Bubble |\n"
                "| 타인 앱/웹 | ❌ 필요 없음 | Notion AI 등"},
    8: {"title": "구글 코렙 예제 코드", 
        "body": "```python\n"
                "!pip install openai\n"
                "from getpass import getpass\n"
                "from openai import OpenAI\n\n"
                "OPENAI_API_KEY = getpass(\"🔑 API 키를 입력하세요: \")\n"
                "client = OpenAI(api_key=OPENAI_API_KEY)\n\n"
                "response = client.chat.completions.create(\n"
                "    model=\"gpt-3.5-turbo\",\n"
                "    messages=[{\"role\": \"system\", \"content\": \"안녕\"}]\n"
                ")\n"
                "print(response.choices[0].message.content)\n"
                "```"}
}

# Streamlit UI
st.set_page_config(layout="wide")
st.title("📚 OpenAI API 키 교육 앱 (Streamlit 버전)")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("주제 목록")
    # 버튼 목록 만들기
    for key in contents:
        if st.button(contents[key]["title"]):
            st.session_state["selected"] = key

with col2:
    st.subheader("설명")
    if "selected" in st.session_state:
        st.markdown(contents[st.session_state["selected"]]["body"])
    else:
        st.info("왼쪽에서 주제를 선택하세요.")
