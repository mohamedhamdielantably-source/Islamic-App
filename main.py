import streamlit as st
import google.generativeai as genai

# إعداد واجهة التطبيق
st.set_page_config(page_title="تطبيقي الإسلامي", page_icon="🕌")
st.title("تطبيق إسلامي ذكي 🕌")

# إعداد مفتاح الـ API بأمان
if "API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error("حدث خطأ في الاتصال بخدمة الذكاء الاصطناعي.")
        st.stop()
else:
    st.error("مفتاح الـ API غير موجود في إعدادات التطبيق (Secrets).")
    st.stop()

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة في الشات
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    # إضافة سؤال المستخدم للشاشة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد
    with st.chat_message("assistant"):
        try:
            # التحقق من سؤال التعريف بالمطور
            if "مين" in prompt and ("صممك" in prompt or "مطورك" in prompt or "صمم" in prompt):
                response_text = "لقد صممني البشمهندس محمد حمدي، وأنا هنا لمساعدتك في أي استفسارات دينية."
            else:
                # الرد الذكي من Gemini
                response = model.generate_content(prompt)
                response_text = response.text
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            
        except Exception as e:
            st.error("عذراً، حدث خطأ أثناء التواصل مع الذكاء الاصطناعي، يرجى المحاولة مرة أخرى.")
