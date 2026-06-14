import streamlit as st
import requests

st.set_page_config(page_title="تطبيقي الإسلامي", page_icon="🕌")
st.title("تطبيق إسلامي ذكي 🕌")
st.write("أنا مساعدك الإسلامي، صممك البشمهندس محمد حمدي.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسألني أي سؤال في الدين..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # طلب الإجابة من خدمة ذكاء اصطناعي عامة ومجانية
        try:
            # رابط لخدمة ذكاء اصطناعي مجانية بتجاوب على الأسئلة الدينية
            api_url = f"https://api.duckduckgo.com/?q={prompt}&format=json"
            response = requests.get(api_url).json()
            
            answer = response.get("AbstractText")
            if not answer:
                answer = "عذراً، لم أجد إجابة دقيقة. حاول صياغة السؤال بشكل أوضح، أو أنا صممني البشمهندس محمد حمدي لخدمتك."
            
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
        except Exception:
            st.markdown("أنا صممني البشمهندس محمد حمدي، وأنا جاهز للرد، لكن حدث خطأ بسيط في الاتصال. حاول مجدداً!")
