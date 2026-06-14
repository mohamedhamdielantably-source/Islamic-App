import streamlit as st

st.set_page_config(page_title="تطبيقي الإسلامي", page_icon="🕌")
st.title("تطبيق إسلامي ذكي 🕌")

# 1. قائمة الأسئلة المبرمجة (القاعدة الثابتة)
data = {
    "أركان الإسلام": "أركان الإسلام خمسة: الشهادتان، الصلاة، الزكاة، الصوم، والحج.",
    "من صممك": "صمم هذا التطبيق البشمهندس محمد حمدي ليكون رفيقاً إيمانياً.",
    "أركان الإيمان": "الإيمان بالله، وملائكته، وكتبه، ورسله، واليوم الآخر، والقدر خيره وشره."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # البحث في الأسئلة المبرمجة
        response_text = data.get(prompt, None)
        
        if response_text:
            st.markdown(response_text)
        else:
            # الحل الوسط: لو مش عارف السؤال، يوجهه ليك!
            st.markdown("عذراً، هذا السؤال يحتاج لمراجعة دقيقة. هل تود إرسال سؤالك مباشرة للبشمهندس محمد حمدي؟")
            st.link_button("إرسال السؤال للبشمهندس محمد", "https://wa.me/201009218581") # حط رقم الواتساب بتاعك هنا
            response_text = "تم توجيه المستخدم للمطور."
            
        st.session_state.messages.append({"role": "assistant", "content": response_text})
