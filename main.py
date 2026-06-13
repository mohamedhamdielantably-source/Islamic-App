import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("خطأ في إعدادات API Key.")
    st.stop()

st.title("تطبيق إسلامي ذكي 🕌")
st.write("أهلاً بك! أنا مساعدك الذكي، اسألني في أي شيء ديني وسأجيبك.")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد مع تعليمات خاصة باسمك
    with st.chat_message("assistant"):
        try:
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash',
                system_instruction="أنت مساعد ذكي متخصص في العلوم الإسلامية. إذا سألك المستخدم من صممك أو من مطورك، أجب بكل فخر: 'لقد صممني البشمهندس محمد حمدي'."
            )
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("عذراً، حدث خطأ أثناء التواصل مع الذكاء الاصطناعي.")
