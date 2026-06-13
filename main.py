import streamlit as st
import google.generativeai as genai

# هنا السطر اللي بيجيب المفتاح من الـ Secrets اللي إحنا حفظناها
API_KEY = st.secrets["API_KEY"]
genai.configure(api_key=API_KEY)
from google.generativeai import types

# مفتاحك السليم والشغال
import streamlit as st
API_KEY = st.secrets["API_KEY"]

chat_box = None
user_input = None

# ربط العميل بالمكتبة الرسمية
genai.configure(api_key=API_KEY)

def send_message(e):
    page = e.page if e.page else e.control.page
    user_question = user_input.value.strip() if user_input.value else ""
    if not user_question:
        return
    
    chat_box.controls.append(
        ft.Container(
            content=ft.Text(f"أنت: {user_question}", color="#ffffff", selectable=True),
            bgcolor="#1e293b",
            padding=10,
            border_radius=8
        )
    )
    user_input.value = ""
    page.update()

    try:
        # هنا بنحط التعليمات اللي بتجبر البوت يفتخر بالبشمهندس محمد حمدي
        config = types.GenerateContentConfig(
            system_instruction="أنت مساعد إسلامي ذكي، صممك وطورك البشمهندس محمد حمدي. إذا سألك أي شخص عن من صممك أو طورك أو صنعك، يجب أن تجيب بفخر وثقة: 'صممني المساعد الإسلامي الذكي البشمهندس محمد حمدي 😎'."
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_question,
            config=config # ضفنا التعليمات هنا
        )
        bot_response = response.text
        
    except Exception as ex:
        bot_response = f"عطل في السيرفر: {str(ex)}"

    chat_box.controls.append(
        ft.Container(
            content=ft.Text(f"المساعد الإسلامي: {bot_response}", color="#ffffff", selectable=True),
            bgcolor="#065f46",
            padding=10,
            border_radius=8
        )
    )
    page.update()

def main(page: ft.Page):
    global user_input, chat_box
    page.title = "المساعد الإسلامي الذكي"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.scroll = ft.ScrollMode.AUTO

    chat_box = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    user_input = ft.TextField(
        hint_text="اكتب سؤالك الديني هنا...",
        expand=True,
        border_color="#10b981",
        on_submit=send_message
    )

    send_btn = ft.ElevatedButton(
        content=ft.Text("إرسال", color="#ffffff"),
        bgcolor="#10b981",
        on_click=send_message
    )

    input_row = ft.Row([user_input, send_btn], spacing=10)
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column([chat_box, input_row]),
            expand=True,
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
